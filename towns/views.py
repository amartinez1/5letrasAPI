from django.shortcuts import get_object_or_404

from rest_framework import generics

from .models import Town
from .serializers import TownListExtraInfoSerializer
from .serializers import TownListSerializer


class TownList(generics.ListAPIView):
    """
    Retrieves a list of all Towns
    ---
    ### More Town Information
    > The API can give you additional information for the Town
      (latitude, longitude, images and motel counts)
      if you add the parameter extra_info=true

    - ####Example:
        *  #####Parameter extra_info: [?extra_info=true](?extra_info=true)
    """
    queryset = Town.objects.filter(status=True)
    paginate_by = 0

    def get_serializer_class(self):
        if self.request.GET.get('extra_info') == 'true':
            return TownListExtraInfoSerializer
        return TownListSerializer


class TownRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a Town by its slug
    """
    serializer_class = TownListExtraInfoSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = Town.objects.get(status=True)
        town = get_object_or_404(queryset, slug=self.kwargs['towns_slug'])
        return town
