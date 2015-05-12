from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from towns import views

urlpatterns = [
    url(r'^api/towns/$', views.TownList.as_view())
]