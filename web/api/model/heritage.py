# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profile import Profile
from django.contrib.auth.models import User
from tag import Tag
from django.db.models.signals import post_save, pre_migrate, post_migrate,pre_save
from django.dispatch import receiver
import datetime
import re

class Heritage(models.Model):
    '''
    Main item to store heritages items in CultureMania App
    '''
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
    location = models.CharField(max_length=100, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='heritage_id')
    event_year = models.IntegerField(null=True)

    def __str__(self):
        return self.title


    def getLocationAsList(self):
        '''

        :return: parsed location
        '''

        location_words = []
        if self.location:
            pattern = re.compile("^\s+|\s*,\s*|\s+$")
            location_words = [x for x in pattern.split(self.location) if x]

        return location_words

@receiver(post_save, sender=Heritage)
def my_handler(sender, instance, **kwargs):
    '''
    handles event_year field accordingly to the DB changes
    '''

    if instance.event_year == None:
        instance.event_year = instance.event_date.year


