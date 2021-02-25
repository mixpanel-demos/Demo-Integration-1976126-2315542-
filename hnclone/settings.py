"""
Django settings for hnclone project.

Generated by 'django-admin startproject' using Django 2.2.5.

Modified by me 2019-09-30 15.50 CEST

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Package deps with the repo to make installation quicker on repl.it
EXTERNALS = os.path.join(BASE_DIR, "..", "externals")
sys.path = ["", EXTERNALS] + sys.path

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TODO' # TODO

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


USE_X_FORWARDED_HOST = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'mptt',
    'debug_toolbar',

    'accounts',
    'news',
    'emaildigest',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.gzip.GZipMiddleware',
    #'htmlmin.middleware.HtmlMinifyMiddleware', # TODO: When activated, Django Debug Toolbar has JS issues
    'htmlmin.middleware.MarkRequestMiddleware',
    'hnclone.middleware.mixpanel_middleware',
]

ROOT_URLCONF = 'hnclone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hnclone.context_processors.settings_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'hnclone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


AUTH_USER_MODEL = 'accounts.CustomUser'


INTERNAL_IPS = [
    '127.0.0.1',
]


PAGING_SIZE = 30


HTML_MINIFY = True



LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'



ACCEPT_UNINVITED_REGISTRATIONS = True


SITE_NAME = 'Data News'
SITE_URL = 'https://news.mixpanel.com'
SITE_DOMAIN = 'news.mixpanel.com'

X_FRAME_OPTIONS = '*'

MIXPANEL_PROJECT_TOKEN = 'test_token'
MIXPANEL_PROJECT_ID = 'test_id'
MIXPANEL_ADMIN_USERNAME = '<MIXPANEL_ADMIN_USERNAME>'
MIXPANEL_ADMIN_PASSWORD = '<MIXPANEL_ADMIN_PASSWORD>'
