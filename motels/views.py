import django_filters
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework import filters

from .models import Amenitie
from .models import Comment
from .models import Motel
from .serializers import AmenitiesListSerializer
from .serializers import CommentsListSerializer
from .serializers import MotelListSerializer
from .serializers import MotelRetrieveSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

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
    Retrieves a list of all motels
    """
    queryset = Motel.objects.filter(status=True, comments__status=True)
    serializer_class = MotelListSerializer
    filter_class = MotelFilter
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ('name', 'town__name', 'amenities__name', 'rating', 'price')
    search_fields = ('^name', )

class MotelRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a motel by its id 
    """
    queryset = Motel.objects.filter(status=True, comments__status=True)
    serializer_class = MotelRetrieveSerializer

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
