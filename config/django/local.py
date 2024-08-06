from .base import *
from config.env import env


SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=True)

# Host
ALLOWED_HOSTS = ['localhost', 'crmtiw.studioslabs.com', 'www.crmtiw.studioslabs.com', 'crm-test.studioslabs.com', 'www.crm-test.studioslabs.com']
CSRF_TRUSTED_ORIGINS = ['https://crmtiw.studioslabs.com', 'http://crmtiw.studioslabs.com', 'https://crm-test.studioslabs.com', 'http://crm-test.studioslabs.com']

LANGUAGE_CODE = 'pl'

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'config/db/db.sqlite3',
    },

    'cloudfl_db': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': env('DATABASE_NAME'),
        'CLOUDFLARE_DATABASE_ID': env('DATABASE_ID'),
        'CLOUDFLARE_ACCOUNT_ID': env('DATABASE_ACCOUNT'),
        'CLOUDFLARE_TOKEN': env('DATABASE_TOKEN'),
    }
}

DATABASE_ROUTERS = ['config.settings.routers.CloudAppRouter',]

# Cloudflare
# RECAPTCHA_PUBLIC_KEY = env('')
# RECAPTCHA_PRIVATE_KEY = env('')

# Google
RECAPTCHA_PUBLIC_KEY = env('PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('PRIVATE_KEY')