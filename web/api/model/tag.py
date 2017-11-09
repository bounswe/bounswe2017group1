from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=25, blank=True, null=True)


    def __str__(self):
        return self.name