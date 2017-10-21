from __future__ import unicode_literals

from django.db import models
from profile import Profile
from heritage import Heritage


class Vote(models.Model):
    value = models.BooleanField()
    user = models.ForeignKey(Profile)
    heritage = models.ForeignKey(Heritage)