from django.core.paginator import Paginator

from .models import Motel
from .models import MotelImage
from amenities.models import Amenitie
from comments.models import Comment
from rooms.models import Room
from rooms.serializers import RoomListSerializer
from towns.serializers import TownListSerializer
from amenities.serializers import AmenitiesListSerializer
from comments.serializers import CommentsListSerializer

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
    town = TownListSerializer()

    def get_motel_town(self, town):
        queryset = Town.objects.filter(status=True, town=town)
        serializer = TownListSerializer(instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town',
                  'latitude', 'longitude', 'price_range', 
                  'rating', 'images', 'address', 'address2', 
                  'email', 'telephone', 'website', 
                  'description', 'amenities')


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

class MotelRetrieveSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField('get_rooms_list')
    images = MotelImagesSerializer(many=True, read_only=True)
    amenities = AmenitiesListSerializer(many=True, read_only=True)
    town = TownListSerializer()

    def get_rooms_list(self, motel):
        queryset = Room.objects.filter(status=True, motel=motel)
        serializer = RoomListSerializer(instance=queryset, many=True)
        return serializer.data


    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town', 'latitude', 
                  'longitude', 'price_range', 'rating', 
                  'images', 'address', 'email', 'telephone', 
                  'website', 'description', 'rooms', 'amenities')

