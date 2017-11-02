from __future__ import unicode_literals

from django.db import models
from profile import Profile
from heritage import Heritage


class Vote(models.Model):
    value = models.BooleanField()
    voter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="votes")
    heritage = models.ForeignKey(Heritage, on_delete=models.CASCADE, related_name="votes")
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('voter', 'heritage')

