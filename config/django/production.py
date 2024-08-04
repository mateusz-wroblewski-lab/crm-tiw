from .base import *
from config.env import env

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DATABASES = {
    'default': {
        'ENGINE': 'django_d1',
        'NAME': env('CF_DB_NAME'),
        'CLOUDFLARE_DATABASE_ID': env('CF_DB_ID'),
        'CLOUDFLARE_ACCOUNT_ID': env('CF_ACC_ID'),
        'CLOUDFLARE_TOKEN': env('CF_TOKEN'),
    }
}

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
