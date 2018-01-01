from django.test import TestCase
import json, requests
from urllib2 import Request, urlopen
from django.test.client import Client

class RecommendationTestCase(TestCase):
    def setUp(self):
        self.url_signup   = '/api/users/signup/'
        self.url_signin   = '/api/users/signin/'
        self.url_heritage = '/api/items/'
        self.url_recommendation_user = '/api/recommendation/user/'
        self.url_recommendation_item = '/api/recommendation/heritage/'
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

        #Heritage item to recommend
        response = self.client.post(self.url_heritage,
            json.dumps({
                           "title": "TestTitle",
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

    def test_user_recommendation(self):

        response = self.client.get(self.url_recommendation_user,
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 200)

    def test_item_recommendation(self):

        response = self.client.get(self.url_recommendation_item + str(self.ItemId),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 200)






