from api.model.heritage import Heritage
from api.serializer.vote import VoteSerializer
from rest_framework import serializers
from api.serializer.tag import TagSerializer
from api.model.tag import Tag
from api.service import heritage, helper


class HeritageSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()
    # votes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Heritage item may not have a tag or have one or more than one tag.
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = Heritage
        fields = '__all__'
        related_object = ('profile')

    # When creating heritage item, you need to add tags.
    # When adding "tags", this function is needed.

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print "\nCreate*******\n"
        heritage = Heritage.objects.create(**validated_data)
        for tag_data in tags_data:
            # tag = Tag.objects.get(name=tag_data['name'])
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            if created:
                concepts_list = helper.get_concepts_from_item(tag.name)
                jdata = {}
                for item in concepts_list:
                    jdata[item[0]] = item[1]

                tag.setlist(jdata)

            heritage.tags.add(tag)
        return heritage

    def update(self, instance, validated_data):
        """Performs an update on a Heritage Item"""

        # Passwords should not be handled with `setattr`, unlike other fields.
        # Django provides a function that handles hashing and
        # salting passwords. That means
        # we need to remove the password field from the
        # `validated_data` dictionary before iterating over it.
        password = validated_data.pop('password', None)
        tags_data = validated_data.pop('tags', [])
        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            setattr(instance, key, value)



        old_tags = heritage.get_all_tags(instance.id)
        #print old_tags


        new_tags_data = []
        for tag in tags_data:
            serializer = TagSerializer(tag)
            new_tags_data.append(serializer.data)

        #print new_tags_data



        for tag_data in new_tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            instance.tags.add(tag)


        if password is not None:
            # `.set_password()`  handles all
            # of the security stuff that we shouldn't be concerned with.
            instance.set_password(password)

        # After everything has been updated we must explicitly save
        # the model. It's worth pointing out that `.set_password()` does not
        # save the model.
        instance.save()

        return instance

    def get_upvote_count(self, obj):
        votes = obj.votes.all()
        return votes.filter(value=True).count()

    def get_downvote_count(self, obj):
        votes = obj.votes.all()
        return votes.filter(value=False).count()
