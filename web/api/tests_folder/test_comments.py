from django.test import TestCase
import json, requests
from urllib2 import Request, urlopen
from django.test.client import Client


class CommentsTestCase(TestCase):
    def setUp(self):
        self.url_signup   = '/api/users/signup/'
        self.url_signin   = '/api/users/signin/'
        self.url_heritage = '/api/items/'
        self.url_comment  = '/api/comments/'

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

        #Heritage item to comment
        response = self.client.post(self.url_heritage,
            json.dumps({
                           "title": "TestTitle",
                           "description": "TestDescription",
                            "tags": []
                          }), 
            content_type='application/json', 
            HTTP_AUTHORIZATION='Token ' + self.token)
        #Authorization should be HTTP_AUTHORIZATION
        self.ItemId = response.data['id']

    def test_comment(self):
        #create comment
        response = self.client.post(self.url_comment,
            json.dumps({
                    "text": "Test Comment",
                    "heritage": self.ItemId
                    }),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 201)
        self.commentId = response.data['id']

        #get comment
        response = self.client.get(self.url_comment + str(self.commentId) ,
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)
        self.assertEqual(response.status_code, 200)


        #delete comment
        response = self.client.delete(self.url_comment + str(self.commentId) ,
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 200)
