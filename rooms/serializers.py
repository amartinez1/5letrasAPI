from .models import Room
from .models import RoomImage
from amenities.serializers import AmenitiesListSerializer

from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer


class RoomImagesSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='common_size')

    class Meta:
        model = RoomImage
        fields = ('id', 'image')


class RoomListSerializer(serializers.ModelSerializer):
    images = RoomImagesSerializer(many=True, read_only=True)
    room_amenities = AmenitiesListSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'slug', 'price',
                  'description', 'images', 'room_amenities')
