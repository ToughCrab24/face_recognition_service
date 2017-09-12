from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from faces.views import FaceViewSet

router = SimpleRouter()
router.register('faces', FaceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
