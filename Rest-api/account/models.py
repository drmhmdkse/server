from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# settings içinde AUTH_USER_MODEL = 'account.CustomUser' olarak ayarla ve her yerde bu şekilde kullan


class CustomUser(AbstractUser):
    avatar = models.ImageField(default="avatars/default.jpg", upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.username

