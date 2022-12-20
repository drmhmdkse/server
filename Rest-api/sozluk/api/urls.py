from django.urls import path, include
from .views import WordViewSet, CommentDetailCreateViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'words', WordViewSet, basename="word")
router.register(r'comments', CommentDetailCreateViewSet, basename="comment")

urlpatterns = [
    path("v2/", include(router.urls)),
]
