
from pathlib import Path
from os import path as p, environ


from django.core.exceptions import ImproperlyConfigured

def get_secret(name, default=None):
    try:
        return environ[name]
    except KeyError:
        if default is None:
            raise ImproperlyConfigured(" environ error ")
        else:
            return default


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'igl%fkjn0!c!9#9p(rb7(f#ou03(giz6alh%daz7*o&c)_tw+m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["pythonfornull.herokuapp.com", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "posting",
    "ckeditor",
    'data',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pythonic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pythonic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#developement databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# postgres://lejroohwikrlkd:40b6c5ec45deb6c9a11864b31eca35250dafedc5cff9be899ee20cc70a01554f@ec2-174-129-199-54.compute-1.amazonaws.com:5432/d1lglnhk5c0t09
# #production database
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'd1lglnhk5c0t09',

        'USER': 'lejroohwikrlkd',

        'PASSWORD': '40b6c5ec45deb6c9a11864b31eca35250dafedc5cff9be899ee20cc70a01554f',

        'HOST': 'ec2-174-129-199-54.compute-1.amazonaws.com',

        'PORT': 5432,

    }

}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = p.join(BASE_DIR, "staticfiles")

MEDIA_URL = '/media/'
MEDIA_ROOT = p.join(BASE_DIR, "media")

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    p.join(BASE_DIR, "static"),
] 


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
        'skin':'moono',
        'toolbar_Basic': 
             [
                 ['CodeSnippet', "Source", "div"],
                 ['div','devtools','TextColor', 'BGColor','Maximize', 'ShowBlocks','Bold', "Table", "Smiley", "HorizontalRule", "Link",'Styles', 'Format', 'Font', 'FontSize' "SpecialChar","Image", "PageBreak", "Iframe", 'Blockquote', 'CreateDiv'],
                  # here
             ],'extraPlugins': ','.join(['codesnippet','div']),
        'width':'auto',
        # "update":['image','update','table','HorizontalRule', 'Smiley', "SpecialChar","CodeSnippet"], 'extraPlugins': 'codesnippet',
    },
    'special': 
        {'toolbar': 'Special', 'height': 500,
         'toolbar_Special': 
             [
                 ['Bold'],
                 ['CodeSnippet'], # here
             ], 'extraPlugins': 'codesnippet', # here
         },
    'extrait': {
        'toolbar': 'Basic',
         'toolbar_Basic': [
             ['BGColor','Bold', "Smiley",'Styles', 'Format', 'Font', 'FontSize' "SpecialChar"]
         ],
        'width':"auto",
        'height': 100,
    },
}

CKEDITOR_UPLOAD_PATH = 'ckeditor/'

LOGIN_URL  ="login"
LOGIN_REDIRECT_URL  = "homepage"
LOGOUT_REDIRECT_URL = "homepage"

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "pythonfornulls@gmail.com"
EMAIL_HOST_PASSWORD = "pythoncode12" #past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'default from email'



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#settings for security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally. 
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True 
SECURE_HSTS_SECONDS = 86400  # 1 day 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
SECURE_HSTS_PRELOAD = True 
