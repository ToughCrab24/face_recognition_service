from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import (
    ThingViewSet,
    ThingMetaViewSet)

# router = SimpleRouter()
# meta_router = SimpleRouter()
# router.register('', ThingViewSet)
# meta_router.register('meta', ThingMetaViewSet)


router = routers.SimpleRouter()
router.register(r'things', ThingViewSet)

meta_router = routers.NestedSimpleRouter(router, r'things', lookup='thing')
meta_router.register(r'meta', ThingMetaViewSet, base_name='thing-meta')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(meta_router.urls)),
]

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^(?P<thing_id>[\w\-]+)/', include(meta_router.urls)),
# ]
