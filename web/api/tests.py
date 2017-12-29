from django.test import TestCase
import json
from urllib2 import Request, urlopen
#hostname = "http://ec2-18-196-2-56.eu-central-1.compute.amazonaws.com/api/"
hostname = "http://localhost:8000/api/"

def singup():
    url     = hostname + "users/signup/"
    headers = {'Content-Type':'application/json'}
    body    = json.dumps({
               "username": "unittestuser",
               "email": "test@example.com",
               "password": "password12345"
              })
    request = Request(url, headers=headers, data=body)
    response_body = urlopen(request).read()
    print json.load(response_body)

def getToken():
    try:
        url     = hostname + "users/signin/"
        headers = {'Content-Type':'application/json'}
        body    = json.dumps({
               "username": "unittestuser",
               "password": "password12345"
            })
        request = Request(url, headers=headers, data=body)
        response_body = urlopen(request).read()
        return json.loads(response_body)['token']
    except Exception as ex:
        return "";


class HeritageTestCase(TestCase):
    #needed to pass the same token
    def __init__(self, *args, **kwargs):
        super(HeritageTestCase, self).__init__(*args, **kwargs)
        self.token     = getToken()
        self.newItemId = -1

#    Works before each method
#    def setUp(self):
#        global token
#        if (self.token == ""):
#            singup()
#            token = getToken()

    def test_heritage_create(self):
        """Animals that can speak are correctly identified"""
        url = hostname + "items/"
        body = json.dumps({
                           "title": "TestTitle",
                           "description": "TestDescription",
                            "tags":
                            [
                                {
                                    "name": "testTag"
                                }
                            ]
                          })
        headers  = {'Content-Type':'application/json', "Authorization":"Token " + self.token }
        request  = Request(url,headers=headers,data=body)
        response = urlopen(request).read()
        response_obj = json.loads(response)
        self.newItemId = response_obj['id']
        self.assertEqual(response.getCode(), 201)

    def test_heritage_get_all(self):
        url = hostname + "items/"
        headers  = {'Content-Type':'application/json', "Authorization":"Token " + self.token }
        request  = Request(url,headers=headers)
        response = urlopen(request).read()
        self.assertEqual(response.getCode(), 200)

    def test_heritage_get_top(self):
        url = hostname + "items/top/"
        headers  = {'Content-Type':'application/json', "Authorization":"Token " + self.token }
        request  = Request(url,headers=headers)
        response = urlopen(request).read()
        self.assertEqual(response.getCode(), 200)

    def test_heritage_get_trending(self):
        url = hostname + "items/trending/"
        headers  = {'Content-Type':'application/json', "Authorization":"Token " + self.token }
        request  = Request(url,headers=headers)
        response = urlopen(request).read()
        self.assertEqual(response.getCode(), 200)

    def test_heritage_get_new(self):
        url = hostname + "items/new/"
        headers  = {'Content-Type':'application/json', "Authorization":"Token " + self.token }
        request  = Request(url,headers=headers)
        response = urlopen(request).read()
        self.assertEqual(response.getCode(), 200)

    def test_heritage_get_created_item(self):
        if self.newItemId != -1:
            url = hostname + "items/" + self.newItemId
            headers  = {'Content-Type':'application/json', "Authorization":"Token " + self.token }
            request  = Request(url,headers=headers)
            response = urlopen(request).read()
            self.assertEqual(response.getCode(), 200)
        else:
            print "Skipping the get item case, since it has failed to create new"
            self.assertEqual(True,False)
