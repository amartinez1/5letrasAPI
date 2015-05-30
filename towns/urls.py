from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/towns/$', views.TownList.as_view(), name='towns-list'),
    url(r'^api/towns/(?P<towns_slug>[\w-]+)/$',
        views.TownRetrieve.as_view(), name='towns-retrieve')
]
