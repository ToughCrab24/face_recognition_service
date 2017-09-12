from django.contrib import admin

from things.models import Thing, ThingMeta

admin.site.register(Thing)
admin.site.register(ThingMeta)
