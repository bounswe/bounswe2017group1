# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profile import Profile
from tag import Tag

class Heritage(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    creator = models.ForeignKey(Profile)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
