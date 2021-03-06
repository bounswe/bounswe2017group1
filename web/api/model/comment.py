
from __future__ import unicode_literals

from django.db import models
from profile import Profile
from heritage import Heritage



class Comment(models.Model):
    '''
    Comment model to store comment data in heritage items
    '''
    text = models.TextField(max_length=200)
    heritage = models.ForeignKey(Heritage)
    creator = models.ForeignKey(Profile)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        '''

        :return: self.text
        '''
        return self.text


