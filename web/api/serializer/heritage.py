from api.model.heritage import Heritage
from api.serializer.vote import VoteSerializer
from rest_framework import serializers
from api.serializer.tag import TagSerializer
from api.model.tag import Tag

class HeritageSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()
    #votes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #Heritage item may not have a tag or have one or more than one tag.
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = Heritage
        fields = '__all__'
        related_object = ('profile')

    #When creating heritage item, you need to add tags.
    #When adding "tags", this function is needed.

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print tags_data
        heritage = Heritage.objects.create(**validated_data)
        for tag_data in tags_data:
           Tag.objects.create(heritage=heritage, **tag_data).save()
        return heritage

    def get_upvote_count(self, obj):
        votes = obj.votes.all()
        return votes.filter(value=True).count()

    def get_downvote_count(self, obj):
        votes = obj.votes.all()
        return votes.filter(value=False).count()

