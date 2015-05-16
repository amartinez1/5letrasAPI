import django_filters
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import filters

from .models import Amenitie
from .models import Comment
from .models import Motel
from .serializers import AmenitiesListSerializer
from .serializers import CommentsListSerializer
from .serializers import MotelListSerializer
from .serializers import MotelRetrieveSerializer

class MotelFilter(django_filters.FilterSet):
    """
    Filter Motel by town, price, amenities, rating
    """
    town = django_filters.CharFilter(name="town__name")
    amenities = django_filters.CharFilter(name="amenities__name")
    min_price = django_filters.NumberFilter(name="price_range", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price_range", lookup_type='lte')

    class Meta:
        model = Motel
        fields = ['town', 'amenities', 'min_price', 'max_price', 'rating']

class MotelList(generics.ListAPIView):
    """
    #Retrieves a list of all motels
    ---
    #### 1. Filters Values
        - Filters by town, amenities, min_price, max_price and rating
        - example: ?town=Guaynabo, ?amenities=wifi, ?rating=5
    #####Link example: [?town=Guaynabo](?town=Guaynabo)
    ---
    #### 2. Ordering Values
        - Ordering by name, town__name, amenities__name, rating, price
        - example: ?ordering=name
    #####Link example: [?ordering=name](?ordering=name)
    ---
    #### 3. Search Values
        - Search keyword starting with motel name
        - example: ?search=MotelName   
    #####Link example: [?search=test](?search=test)
    """
    queryset = Motel.objects.filter(status=True)
    serializer_class = MotelListSerializer
    filter_class = MotelFilter
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ('name', 'town__name', 'amenities__name', 'rating', 'price')
    search_fields = ('^name', )

class MotelRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a motel by its slug 
    """
    serializer_class = MotelRetrieveSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = Motel.objects.filter(status=True, comments__status=True)
        motel = get_object_or_404(queryset, slug=self.kwargs['motels_slug'])
        return motel

class AmenitiesList(generics.ListAPIView):
    """
    Retrieves a list of all amenities
    """
    queryset = Amenitie.objects.all()
    serializer_class = AmenitiesListSerializer

class CommentList(generics.ListCreateAPIView):
    """
    Retrieves a list of all Comments
    """
    queryset = Comment.objects.filter(motel__status=True, status=True)
    serializer_class = CommentsListSerializer
