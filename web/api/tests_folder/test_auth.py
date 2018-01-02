from django.test import TestCase
import json
from django.test.client import Client



class AuthTestCase(TestCase):
    def setUp(self):
        self.url_signup  = '/api/users/signup/'
        self.url_signin  = '/api/users/signin/'
        self.url_signout = '/api/users/signout/'

        self.username = "unittestuser"
        self.email    = "test@example.com"
        self.password = "Password.12345"
        self.client   = Client()

    def test_auth(self):
        #Signup user
        response = self.client.post(self.url_signup,
            json.dumps({

                "username":self.username,
                "email":self.email,
                "password":self.password
                }),

            content_type='application/json')

        self.assertEqual(response.status_code, 201)

        response = self.client.post(self.url_signin,
            json.dumps({
                           "username": self.username,
                           "password": self.password
                        }),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.token = response.data['token']


        #test_signout
        response = self.client.post(self.url_signout,
                                   content_type='application/json',
                                   HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 200)


        response = self.client.post(self.url_signout,
                                   content_type='application/json',
                                   HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 401)




