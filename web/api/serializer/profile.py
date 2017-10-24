
from rest_framework import serializers
from api.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=50,required=False)
    gender = serializers.CharField(max_length=10,required=False)
    photo_path = serializers.CharField(max_length=50,required=False)
    class Meta:
        model = Profile
        fields = "__all__"
