from rest_framework import serializers

from .models import Amenitie


class AmenitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenitie
        fields = ('id', 'name', 'slug')
