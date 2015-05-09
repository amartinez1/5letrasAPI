from django.conf.urls import include
from django.conf.urls import url
from motels import views

urlpatterns = [
    url(r'^api/towns/$', views.TownList.as_view()),
    url(r'^api/motels/$', views.MotelList.as_view()),
    url(r'^api/motels/(?P<pk>[0-9]+)/$', views.MotelRetrieve.as_view()),
    url(r'^api/comments/$', views.CommentList.as_view()),
    url(r'^api/amenities/$', views.AmenitiesList.as_view()),
]