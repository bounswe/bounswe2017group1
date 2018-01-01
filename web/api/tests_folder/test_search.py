from django.test import TestCase
import json, requests
from urllib2 import Request, urlopen
from django.test.client import Client

class RecommendationTestCase(TestCase):
    def setUp(self):
        self.url_signup   = '/api/users/signup/'
        self.url_signin   = '/api/users/signin/'
        self.url_heritage = '/api/items/'
        self.url_search = '/api/search/'

        self.username = "unittestuser"
        self.email = "test@example.com"
        self.password = "Password.12345"
        self.client = Client()

        #Signup user
        response = self.client.post(self.url_signup,
            json.dumps({

                "username":self.username,
                "email":self.email,
                "password":self.password
                }),

            content_type='application/json')

        #Signin user
        response = self.client.post(self.url_signin, 
            json.dumps({
                "username":self.username,
                "password":self.password
                }), 
            content_type='application/json')
        self.token = response.data['token']

        #Heritage item to search
        response = self.client.post(self.url_heritage,
            json.dumps({
                           "title": "TestTitle12345",
                           "description": "TestDescription",
                            "tags": [
                                {
                                "name": "Food"
                                },
                                {
                                "name": "History"
                                }
                            ]
                          }), 
            content_type='application/json', 
            HTTP_AUTHORIZATION='Token ' + self.token)
        #Authorization should be HTTP_AUTHORIZATION
        self.ItemId = response.data['id']

    def test_search(self):
        response = self.client.post(self.url_search,
            json.dumps(
                {
                    "query": "TestTitle12345",
                    "filters":{}
                }
            ),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code,200)
        self.assertEqual(self.ItemId,response.data[0]["id"])


