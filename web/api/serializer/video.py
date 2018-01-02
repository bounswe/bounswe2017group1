from api.model.video import Video
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    '''
    Serializer class to generate new items of Video Model and also serialize its members

    '''
    class Meta:
        model = Video
        fields = ('__all__')
