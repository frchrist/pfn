from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = "9)#!m%m67@)^h==e@+b@&_1)qa()gd5*$8klvv(lv8)3z737no"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': environ["DB_NAME"],

        'USER':  environ["DB_USER"],

        'PASSWORD':  environ["DB_PASSWORD"],

        'HOST': environ["DB_HOST"],

        'PORT':  environ["DB_PORT"],

    }}
# settings for security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally. 
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True 
SECURE_HSTS_SECONDS = 86400  # 1 day 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
SECURE_HSTS_PRELOAD = True 
