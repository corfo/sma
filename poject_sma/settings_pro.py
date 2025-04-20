from poject_sma.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("PGDATABASE"),
        'USER': os.environ.get("PGUSER"),
        'PASSWORD': os.environ.get("PGPASSWORD"),
        'HOST': os.environ.get("PGHOST"),
        'PORT': os.environ.get("PGPORT"),
        'OPTIONS':{ 'sslmode':'require'},
        'DISABLE_SERVER_SIDE_CURSORS':True,
    }
}
