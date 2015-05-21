from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Comment
from .serializers import CommentsListSerializer

from rest_framework import generics

class CommentList(generics.ListCreateAPIView):
    """
    Retrieves a list of all Comments
    """
    queryset = Comment.objects.filter(motel__status=True, status=True)
    serializer_class = CommentsListSerializer


class CommentRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a Town by its slug 
    """
    serializer_class = CommentsListSerializer


    def get_object(self):
        queryset = Comment.objects.filter(motel__status=True, status=True)
        comment = get_object_or_404(queryset, slug=self.kwargs['comments_id'])
        return comment
