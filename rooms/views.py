from rest_framework import generics

from .models import Room
from .serializers import RoomListSerializer


class RoomList(generics.ListAPIView):
    """
    Retrieves a list of all motels
    """
    queryset = Room.objects.filter(motel__status=True, status=True)
    serializer_class = RoomListSerializer
