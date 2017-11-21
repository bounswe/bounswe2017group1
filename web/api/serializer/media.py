from api.model.media import Media
from rest_framework import serializers


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Media
        fields = ('type', 'image', 'heritage', 'creation_date', 'update_date')

