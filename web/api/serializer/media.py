from api.model.media import Media
from rest_framework import serializers


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, allow_empty_file=True)

    class Meta:
        model = Media
        fields = ('__all__')

