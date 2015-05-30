import django_filters
from django.shortcuts import get_object_or_404

from rest_framework import filters
from rest_framework import generics

from .models import Motel
from .serializers import MotelListSerializer
from .serializers import MotelRetrieveSerializer


class MotelFilter(django_filters.FilterSet):
    """
    Filter Motel by town, price, amenities, rating
    """
    town = django_filters.CharFilter(name="town__name")
    amenities = django_filters.CharFilter(name="amenities__name")
    min_price = django_filters.NumberFilter(name="price_range",
                                            lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price_range",
                                            lookup_type='lte')

    class Meta:
        model = Motel
        fields = ['town', 'amenities', 'min_price', 'max_price', 'rating']


class MotelList(generics.ListAPIView):
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
    """
    queryset = Motel.objects.filter(status=True, town__status=True)
    serializer_class = MotelListSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,
                       filters.DjangoFilterBackend)
    ordering_fields = ('name', 'town__name', 'amenities__name',
                       'rating', 'price', 'created_date')
    search_fields = ('name', )
    # filter_fields = ('town__name', 'amenities__name', 'rating')
    filter_class = MotelFilter


class MotelRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a motel by its slug
    """
    serializer_class = MotelRetrieveSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = Motel.objects.filter(status=True, town__status=True)
        motel = get_object_or_404(queryset, slug=self.kwargs['motels_slug'])
        return motel
