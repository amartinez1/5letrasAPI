from django.conf.urls import include, url
from motels import views

urlpatterns = [
    url(r'^api/motels/$',views.motel_list),
    url(r'^api/motels/(?P<pk>[0-9]+)/$', views.motel_detail),
]