from django.db import models

from common.models import DateTimeMixin


class Face(DateTimeMixin, models.Model):
    face_id = models.CharField(max_length=150, blank=False, null=False)
    face_image = models.ImageField()
