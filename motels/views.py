from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


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

# Create your views here.


class JSONResponse(HttpResponse):

    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def town_list(request):
    """
    retrieves a list of all motels
    """
    if request.method == 'GET':
        motels = Town.objects.all()
        serializer = TownSerializer(motels, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def motel_list(request):
    """
    retrieves a list of all motels
    """
    if request.method == 'GET':
        motels = Motel.objects.all()
        serializer = MotelListSerializer(motels, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def motel_detail(request, pk):
    """
    retireves a motel by its id
    """ 
    try:
        motel = Motel.objects.get(pk=pk)
    except Motel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MotelSerializer(motel)
        return JSONResponse(serializer.data)

@csrf_exempt
def amenities_list(request):
    """
    retireves a motel by its id
    """ 
    if request.method == 'GET':
        amenitie = Amenitie.objects.all()
        serializer = AmenitiesSerializer(amenitie, many=True)
        return JSONResponse(serializer.data)

@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)