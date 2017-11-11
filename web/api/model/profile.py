# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	username = models.CharField(max_length=50, unique=True)
	location = models.CharField(max_length=50, blank=True)
	gender = models.CharField(max_length=10, blank=True)
	photo_path = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.username
