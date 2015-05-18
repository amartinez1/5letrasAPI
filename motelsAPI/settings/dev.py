from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'motels_db',
    }
}

ALLOWED_HOSTS = []

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '0-3lhlvovx6&nkau1+dr9npw47@q0*#^48p)t!1b**bla9ejc)'

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

FIXTURE_DIRS = (
   '/motelsAPI/fixtures/',
)
