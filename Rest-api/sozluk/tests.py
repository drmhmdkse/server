from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.


class UserResgistrationTestCase(APITestCase):
    url = reverse("rest_framework:login")

    def test_user_registration(self):
        """
            ensure we can log in with correct values
        """

        data = {
            "username": "durdu",
            "password": "durdu"
        }

        response = self.client.post(self.url, data)
        print(self.url)
        self.assertEqual(302, response.status_code)  # success log in
        # todo development ve production diye ayır
