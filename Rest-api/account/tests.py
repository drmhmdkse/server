from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from account.models import CustomUser


class UserRegistrationTestCase(APITestCase):
    url = reverse("account:user-register")
    url_login = reverse("token_obtain_pair")

    # Ok
    def test_user_registration(self):

        data = {
            "username": "durdu",
            "password": "Durdu.1965",
            "first_name": "Durdu",
            "email": "drmhmdka@hotmail.com"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)  # 201 mean is created

    # Ok
    def test_user_invalid_password(self):

        data = {
            "username": "durdu",
            "password": "1", # django için geçeersiz şifre
            "first_name": "Durdu",
            "email": "drmhmdka@hotmail.com"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    # Ok
    def test_unique_name(self):
        self.test_user_registration()
        data = {
            "username": "durdu",
            "password": "Durdu.1965",
            "first_name": "Durdu",
            "email": "drmhmdka@hotmail.com"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    # Ok
    def test_user_authentication_registration(self):
        """
                    session ile giriş yapmış kullanıcı sayfayı görememeli.
        """
        self.test_user_registration()
        self.client.login(username="durdu", password="Durdu.1965")
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    # Ok
    def test_user_authenticated_token_registration(self):
        """
            token ile giriş yapmış kullanıcı sayfayı görememeli.
        """
        self.test_user_registration()
        data = {
            "username": "durdu",
            "password": "Durdu.1965",
            "first_name": "Durdu",
            "email": "drmhmdka@hotmail.com"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_2 = self.client.get(self.url)
        self.assertEqual(403, response_2.status_code)


class UserLogin(APITestCase):
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "durdu"
        self.password = "Durdu.1965"
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)

    # Ok
    def test_user_token(self):
        response = self.client.post(self.url_login, {"username": "durdu", "password": "Durdu.1965"})
        self.assertEqual(200, response.status_code)

    # Ok
    def test_user_invalid_data(self):
        response = self.client.post(self.url_login, {"username": "invalidusername", "password": "Durdu.1965"})
        self.assertEqual(401, response.status_code)

    # Ok
    def test_user_empty_data(self):
        response = self.client.post(self.url_login, {"username": "", "password": ""})
        self.assertEqual(400, response.status_code)