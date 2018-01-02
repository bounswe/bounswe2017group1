from api.models import Vote
from rest_framework import serializers


class VoteSerializer(serializers.ModelSerializer):
    '''
    Serializer class to generate new items of Vote Model and also serialize its members

    '''
    class Meta:
        model = Vote
        fields = "__all__"
