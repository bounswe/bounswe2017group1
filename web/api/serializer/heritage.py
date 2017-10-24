from ..model.heritage import Heritage

from rest_framework import serializers

class HeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = '__all__';

