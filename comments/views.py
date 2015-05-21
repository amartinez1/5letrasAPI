from django.shortcuts import render

from .models import Comment
from .serializers import CommentsListSerializer

from rest_framework import generics

class CommentList(generics.ListCreateAPIView):
    """
    Retrieves a list of all Comments
    """
    queryset = Comment.objects.filter(motel__status=True, status=True)
    serializer_class = CommentsListSerializer