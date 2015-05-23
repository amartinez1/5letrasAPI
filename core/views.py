from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRoot(APIView):
    def get(self, request):
        return Response({
            'motels': reverse('motels-list', request=request),
            'motels-retrieve': reverse('token-auth', request=request),
            'motel_filters': reverse('motels-filters', request=request),
            'comments': reverse('comments-list', request=request),
            'ammenities': reverse('ammenities-list', request=request),
            'rooms': reverse('rooms-list', request=request),
            'towns': reverse('towns-list', request=request),
            'token-auth': reverse('token-auth', request=request),
        })
