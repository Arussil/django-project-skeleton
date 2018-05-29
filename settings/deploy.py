import os

from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += [] 
