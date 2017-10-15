import time
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import RequestsClient

from TestApp.models import User


class AuthentificationTestCase(TestCase):
    def test_registration(self):
        userName = 'vasia'
        password = '123'

        self.assertEqual(User.objects.count(), 0)

        response = self.client.get(reverse('register', args={password, userName}))
        expected = User(name=userName, password=password)
        time.sleep(1)
#        result = User.objects.get(name=userName)

#        self.assertEqual(result, expected)
        self.assertEqual(response.status_code, 200)

    def test_auth(self):
        userName = 'vitia'
        password = '1234'
        user = User(name=userName, password=password)
        user.save()

        response = self.client.get(reverse('auth', args=[userName, password]))

        self.assertEqual(response.status_code, 200)