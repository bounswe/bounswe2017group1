from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()
	gpa = models.FloatField()