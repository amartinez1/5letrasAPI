from django.shortcuts import get_object_or_404

from rest_framework import generics

from .models import Town
from .serializers import TownListSerializer


class TownList(generics.ListCreateAPIView):
    """
    Retrieves a list of all Towns
    """
    queryset = Town.objects.all()
    serializer_class = TownListSerializer
    paginate_by = 100


class TownRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a Town by its slug 
    """
    serializer_class = TownListSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = Town.objects.all()
        town = get_object_or_404(queryset, slug=self.kwargs['towns_slug'])
        return town
