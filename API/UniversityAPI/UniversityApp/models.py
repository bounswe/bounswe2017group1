from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()
	gpa = models.FloatField()
	department = models.CharField(max_length=50, default='none')
	university = models.CharField(max_length=50, default='none')

	def __str__(self):
		return self.name


class HeritageItem(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name