from api.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializer class to generate new items of Profile Model and also serialize it

    '''
    class Meta:
        model = Profile
        fields = '__all__'


