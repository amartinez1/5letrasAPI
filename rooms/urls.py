from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from rooms import views

urlpatterns = [
    url(r'^api/rooms/$', views.RoomList.as_view()),
]
