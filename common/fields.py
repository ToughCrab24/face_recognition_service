from django.db import models


class SlugPkField(models.SlugField):
    def __init__(self, *args, primary_key=True, max_length=200, blank=False, unique=True, **kwargs):
        kwargs['primary_key'] = primary_key
        kwargs['max_length'] = max_length
        kwargs['blank'] = blank
        kwargs['unique'] = unique
        super(SlugPkField, self).__init__(*args, **kwargs)
