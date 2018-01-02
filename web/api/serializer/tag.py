from api.model.tag import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    '''
    Serializer class to generate new items of Tag Model and also serilize with only id and name fields
    '''
    class Meta:
        model = Tag
        fields = ("id", "name")


class ExtendedTagSerializer(serializers.ModelSerializer):
    '''
    Serializer class to generate new items of Tag Model and also serialize with all fields

    '''
    class Meta:
        model = Tag
        fields = '__all__'
