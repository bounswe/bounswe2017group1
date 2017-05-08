from django.test import Client, TestCase
from .models import Student
import requests
from rest_framework.test import APIRequestFactory
from .serializers import StudentSerializer

class PostViewTestCase(TestCase):
    """
        Tests post method by generating post request, then checks if it is generated in database
    """
    def test_post_method(self):
        c = Client()  # instantiate the Django test client
        # creates post request
        response = c.post('/api/students', {'name': 'Hakan', 'number': '2013400153', 'gpa': '3.40', 'department': 'cmpE', 'university':'Bogazici'})
        # checks post response code
        self.assertEqual(response.status_code, 201)
        #filters posted object
        retS = Student.objects.filter(name = 'Hakan', number =2013400153)[0]
        # checks if posted object created in datebase
        self.assertEquals(retS.number, 2013400153)

    """
        Tests get method by generating get request, then checks if it returns 
    """
    def test_get_method(self):
        c = APIRequestFactory()
        response = c.get('/api/students')
        self.assertNotEqual(None, response)

    """
        Tests if Student serializer works as it is supposed by passing a Student object to serializer
    """
    def test_Student_Serializer(self):
        newS = Student(name = 'Taha', number = 2013400174, gpa = '3.3', department = 'CMPE' , university = 'BOUN')
        yaml = StudentSerializer(newS)
        self.assertEquals({'department': u'CMPE', 'university': u'BOUN', 'name': u'Taha', 'gpa': 3.3, 'number': 2013400174},yaml.data)
