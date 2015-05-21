from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/amenities/$', views.AmenitiesList.as_view(), name='ammenities-list'),
    url(r'^api/amenities/(?P<amenities_slug>[\w-]+)/$', views.AmenitiesList.as_view(), name='ammenities-retrieve'),
]
