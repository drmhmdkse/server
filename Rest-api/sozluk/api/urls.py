from django.urls import path, include
from .views import WordViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'words', WordViewSet, basename="word")

urlpatterns = [
    path("v2/", include(router.urls)),
]
