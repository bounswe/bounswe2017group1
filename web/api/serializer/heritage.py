from api.model.heritage import Heritage
from api.serializer.vote import VoteSerializer
from rest_framework import serializers


class HeritageSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()
    #votes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Heritage
        fields = '__all__'
        related_object = ('profile')

    def get_upvote_count(self, obj):
        votes = obj.votes.all()
        return votes.filter(value=True).count()

    def get_downvote_count(self, obj):
        votes = obj.votes.all()
        return votes.filter(value=False).count()

