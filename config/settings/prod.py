from config.settings.base import *
from .base import *
import os

SECRET_KEY = os.environ.get("PROD_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('HUR_DB_NAME'),
        'USER': os.environ.get('HUR_USER'),
        'PASSWORD': os.environ.get('HUR_DB_PASS'),
        'HOST': os.environ.get('HUR_HOST'),
        'PORT': '5432',
    },
}
