from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Face


class FaceSerializer(ModelSerializer):
    class Meta:
        model = Face
        fields = [
            'face_image',
            'face_id',
        ]
        read_only_fields = ['created_at', 'updated_at']


class UnknownFaceSerializer(Serializer):
    face_image = ImageField()

    def update(self, instance, validated_data):
        instance.face_image = validated_data.get('face_image', instance.face_image)
        return instance

class RecognitionSerializer(ModelSerializer):
    class Meta:
        model = Face
        fields = [
            'face_image',
        ]
        read_only_fields = ['created_at', 'updated_at']
