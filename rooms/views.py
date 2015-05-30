from rest_framework import generics

from .models import Room
from .serializers import RoomListSerializer


class RoomList(generics.ListAPIView):
    """
    Retrieves a list of all motels
    """
    queryset = Room.objects.filter(status=True, motel__status=True,
                                   motel__town__status=True)
    serializer_class = RoomListSerializer
