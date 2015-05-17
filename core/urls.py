from django.conf import settings
from django.conf.urls import url
from core import views

urlpatterns = [
	url(r'^api/$', views.APIRoot.as_view()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
]
