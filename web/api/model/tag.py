from __future__ import unicode_literals

import json
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)
    related_list = models.CharField(max_length=200, blank=True, null=True)

    def setlist(self, x):
        self.related_list = json.dumps(x)

    def getlist(self):
        if self.related_list:
            tt = self.related_list.split(' ')
            if tt[len(tt)-1] == '':
                tt = tt[:len(tt)-1]
            return tt

        return None
        #return json.loads(self.related_list)

    def __str__(self):
        return self.name
