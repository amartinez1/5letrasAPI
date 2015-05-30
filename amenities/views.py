from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics

from .models import Amenitie
from .serializers import AmenitiesListSerializer


class AmenitiesList(generics.ListAPIView):
    """
    Retrieves a list of all amenities
    """
    queryset = Amenitie.objects.all()
    serializer_class = AmenitiesListSerializer
    paginate_by = 0


class AmenitiesRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a motel by its slug
    """
    serializer_class = AmenitiesListSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = Amenitie.objects.filter()
        amenities = get_object_or_404(queryset,
                                      slug=self.kwargs['amenities_slug'])
        return amenities
