from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Comment
from .serializers import CommentsListSerializer

from rest_framework import generics

class CommentList(generics.ListCreateAPIView):
    """
    Retrieves a list of all Comments
    """
    queryset = Comment.objects.filter(status=True, motel__status=True, 
                                      motel__town__status=True)
    serializer_class = CommentsListSerializer


class CommentMotelListFilter(generics.ListAPIView):
    """
    Retrieves a motel comments listt by its slug 
    """
    serializer_class = CommentsListSerializer


    def get_queryset(self):
        queryset = Comment.objects.filter(status=True, motel__status=True, 
                                          motel__town__status=True,
                                          motel__slug=self.kwargs['motel_slug'])
        return queryset
