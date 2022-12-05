from django.urls import path
from .views import ListUsersAPiView

urlpatterns = [
    path('v2/users/',ListUsersAPiView.as_view(), name='users-listesi'),

]