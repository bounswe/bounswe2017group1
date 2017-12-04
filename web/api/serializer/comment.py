from ..model.comment import Comment

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    creator_image_path = serializers.SerializerMethodField()
    creator_username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__';
        related_object = 'comment'

    def get_is_owner(self, obj):
        if 'requester_profile_id' in self.context:
            requester_id = self.context['requester_profile_id']
            if requester_id == obj.creator.pk:
                return True
        return False

    def get_creator_username(self, obj):
        return obj.creator.username

    def get_creator_image_path(self, obj):
        gender = obj.creator.gender.lower()
        if gender.startswith('m'):
            return '/media/avatars/m' + str(obj.creator.pk % 8 + 1) + '.png'
        elif gender.startswith('f'):
            return '/media/avatars/f' + str(obj.creator.pk % 8 + 1) + '.png'
        else:
            return '/media/avatars/doge.png'

