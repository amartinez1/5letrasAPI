from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^', include('core.urls', namespace="core")),
    url(r'^api/', include('restapi.urls', namespace="rest-api")),
]
