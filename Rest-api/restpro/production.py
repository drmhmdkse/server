def database():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'databasepostgresql',
            'USER': 'databasepostgresql_user',
            'PASSWORD': 'databasepostgresql_password',
            'HOST': 'databasepostgresql',
            'PORT': '5432'
        }
    }
    return DATABASES


def staticroot(os, basedir):
    STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(basedir)), 'opt/services/djangoapp/static')
    return STATIC_ROOT


def mediaroot(os,basedir):
    MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(basedir)), 'opt/services/djangoapp/media')
    return MEDIA_ROOT
