# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from faces.face_recognition import find_face
from faces.models import Face
from faces.serializers import FaceSerializer, UnknownFaceSerializer


# Face registration
# Adding known faces to our database and tagging
# them with the right data such as name etc.
class FaceViewSet(ModelViewSet):
    """ Face resource. """
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    lookup_field = 'id'


class FaceProcessor(APIView):
    queryset = Face.objects.all()
    serializer_class = UnknownFaceSerializer
    lookup_field = 'id'

    def post(self, request):
        data = request.data
        data['unknown'] = True

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        unknown_image_path = serializer.data['face_image']

        # get all of our known faces
        known_faces = Face.objects.filter(unknown=False)

        if len(known_faces) == 0:
            return Response('We have no known faces, please add one', status=status.HTTP_400_BAD_REQUEST)

        # judgement call
        matches = find_face(unknown_image_path, known_faces)
        # return the result
        is_match = len(matches) > 0
        response_data = {
            'is_match': is_match,
            'message': 'This is {}'.format(matches[0]['face_name']) if is_match else 'Sorry we don\'t know this face',
            'matches': matches
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
