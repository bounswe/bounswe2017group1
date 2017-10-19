from rest_framework import serializers
from django.contrib.auth.models import User
#from .models import UserProfile


class UserSeralizer(serializers.ModelSerializer):
    #users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        #fields = ('users', 'bio', 'city')


        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(validated_data['password'])
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

        #fields = '__all__'