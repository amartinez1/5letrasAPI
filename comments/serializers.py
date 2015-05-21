from rest_framework import serializers

from .models import Comment

class CommentsListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', 
                                             required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'motel', 'body', 'rating',
                  'created_date')
