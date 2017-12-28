# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from heritage import Heritage

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Images/{0}/{1}'.format(instance.heritage.id, filename)


class Media(models.Model):
    type = models.CharField(max_length=10)
    heritage = models.ForeignKey(Heritage, related_name='medias', on_delete=models.CASCADE)
    #TODO add Images/<item_id>/imagename
    image = models.ImageField(upload_to = user_directory_path, null=True, blank=True)
    video_url = models.CharField(max_length=100, null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image
