from .models import Town, Motel
from rest_framework import serializers


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('name', 'location')


class MotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motel
        fields = ('id', 'name', 'town', 
        	'latitude', 'latitude','longitude','ranking','telephone', 'website','description')