from django.urls import path
from .views import UserDetailApiView, UserPasswordChangeApiView, UserRegisterApiView, UserEditApiView

urlpatterns = [
    path("profile/<int:id>", UserDetailApiView.as_view(), name="user-profilos"),
    path("profile/change-password", UserPasswordChangeApiView.as_view(), name="change-password"),
    path("register", UserRegisterApiView.as_view(), name="user-register"),
    path("profile/<int:id>/edit", UserEditApiView.as_view(), name="user-edit")


]
