from __future__ import unicode_literals

from django.db import models
from profile import Profile
from heritage import Heritage

class Comment(models.Model):
    text = models.TextField();
    heritage = models.ForeignKey(Heritage)
    creator = models.ForeignKey(Profile)
    #parent = models.ForeignKey(Comment)
    date = models.DateTimeField()