from django.test import Client, TestCase
from .models import Student
import requests
from rest_framework.test import APIRequestFactory
from .serializers import StudentSerializer

class PostViewTestCase(TestCase):
    def test_post_creation(self):
        c = Client()  # instantiate the Django test client
        response = c.post('/api/students', {'name': 'Hakan', 'number': '2013400153', 'gpa': '3.40', 'department': 'cmpE', 'university':'Bogazici'})
        self.assertEqual(response.status_code, 201)
        retS = Student.objects.filter(name = 'Hakan', number =2013400153)[0]
        self.assertEquals(retS.number, 2013400153)

    def test_get_creation(self):
        c = APIRequestFactory()
        response = c.get('/api/students')
        self.assertNotEqual(None, response)

    def test_Student_Serializer(self):
        newS = Student(name = 'Taha', number = 2013400174, gpa = '3.3', department = 'CMPE' , university = 'BOUN')
        yaml = StudentSerializer(newS)
        self.assertEquals({'department': u'CMPE', 'university': u'BOUN', 'name': u'Taha', 'gpa': 3.3, 'number': 2013400174},yaml.data)
