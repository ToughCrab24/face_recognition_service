# Create your views here.
from rest_framework.viewsets import ModelViewSet

from faces.models import Face
from faces.serializers import FaceSerializer


class FaceViewSet(ModelViewSet):
    """ Thing resource. """
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    lookup_field = 'id'
