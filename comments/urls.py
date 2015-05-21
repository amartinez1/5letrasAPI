from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/comments/$', views.CommentList.as_view(), name='comments-list'),
]


