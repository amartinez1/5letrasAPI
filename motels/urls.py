from django.conf import settings
from django.conf.urls import url
from motels import views

from rest_framework.views import APIView


urlpatterns = [
    url(r'^api/motels/$', views.MotelList.as_view(), name='motel-list'),
    url(r'^api/motels/filters/$', views.MotelListFilters.as_view(), name='motel-filters'),
    url(r'^api/motels/(?P<motels_slug>[\w-]+)/$', views.MotelRetrieve.as_view(), name='motel-retrieve'),
    url(r'^api/comments/$', views.CommentList.as_view(), name='comment-list'),
    url(r'^api/amenities/$', views.AmenitiesList.as_view(), name='ammenities-list'),
]
