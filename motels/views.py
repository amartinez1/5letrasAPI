from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import generics

# from rest_framework.parsers import JSONParser #for Post, UPdate, Delete
# requests
from .models import Comment
from .models import Motel
from .models import Town
from .models import Amenitie
from .serializers import CommentSerializer
from .serializers import MotelSerializer
from .serializers import MotelListSerializer
from .serializers import TownSerializer
from .serializers import AmenitiesSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class TownList(generics.ListAPIView):
    """
    retrieves a list of all Towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer

class MotelList(generics.ListAPIView):
    """
    Retrieves a list of all motels
    """
    queryset = Motel.objects.all()
    serializer_class = MotelSerializer

@csrf_exempt
def motel_detail(request, pk):
    """
    Retireves a motel by its id
    """ 
    try:
        motel = Motel.objects.get(pk=pk)
    except Motel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MotelSerializer(motel)
        return JSONResponse(serializer.data)

class AmenitiesList(generics.ListAPIView):
    """
    Retrieves a list of all amenities
    """
    queryset = Amenitie.objects.all()
    serializer_class = AmenitiesSerializer

class CommentList(generics.ListCreateAPIView):
    """
    Retrieves a list of all Comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
