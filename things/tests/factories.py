from factory.django import DjangoModelFactory


class ThingMetaFactory(DjangoModelFactory):
    class Meta:
        model = 'things.ThingMeta'
        django_get_or_create = ('key', 'value')

    key = 'Test'
    value = 'Data'


class ThingFactory(DjangoModelFactory):
    class Meta:
        model = 'things.Thing'
        django_get_or_create = ('alias', 'type', 'active')

    id = 'some-sensor'
    alias = 'something'
    type = 'BEACON'
    active = True
