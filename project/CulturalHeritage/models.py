# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=50)
	gender = models.CharField(max_length=10)
	photo_path = models.CharField(max_length=50)

	def __str__(self):
		return self.user.name


class Heritage(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	creator = models.ForeignKey(Profile)
	creation_date = models.DateTimeField()
	event_date = models.DateTimeField()
	location = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class Media(models.Model):
	type = models.CharField(max_length=10)
	data_path = models.CharField(max_length=50)
	heritage = models.ForeignKey(Heritage)

class Comment(models.Model):
	text = models.TextField();
	heritage = models.ForeignKey(Heritage)
	creator = models.ForeignKey(Profile)
	#parent = models.ForeignKey(Comment)
	date = models.DateTimeField()


class Vote(models.Model):
	value = models.BooleanField()
	user = models.ForeignKey(Profile)
	heritage = models.ForeignKey(Heritage)


class Tag(models.Model):
	name = models.CharField(max_length=25)
	category = models.CharField(max_length=25)
	heritage = models.ManyToManyField(Heritage)



"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""


"""
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user, bio='my bio')
        user_profile.save()

post_save.connect(create_profile, sender=User)
"""
