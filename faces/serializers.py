from rest_framework.serializers import ModelSerializer

from faces.fields import Base64ImageField
from .models import Face


class FaceSerializer(ModelSerializer):
    face_image = Base64ImageField()

    class Meta:
        model = Face
        fields = [
            'id',
            'face_image',
            'face_id',
            'face_name',
            'unknown',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'unknown']


class UnknownFaceSerializer(ModelSerializer):
    face_image = Base64ImageField()

    class Meta:
        model = Face
        fields = [
            'face_image',
            'unknown',
        ]
        read_only_fields = ['unknown', 'created_at', 'updated_at']
