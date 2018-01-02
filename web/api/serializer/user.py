from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer class to generate new items of Django.User Model and serialize members of it

    '''
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, min_length=6)

    def create(self, validated_data):
        '''
        creates a new item of User Model
        :param validated_data: User Model validated date
        :return: new User
        '''
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
