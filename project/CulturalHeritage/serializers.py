from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
#from .models import UserProfile


class UserSeralizer(serializers.ModelSerializer):
    #users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=True, write_only=True, min_length=6)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])

        if 'first_name' in validated_data:
            user.first_name = validated_data['first_name']
        if 'last_name' in validated_data:
            user.last_name = validated_data['last_name']

        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        #extra_kwargs = {'password': {'write_only': True}}



        #fields = '__all__'