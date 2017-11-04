# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from heritage import Heritage

class Media(models.Model):
	type = models.CharField(max_length=10)
	data_path = models.CharField(max_length=50)
	heritage = models.ForeignKey(Heritage)
	creation_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)


