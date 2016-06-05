"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*kf(*ey!_*a3&1(tuk1++b)oq_5q1k%ed)0b3==-+c&62jdgjq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'solo',

    'account',
    'app',
    'pipeline',
    'core',
    'attendance',
    'progress',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.AuthRequiredMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# Database setting stored in app/local_settings.


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Samara'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

PIPELINE_STORAGE = 'pipeline.storage.PipelineFinderStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    # 'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'bower': {
            'source_filenames': (
              'bower_components/bootstrap/dist/css/bootstrap.css',
              'bower_components/bootstrap-select/dist/css/bootstrap-select.css',
              'bower_components/bootstrap-datepicker/dist/css/bootstrap-datepicker.css',
              'bower_components/bootstrap-table/dist/bootstrap-table.css',
              'bower_components/font-awesome/css/font-awesome.css',
              'bower_components/bootstrap-table-fixed-columns/bootstrap-table-fixed-columns.css',
            ),
            'output_filename': 'css/libs.css',
        },
        'custom': {
            'source_filenames': (
              'css/components/**/*.css',
            ),
            'output_filename': 'css/styles.css',
        },
    },
    'JAVASCRIPT': {
        'bower': {
            'source_filenames': (
              'bower_components/jquery/dist/jquery.js',
              'bower_components/bootstrap/dist/js/bootstrap.js',
              'bower_components/bootstrap-select/dist/js/bootstrap-select.js',
              'bower_components/bootstrap-datepicker/dist/js/bootstrap-datepicker.js',
              'bower_components/bootstrap-table/dist/bootstrap-table.js',
              'bower_components/bootstrap-table-fixed-columns/bootstrap-table-fixed-columns.js',
            ),
            'output_filename': 'js/libs.js',
        },
        'custom': {
            'source_filenames': (
              'js/jquery.params.js',
              'js/scripts.min.js',
            ),
            'output_filename': 'js/scripts.min.js',
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
