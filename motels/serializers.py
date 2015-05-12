from .models import Amenitie
from .models import Comment
from .models import Motel
from .models import MotelImage
from .models import Town
from .models import TownImage

from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer


class TownImagesSerializer(serializers.ModelSerializer):
  image = VersatileImageFieldSerializer(sizes='common_size')

  class Meta:
      model = TownImage
      fields = ('id', 'image')

class TownSerializer(serializers.ModelSerializer):
    images = TownImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Town
        fields = ('id', 'name', 'slug', 'latitude', 
                  'longitude', 'images')

class CommentSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', required=False)

    class Meta:
        model = Comment
        fields = ('id', 'motel', 'body', 'ranking', 
                  'created_date')
        ordering = ['id']

class MotelImagesSerializer(serializers.ModelSerializer):
  image = VersatileImageFieldSerializer(sizes='common_size')

  class Meta:
      model = MotelImage
      fields = ('id', 'image')

class MotelListSerializer(serializers.ModelSerializer):
    images = MotelImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town',
                  'latitude', 'longitude', 'number_of_rooms',
                  'price_range', 'ranking', 'images', 'address', 'address2',
                  'email', 'telephone', 'website', 'description')

class MotelRetrieveSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    images = MotelImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town',
                  'latitude', 'longitude', 'number_of_rooms',
                  'price_range', 'ranking', 'images', 'address',
                  'email', 'telephone', 'website', 'description', 
                  'comments')

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenitie
        fields = ('id', 'name')