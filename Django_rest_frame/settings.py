"""
Django settings for Django_rest_frame project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1o#o&h2&qpj-(6#)i7)8r9&x^%p!x)c&wh9v(r-z9bhtwmnsnt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin' ,
    'django.contrib.auth' ,
    'django.contrib.contenttypes' ,
    'django.contrib.sessions' ,
    'django.contrib.messages' ,
    'django.contrib.staticfiles' ,
    'django_celery_results' ,
    'Celeries' ,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware' ,
    'django.contrib.sessions.middleware.SessionMiddleware' ,
    'django.middleware.common.CommonMiddleware' ,
    'django.middleware.csrf.CsrfViewMiddleware' ,
    'django.contrib.auth.middleware.AuthenticationMiddleware' ,
    'django.contrib.messages.middleware.MessageMiddleware' ,
    'django.middleware.clickjacking.XFrameOptionsMiddleware' ,
]

ROOT_URLCONF = 'Django_rest_frame.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates' ,
        'DIRS': [os.path.join(BASE_DIR , 'templates')]
        ,
        'APP_DIRS': True ,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug' ,
                'django.template.context_processors.request' ,
                'django.contrib.auth.context_processors.auth' ,
                'django.contrib.messages.context_processors.messages' ,
            ] ,
        } ,
    } ,
]

WSGI_APPLICATION = 'Django_rest_frame.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3' ,
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3') ,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' ,
    } ,
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' ,
    } ,
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' ,
    } ,
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' ,
    } ,
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

CELERY_BROKER_URL = 'redis://localhost:6379/1'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'kira_luang@163.com'
EMAIL_HOST_PASSWORD = 'SGYZWVFANOTTXAQF'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# EMAIL_USE_SSL=True
