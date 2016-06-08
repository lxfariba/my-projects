import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, MIDDLEWARE_CLASSES
from django.utils.translation import ugettext_lazy as _


gettext_noop = lambda s: s


DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Tehran'
USE_TZ = True
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
      ('fa' ,_('Persian')),
      ('en' ,_('English')),
)
USE_I18N = True


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALE_PATHS = (
    os.path.join(BASE_DIR, '..', 'locale'),
)

USE_L10N = True

#SERVER_EMAIL = 'mail@abc.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'university_db'),
    }
}


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'university',
    'registration',
    'manager',
    'student',
)


TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

SECRET_KEY = 'a9f7ye4jjp1c-in9a@sf&l=j7c!0@!@!q0%9_=qv&2w#_3411s'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

WSGI_APPLICATION = 'university.wsgi.application'

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'university.urls'

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
            ],
        },
    },
]


AVATAR_ROOT = os.path.join(MEDIA_ROOT,'avatars/')
AVATAR_PATH ='avatars/'