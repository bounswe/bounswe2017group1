from rest_framework import serializers
from django.contrib.auth.models import User
#from .models import UserProfile


class UserSeralizer(serializers.ModelSerializer):
    #users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        #fields = ('users', 'bio', 'city')
        fields = '__all__'