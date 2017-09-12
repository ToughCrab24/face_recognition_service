from rest_framework.serializers import ModelSerializer
from .models import Face


class FaceSerializer(ModelSerializer):
    class Meta:
        model = Face
        fields = [
            'face_image',
            'face_id',
        ]
        read_only_fields = ['created_at', 'updated_at']
