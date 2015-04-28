from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser #for Post, UPdate, Delete requests 
from .models import Motel
from .serializers import MotelSerializer

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
def motel_list(request):
	"""
	retrieves a list of all motels
	"""
	if request.method == 'GET':
		motels = Motel.objects.all()
		
		serializer = MotelSerializer(motels, many = True)
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