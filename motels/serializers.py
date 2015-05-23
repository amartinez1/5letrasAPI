from django.core.paginator import Paginator

from .models import Motel
from .models import MotelImage
from amenities.models import Amenitie
from rooms.models import Room
from rooms.serializers import RoomListSerializer
from towns.serializers import TownListSerializer
from amenities.serializers import AmenitiesListSerializer

from rest_framework import pagination
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


class MotelImagesSerializer(serializers.ModelSerializer):
  image = VersatileImageFieldSerializer(sizes='common_size')

  class Meta:
      model = MotelImage
      fields = ('id', 'image')


class MotelListSerializer(serializers.ModelSerializer):
    images = MotelImagesSerializer(many=True, read_only=True)
    amenities = AmenitiesListSerializer(many=True, read_only=True)
    rating_percent = serializers.ReadOnlyField(source="get_percent")
    town = TownListSerializer()


    def get_motel_town(self, town):
        queryset = Town.objects.filter(status=True, town=town)
        serializer = TownListSerializer(instance=queryset, many=True)
        return serializer.data


    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town',
                  'latitude', 'longitude', 'price_range',
                  'rating', 'rating_percent', 'images',
                  'address', 'address2', 'email',
                  'telephone', 'website', 'description',
                  'amenities')


class MotelRetrieveSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField('get_rooms_list')
    images = MotelImagesSerializer(many=True, read_only=True)
    amenities = AmenitiesListSerializer(many=True, read_only=True)
    rating_percent = serializers.ReadOnlyField(source="get_percent")
    town = TownListSerializer()

    def get_rooms_list(self, motel):
        queryset = Room.objects.filter(status=True, motel=motel)
        serializer = RoomListSerializer(instance=queryset, many=True)
        return serializer.data


    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town', 'latitude', 
                  'longitude', 'price_range', 'rating',
                  'rating_percent', 'images', 'address', 
                  'email', 'telephone', 'website', 
                  'description', 'rooms', 'amenities',
                  'get_percent')

