from django.urls import path
from .views import WordDetailUpdateApiView,WordListCreateApiView,CommentCreateApiView,CommentDetailApiView

urlpatterns = [
    path('v2/word/',WordListCreateApiView.as_view(), name='makale-listesi'),
    path("v2/word/<str:name>",WordDetailUpdateApiView.as_view(),name="word-detail"),
    path("v2/word/<int:pk>/comment", CommentCreateApiView.as_view(), name="comment-create"),
    path("v2/comment/<int:pk>",CommentDetailApiView.as_view(),name="comment-detail"),

]