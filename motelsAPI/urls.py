from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'motelsAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls')),
    url(r'^', include('motels.urls')),
    url(r'^', include('towns.urls')),
]
