def database(basedir):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': basedir / 'db.sqlite3',
        }
    }
    return DATABASES