from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class APIRoot(APIView):
    def get(self, request):
        return Response({
            'motel': reverse('motel-list', request=request),
            'motel_filters': reverse('motel-filters', request=request),
            'comment': reverse('comment-list', request=request),
            'ammenities': reverse('ammenities-list', request=request),
            'rooms': reverse('rooms-list', request=request),
            'towns': reverse('town-list', request=request),
        })