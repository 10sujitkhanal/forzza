import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '=)h--nymd2&at*v$2$jf87q0&*o%tw9gzxgul(kr%$c4=k4q3)'
SITE_ID = 1
DEBUG = True
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

ALLOWED_HOSTS = ['ancient-beyond-85603.herokuapp.com','127.0.0.1','*','192.168.16.108']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'accounts',
    'userprofile',
	'notifications',
    'core',
    'deposit',
    'withdraw',
    'crispy_forms',
    'django_cleanup',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'message',
    'admin.common',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'accounts.LoginCheckMiddleWare.LoginCheckMiddleWare'

]

ROOT_URLCONF = 'forzzanepal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
                'django.template.context_processors.i18n',
		'forzzanepal.context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'forzzanepal.wsgi.application'
ASGI_APPLICATION = "forzzanepal.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'forzzanepal.sqlite3'),
    }
}


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'socialnetwork',
#         'USER': 'root',
#         'PASSWORD': 'sujit',
#         'HOST': 'localhost',   
#         'PORT': '3306',
#     }    
# }
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'fi'

LANGUAGES = (
    ('en-us', _('English')),
    ('ne', _('Nepali')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

LOGIN_REDIRECT_URL = 'deposit:deposit'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = "accounts.User"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MESSAGES_TO_LOAD = 15
SOCIAL_AUTH_FACEBOOK_KEY = '847761292690566'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '4d7acd49ac1e1a2f122b4f8d98850996'  # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '521498671369-ojvc70sknflinl7brvfgjfhca0if3mp7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '6WApggYNVYScUGzMink4297a'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

DJANGO_NOTIFICATIONS_CONFIG = { 'USE_JSONFIELD': True}
