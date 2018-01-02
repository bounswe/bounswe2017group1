from django.test import TestCase
import json, requests
from urllib2 import Request, urlopen
from django.test.client import Client

#hostname = "http://ec2-18-196-2-56.eu-central-1.compute.amazonaws.com/api/"


class VotesTestCase(TestCase):
    def setUp(self):
        self.url_signup   = '/api/users/signup/'
        self.url_signin   = '/api/users/signin/'
        self.url_heritage = '/api/items/'
        self.url_votes    = '/api/votes/'

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

        #Heritage item to vote
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
        self.upvoteCount = response.data['upvote_count']
        self.downvoteCount = response.data['downvote_count']

    def test_vote_upvote(self):
        #test_heritage_upvote:
        response = self.client.post(self.url_votes,
            json.dumps({
                            "value": True,
                            "heritage": self.ItemId
                        }),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.upvoteCount + 1, response.data['upvote_count'])

        #delete vote
        response = self.client.delete(self.url_votes,
            json.dumps({
                            "heritage": self.ItemId
                        }),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 200)
    def test_vote_downvote(self):
        #test_heritage_upvote:
        response = self.client.post(self.url_votes,
            json.dumps({
                            "value": False,
                            "heritage": self.ItemId
                        }),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.downvoteCount + 1, response.data['downvote_count'])

        #delete vote
        response = self.client.delete(self.url_votes,
            json.dumps({
                            "heritage": self.ItemId
                        }),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token)

        self.assertEqual(response.status_code, 200)






