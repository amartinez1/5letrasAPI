from .models import Room
from .models import RoomImage
from motels.models import Amenitie

from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

class AmenitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenitie
        fields = ('id', 'name')

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
        fields = ('id', 'name', 'slug',
                  'price', 'description','images',
                  'room_amenities')
