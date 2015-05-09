from .models import Comment
from .models import Motel
from .models import Town
from .models import Amenitie
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', required=False)

    class Meta:
        model = Comment
        fields = ('id', 'motel', 'body', 'ranking', 
                  'created_date')

class MotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town',
                  'latitude', 'longitude', 'ranking',
                  'telephone', 'website', 'description')

class MotelRetrieveSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Motel
        fields = ('id', 'name', 'slug', 'town', 
                  'latitude', 'longitude','ranking',
                  'telephone', 'website','description', 
                  'comments')

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenitie
        fields = ('id', 'name',)

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('id', 'name', 'slug', 'latitude', 'longitude')