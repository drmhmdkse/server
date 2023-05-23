from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.


class UserResgistrationTestCase(APITestCase):
    url = reverse("rest_framework:login")



