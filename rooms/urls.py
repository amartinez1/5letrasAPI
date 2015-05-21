from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^api/rooms/$', views.RoomList.as_view(), name='rooms-list'),
]
