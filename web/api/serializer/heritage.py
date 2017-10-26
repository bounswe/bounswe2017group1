from ..model.heritage import Heritage

from rest_framework import serializers

class HeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = ('title', 'description', 'location', 'creator', 'creation_date', 'event_date');
        related_object = 'profile'


