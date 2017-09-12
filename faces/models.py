import os
from django.db import models
from django.dispatch import receiver

from common.models import DateTimeMixin


class Face(DateTimeMixin, models.Model):
    face_id = models.CharField(max_length=150, blank=False, null=False)
    face_image = models.ImageField()
    face_name = models.CharField(max_length=150, blank=True, null=True)
    unknown = models.BooleanField(default=False)


@receiver(models.signals.post_delete, sender=Face)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Face` object is deleted.
    """
    if instance.face_image:
        if os.path.isfile(instance.face_image.path):
            os.remove(instance.face_image.path)
