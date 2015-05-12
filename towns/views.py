from django.shortcuts import render

from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from .models import Town
from .serializers import TownSerializer

class TownList(generics.ListAPIView):
    """
    Retrieves a list of all Towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer