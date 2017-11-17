from ..model.comment import Comment

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__';
        related_object = 'comment'
