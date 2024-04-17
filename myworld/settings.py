import os
from pathlib import Path

# Set the secret key
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-a5w#s8w02_887j5(#_0bym8d+&s18ctd&o@-%(kl*kp)b329*d')

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug mode
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = ['127.0.0.1']

# Custom user model
AUTH_USER_MODEL = 'account.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account.apps.AccountConfig',
    'Booking.apps.BookingConfig',
    'oauth2_provider',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.ApprovalMiddleware',  # Custom middleware added here
]

# Root URL configuration
ROOT_URLCONF = 'myworld.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR / 'templates'),  # Convert Path object to string
            str(BASE_DIR / 'account' / 'templates'),  # Convert Path object to string
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

# WSGI application
WSGI_APPLICATION = 'myworld.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators
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

# Language and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(BASE_DIR / 'static'),
]
STATIC_ROOT = str(BASE_DIR / 'staticfiles')

# Custom authentication backends
AUTHENTICATION_BACKENDS = [
    'account.backends.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# OAuth2 Provider Settings
OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups',
    }
}

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server address
EMAIL_PORT = 587  # SMTP server port
EMAIL_USE_TLS = True  # Whether to use TLS (secure connection) for sending emails
EMAIL_HOST_USER = 'hads1kiki@gmail.com'  # SMTP username (your email address)
EMAIL_HOST_PASSWORD = 'jxrt rxfv xrrh fono'  # SMTP password for authentication
EMAIL_SUBJECT_PREFIX = '[MyApp] '  # Email subject prefix (optional)
ADMIN_EMAIL = 'hads1kiki@gmail.com'  # Admin email address (optional)
DEFAULT_FROM_EMAIL = 'hads1kiki@gmail.com'  # Default sender email address (optional)
