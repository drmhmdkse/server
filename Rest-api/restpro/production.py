import os
from dotenv import load_dotenv
load_dotenv()
def database():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
        }
    }
    return DATABASES


def staticroot(os, basedir):
    STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(basedir)), 'opt/services/djangoapp/static')
    return STATIC_ROOT


def mediaroot(os,basedir):
    MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(basedir)), 'opt/services/djangoapp/media')
    return MEDIA_ROOT
