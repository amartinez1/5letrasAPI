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
