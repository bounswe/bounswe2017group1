from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Images/ProfilePhotos/{0}/{1}'.format(instance.username, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to=user_directory_path, default='Images/no_image.jpg')


    def __str__(self):
        return self.username
