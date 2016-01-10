from django.shortcuts import get_object_or_404

from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework_gis.filters import DistanceToPointFilter

from motels.models import Motel
from towns.models import Town
from rooms.models import Room
from amenities.models import Amenitie
from comments.models import Comment
from .serializers import MotelListSerializer
from .serializers import MotelRetrieveSerializer
from .serializers import TownRetrieveSerializer
from .serializers import TownListSerializer
from .serializers import RoomListSerializer
from .serializers import AmenitiesListSerializer
from .serializers import CommentsListSerializer
from .filters import MotelFilter


class MotelsViewSet(ReadOnlyModelViewSet):
    """
    #Retrieves a list of all motels
    ---
    ### 1. Search Values
    > Search by motel name keyword

    - ####Example:
        *  #####Search by Motel Name: [?search=MotelName](?search=MotelName)
    ---
    ### 2. Ordering Values
    > Order by name, town name, amenities name, rating and price

    - ####Examples:
        *  #####Ordering by name: [?ordering=name](?ordering=name)
        *  #####Ordering by town: [?ordering=town__name](?ordering=town__name)
        *  #####Ordering by amenities: [?ordering=amenities__name](?ordering=amenities__name)
        *  #####Ordering by rating: [?ordering=rating](?ordering=rating)
        *  #####Ordering by price: [?ordering=price](?ordering=price)
        *  #####Ordering by price: [?ordering=created_date](?ordering=created_date)

    The API may also specify reverse orderings by prefixing the field name
    with '-', like so:

        - http://example.com/api/motels?ordering=-name

    Multiple orderings may also be specified:

        - http://example.com/api/motels?ordering=name,town__name
    ---
    ###3. Filters Values
    > Filters by town, amenities, min_price, max_price and rating.

    - ####Examples:
        *  #####Filter by town: [?town=Guaynabo](?town=Guaynabo)
        *  #####Filter by amenities: [?amenities=Wifi](?amenities=Wifi)
        *  #####Filter by rating: [?rating=5](?rating=5)
        *  #####Filter by rating: [?min_price=5](?min_price=5)
        *  #####Filter by rating: [?max_price=15](?max_price=15)
    ---
    ###4. Filters By Distance
    > Filters by dist (distance in meters) and point (latitude and longitude).

    - ####Examples:
        *  #####Filter by distance: [?dist=10&point=-122.4862,37.7694&format=json](?dist=10&point=-122.4862,37.7694&format=json)
    ---
    """
    queryset = Motel.objects.filter(status=True, town__status=True)
    serializer_class = MotelListSerializer
    distance_filter_field = 'point'
    bbox_filter_include_overlapping = True # Optional
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,
                       filters.DjangoFilterBackend, DistanceToPointFilter)
    ordering_fields = ('name', 'town__name', 'amenities__name',
                       'rating', 'price', 'created_date')
    search_fields = ('name', )
    filter_class = MotelFilter
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        motel = get_object_or_404(Motel.objects.filter(status=True, town__status=True),
            slug=slug)
        serializer = MotelRetrieveSerializer(motel,
            context={'request': request})
        return Response(serializer.data)


class TownViewSet(ReadOnlyModelViewSet):
    """
    Retrieves a list of all Towns
    ---
    ###1. More Town Information
    > The API can give you additional information for the Town
      (latitude, longitude, images and motel counts)
      if you add the parameter extra_info=true

    - ####Example:
        *  #####Parameter extra_info: [?extra_info=true](?extra_info=true)
    ###2. Filters By Distance
    > Filters by dist (distance in meters) and point (latitude and longitude).

    - ####Examples:
        *  #####Filter by distance: [?dist=10&point=-122.4862,37.7694&format=json](?dist=10&point=-122.4862,37.7694&format=json)
    ---
    """
    queryset = Town.objects.filter(status=True)
    serializer_class = TownListSerializer
    distance_filter_field = 'point'
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True # Optional
    page_size = 0
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        town = get_object_or_404(Town.objects.filter(status=True),
            slug=slug)
        serializer = TownRetrieveSerializer(town)
        return Response(serializer.data)


class RoomViewSet(ReadOnlyModelViewSet):
    """
    Retrieves a list of all motels
    """
    queryset = Room.objects.filter(status=True, motel__status=True,
                                   motel__town__status=True)
    serializer_class = RoomListSerializer
    lookup_field = 'slug'


class AmenitiesViewSet(ReadOnlyModelViewSet):
    """
    Retrieves a list of all amenities
    """
    queryset = Amenitie.objects.all()
    serializer_class = AmenitiesListSerializer
    paginate_by = 0
    lookup_field = 'slug'


class CommentsViewSet(ReadOnlyModelViewSet):
    """
    Retrieves a list of all Comments
    """
    queryset = Comment.objects.filter(status=True, motel__status=True,
                                      motel__town__status=True)
    serializer_class = CommentsListSerializer
