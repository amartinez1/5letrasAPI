from .models import Amenitie
from .models import Comment
from .models import Motel
from .models import MotelImage

from towns.serializers import TownListSerializer
from rooms.serializers import RoomListSerializer

from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

class AmenitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenitie
        fields = ('id', 'name')

class CommentsListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', 
                                             required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'motel', 'body', 'rating', 
                  'created_date')
        ordering = ['id']

class MotelImagesSerializer(serializers.ModelSerializer):
  image = VersatileImageFieldSerializer(sizes='common_size')

  class Meta:
      model = MotelImage
      fields = ('id', 'image')

class MotelListSerializer(serializers.ModelSerializer):
    images = MotelImagesSerializer(many=True, read_only=True)
    amenities = AmenitiesListSerializer(many=True, read_only=True)
    town = TownListSerializer(read_only=True)

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town',
                  'latitude', 'longitude', 'price_range', 
                  'rating', 'images', 'address', 'address2', 
                  'email', 'telephone', 'website', 
                  'description', 'amenities')

class MotelRetrieveSerializer(serializers.ModelSerializer):
    comments = CommentsListSerializer(many=True, read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    images = MotelImagesSerializer(many=True, read_only=True)
    amenities = AmenitiesListSerializer(many=True, read_only=True)
    town = TownListSerializer()

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town', 'latitude', 
                  'longitude', 'price_range', 'rating', 
                  'images', 'address', 'email', 'telephone', 
                  'website', 'description', 'rooms', 'amenities', 
                  'comments')
