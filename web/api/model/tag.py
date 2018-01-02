from __future__ import unicode_literals

import json
from django.db import models


class Tag(models.Model):
    '''
    Model to store Tags and related tags to that tag, which are connected to Heritage Item
    '''
    name = models.CharField(max_length=25)
    related_list = models.CharField(max_length=200, blank=True, null=True)

    def setlist(self, x):
        '''
        sets related_list
        :param x: list of tag list
        :return: tag list dumped as a single string
        '''
        self.related_list = json.dumps(x)

    def getlist(self):
        '''
        gets related_list
        :return: related list string as a list
        '''
        if self.related_list:
            tt = self.related_list.split(' ')
            if tt[len(tt)-1] == '':
                tt = tt[:len(tt)-1]
            return tt

        return None
        #return json.loads(self.related_list)

    def __str__(self):
        return self.name
