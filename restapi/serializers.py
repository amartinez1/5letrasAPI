from towns.models import Town
from towns.models import TownImage
from motels.models import Motel
from motels.models import MotelImage
from rooms.models import Room
from rooms.models import RoomImage
from amenities.models import Amenitie
from comments.models import Comment

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer


class AmenitiesListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amenitie
        fields = ('id', 'name', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
          'url': {'lookup_field': 'slug'}
        }


class RoomImagesSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='common_size')

    class Meta:
        model = RoomImage
        fields = ('id', 'image')


class RoomListSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImagesSerializer(many=True, read_only=True)
    room_amenities = AmenitiesListSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'slug', 'price',
                  'description', 'images', 'room_amenities')


class CommentsListSerializer(serializers.HyperlinkedModelSerializer):
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M',
                                             required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'motel', 'body', 'rating',
                  'created_date')


class TownImagesSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='common_size')

    class Meta:
        model = TownImage
        fields = ('id', 'image')


class TownRetrieveSerializer(serializers.ModelSerializer):
    images = TownImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Town
        fields = ('id', 'name', 'slug', 'images')
        lookup_field = 'slug'
        extra_kwargs = {
          'url': {'lookup_field': 'slug'}
        }


class TownListSerializer(serializers.HyperlinkedModelSerializer):
    motel_count = serializers.ReadOnlyField(source="count")

    class Meta:
        model = Town
        fields = ('id', 'name', 'slug',
                  'motel_count', 'point')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }



class MotelImagesSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='common_size')

    class Meta:
        model = MotelImage
        fields = ('id', 'image')


class MotelListSerializer(serializers.HyperlinkedModelSerializer):
    images = MotelImagesSerializer(many=True, read_only=True)
    amenities = AmenitiesListSerializer(many=True, read_only=True)
    rating_percent = serializers.ReadOnlyField(source="get_percent")
    town = TownListSerializer()

    def get_motel_town(self, town):
        queryset = Town.objects.filter(status=True, town=town)
        serializer = TownListSerializer(instance=queryset, many=False)
        return serializer.data

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town', 'price_range',
                  'rating', 'rating_percent', 'images',
                  'address', 'address2', 'email',
                  'telephone', 'website', 'description',
                  'amenities')
        lookup_field = 'motel_slug'
        extra_kwargs = {
          'url': {'lookup_field': 'slug'}
        }


class MotelRetrieveSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField('get_rooms_list')
    images = MotelImagesSerializer(many=True, read_only=False)
    amenities = AmenitiesListSerializer(many=True, read_only=False)
    rating_percent = serializers.ReadOnlyField(source="get_percent")
    town = TownListSerializer()

    def get_rooms_list(self, motel):
        queryset = Room.objects.filter(status=True, motel=motel)
        serializer = RoomListSerializer(instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town','price_range',
                  'rating', 'rating_percent', 'images', 'address',
                  'email', 'telephone', 'website',
                  'description', 'rooms', 'amenities',
                  'get_percent')
