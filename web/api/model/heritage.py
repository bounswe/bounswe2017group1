# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profile import Profile
from django.contrib.auth.models import User
from tag import Tag


class Heritage(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='heritage_id')

    def __str__(self):
        return self.title
