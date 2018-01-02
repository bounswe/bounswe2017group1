# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from heritage import Heritage



class Video(models.Model):
    '''
    Model to store video URLs connected to the heritage item
    '''
    heritage = models.OneToOneField(Heritage, related_name='video', on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video_url
