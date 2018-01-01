from django.test import TestCase
import json, requests
from urllib2 import Request, urlopen
from django.test.client import Client

#hostname = "http://ec2-18-196-2-56.eu-central-1.compute.amazonaws.com/api/"


class ItemTestCase(TestCase):
    def setUp(self):
        self.url_signup = '/api/users/signup/'
        self.url_signin = '/api/users/signin/'
        self.url_heritage = "/api/items/"

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
        
        #print "XXXXXXX ", response

        #Signin user
        response = self.client.post(self.url_signin, 
            json.dumps({
                "username":self.username,
                "password":self.password
                }), 
            content_type='application/json')
        self.token = response.data['token']
        #print "TOKEN ",self.token

    def test_heritage_create(self):
        #print "TOKEN:::", self.token
        headers  = {'Content-Type':'application/json', "Authorization": self.token}
        response = self.client.post(self.url_heritage,
            json.dumps({
                           "title": "TestTitle",
                           "description": "TestDescription",
                            "tags": []
                          }), 
            content_type='application/json', 
            HTTP_AUTHORIZATION='Token ' + self.token)
        #Authorization should be HTTP_AUTHORIZATION
        print "ID: ",response.data['id'], "--- Status code: ", response.status_code
        self.newItemId = response.data['id']
        self.assertEqual(response.status_code, 201)










