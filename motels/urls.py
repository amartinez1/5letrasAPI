from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/motels/$', views.MotelList.as_view(), name='motels-list'),
    url(r'^api/motels/filters/$', views.MotelListFilters.as_view(), name='motels-filters'),
    url(r'^api/motels/(?P<motels_slug>[\w-]+)/$', views.MotelRetrieve.as_view(), name='motels-retrieve'),
]
