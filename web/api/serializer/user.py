from rest_framework import serializers
from django.contrib.auth.models import User
from profile import Profile

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'location', 'gender', 'photo_path')

