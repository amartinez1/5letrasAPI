from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/comments/$', views.CommentList.as_view(), name='comments-list'),
    url(r'^api/comments/motel/(?P<motels_slug>[\w-]+)/$', views.CommentRetrieve.as_view(),
    	name='comments-motel-retrieve'),
]
