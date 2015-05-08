from .models import Comment
from .models import Motel
from .models import Town
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
        fields = ('id', 'name', 'town', 'latitude', 
                  'longitude', 'ranking', 'telephone', 
                  'website', 'description')

class MotelSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Motel
        fields = ('id', 'name', 'town', 'latitude', 
                  'longitude','ranking','telephone', 
                  'website','description', 'comments')

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('name', 'latitude', 'longitude')