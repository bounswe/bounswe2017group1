# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profile import Profile
from django.contrib.auth.models import User
from tag import Tag

class Heritage(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(Profile)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    event_date = models.DateTimeField(blank=True)
    location = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
