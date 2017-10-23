from rest_framework import serializers
from django.contrib.auth.models import User
from profile import Profile

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.HyperlinkedModelSerializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, min_length=6)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])

        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'location', 'gender', 'photo_path')

