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