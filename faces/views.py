# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from faces.models import Face
from faces.serializers import FaceSerializer


class FaceViewSet(ModelViewSet):
    """ Face resource. """
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    lookup_field = 'id'


class FaceProcessor(APIView):

    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    lookup_field = 'id'

    def post(self):
        # grab the image

        # lookup files to compare against
        # Face.objects.all()

        # judement call


        # return the result

        pass

