from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = get_secret('SECRET_KEY', "")

ALLOWED_HOSTS = ["pythonull.herokuapp.com"]

DATABASES["default"] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'