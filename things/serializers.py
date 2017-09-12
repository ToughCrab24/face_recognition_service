from rest_framework.serializers import ModelSerializer
from things.models import Thing, ThingMeta


class ThingMetaSerializer(ModelSerializer):

    class Meta:
        model = ThingMeta
        fields = [
            'key',
            'value',
            'thing_id',
        ]
        read_only_fields = ['created_at', 'updated_at']


class ThingSerializer(ModelSerializer):

    class Meta:
        model = Thing
        fields = [
            'id',
            'alias',
            'type',
            'active',
        ]
        read_only_fields = ['created_at', 'updated_at']

