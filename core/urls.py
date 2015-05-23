from django.conf import settings
from django.conf.urls import url
from .views import APIRoot
from rest_framework.authtoken import views


urlpatterns = [
	url(r'^api/$', APIRoot.as_view()),
	url(r'^api/token-auth/', views.obtain_auth_token, name='token-auth'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
]
