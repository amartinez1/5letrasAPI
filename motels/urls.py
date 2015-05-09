from django.conf.urls import include
from django.conf.urls import url
from motels import views

urlpatterns = [
    url(r'^api/towns/$', views.town_list),
    url(r'^api/motels/$', views.motel_list),
    url(r'^api/motels/(?P<pk>[0-9]+)/$', views.motel_detail),
    url(r'^api/amenities/$', views.amenities_list),
    url(r'^api/comments/$', views.comment_list),
]