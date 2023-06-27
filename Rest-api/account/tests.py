from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.utils import json

from account.models import CustomUser


class UserRegistrationTestCase(APITestCase):
    url = reverse("account:user-register")
    url_login = reverse("token_obtain_pair")

    # Ok
    def test_user_registration(self):

        data = {
            "username": "test",
            "password": "Test.1881",
            "first_name": "Durdu",
            "email": "test@gmail.com"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)  # 201 mean is created

    # Ok
    def test_user_invalid_password(self):

        data = {
            "username": "test",
            "password": "1",  # django için geçeersiz şifre
            "first_name": "Durdu",
            "email": "test@gmail.com"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    # Ok
    def test_unique_name(self):
        self.test_user_registration()
        data = {
            "username": "test",
            "password": "Test.1881",
            "first_name": "Durdu",
            "email": "test@gmail.com"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    # Ok
    def test_user_authentication_registration(self):
        """
                    session ile giriş yapmış kullanıcı sayfayı görememeli.
        """
        self.test_user_registration()
        self.client.login(username="test", password="Test.1881")
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    # Ok
    def test_user_authenticated_token_registration(self):
        """
            token ile giriş yapmış kullanıcı sayfayı görememeli.
        """
        self.test_user_registration()
        data = {
            "username": "test",
            "password": "Test.1881",
            "first_name": "Durdu",
            "email": "test@gmail.com"
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
        self.username = "test"
        self.password = "Test.1881"
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)

    # Ok
    def test_user_token(self):
        response = self.client.post(self.url_login, {"username": "test", "password": "Test.1881"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))

    # Ok
    def test_user_invalid_data(self):
        response = self.client.post(self.url_login, {"username": "invalidusername", "password": "Test.1881"})
        self.assertEqual(401, response.status_code)

    # Ok
    def test_user_empty_data(self):
        response = self.client.post(self.url_login, {"username": "", "password": ""})
        self.assertEqual(400, response.status_code)


class UserChangePassword(APITestCase):
    url = reverse("account:change-password")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "test"
        self.password = "Test.1881"
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)


    def login_with_token(self):
        data = {
            "username": "test",
            "password": "Test.1881"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_is_not_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_with_valid_informations(self):
        self.login_with_token()
        data = {
            "old_password": "Test.1881",
            "new_password": "Test.1881212"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(204, response.status_code)


    def test_with_wrong_informations(self):
        self.login_with_token()
        data = {
            "old_password": "asdaasdsd",
            "new_password": "asdasdas123asd456"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)


class UserProfileUpdate(APITestCase):
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "test"
        self.password = "Test.1881"
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)
        self.url = reverse("account:user-edit",kwargs={"id":self.user.id})
    def login_with_token(self):
        data = {
            "username": "test",
            "password": "Test.1881"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_is_not_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_with_valid_informations(self):
        self.login_with_token()
        data = {
            "first_name": "Testo",
            "last_name": "taylanto",
            "avatar":None,
            "email": "godjesus@godmail.com"
        }

        response = self.client.put(self.url, data, format="json")
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content), data)
