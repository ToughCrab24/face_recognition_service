from django.db import models
from common.fields import SlugPkField
from common.models import DateTimeMixin

choices = (
    ('BEACON', 'BEACON'),
    ('NFC', 'NFC'),
    ('RFID', 'RFID'),
)


class Thing(DateTimeMixin, models.Model):
    id = SlugPkField()
    alias = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=False, choices=choices)
    active = models.BooleanField(default=True)


class ThingMeta(DateTimeMixin, models.Model):
    key = models.CharField(max_length=200, blank=False)
    value = models.CharField(max_length=200, blank=False)
    thing = models.ForeignKey(Thing)
