from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from motels import views

urlpatterns = [
    url(r'^api/motels/$', views.MotelList.as_view()),
    url(r'^api/motels/filters/$', views.MotelListFilters.as_view()),
    url(r'^api/motels/(?P<motels_slug>[\w-]+)/$', views.MotelRetrieve.as_view()),
    url(r'^api/comments/$', views.CommentList.as_view()),
    url(r'^api/amenities/$', views.AmenitiesList.as_view()),
]
