from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'motels_db',
        'USER': 'admin_motels',
        'PASS': 'motels',
    }
}

ALLOWED_HOSTS = ['*']

SECRET_KEY = get_env_setting('SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR_PATCH_SETTINGS = False
