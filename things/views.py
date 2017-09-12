from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from things.models import Thing, ThingMeta
from things.serializers import ThingSerializer, ThingMetaSerializer


class ThingViewSet(ModelViewSet):
    """ Thing resource. """
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    lookup_field = 'id'
    filter_backends = (SearchFilter,)
    search_fields = ('alias', 'id', 'type', 'active')


class ThingMetaViewSet(ModelViewSet):
    """ ThingMeta resource. """

    def get_queryset(self):
        return ThingMeta.objects.filter(thing=self.kwargs['thing_id'])

    serializer_class = ThingMetaSerializer
    lookup_field = 'id'
    filter_backends = (SearchFilter,)
    search_fields = ('key', 'value',)

    def create(self, request, *args, thing_id=None, **kwargs):
        self.request.thing_id = thing_id
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer, thing_id=None):
        serializer.save(thing_id=self.request.thing_id)
