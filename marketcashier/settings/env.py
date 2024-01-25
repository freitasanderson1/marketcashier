from .base import *

SECRET_KEY = "fk9ml0#a%p$a2os!r1-^ojb=#@kfkj!^gqmwv-pr@4!1rm!@gn"

DEBUG=True

ALLOWED_HOSTS=['localhost','127.0.0.1','0.0.0.0']

CSRF_TRUSTED_ORIGINS = ['http://localhost:1404', 'http://localhost:5432']

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'marketcashier',
    'USER': 'anderson',
    'PASSWORD': 'password123',
    'HOST': 'db',
    'PORT': '5432',
  }
}