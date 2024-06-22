import os
from pathlib import Path
from easy_thumbnails.conf import Settings as thumbnail_settings

# Set the secret key
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug mode
DEBUG = True
# Allowed hosts
ALLOWED_HOSTS = ['172.20.10.6','https://courseworkrentplushire.netlify.app/','127.0.0.1']

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
    'Cart.apps.CartConfig',
    'oauth2_provider',
    'easy_thumbnails',
    'image_cropping',  # Add 'image_cropping' to your installed apps
]

# Add thumbnail processors to THUMBNAIL_PROCESSORS
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.ApprovalMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Custom middleware added here
]

# Root URL configuration
ROOT_URLCONF = 'myworld.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'templates'),  # Main templates directory
             os.path.join(BASE_DIR, 'Booking', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Cart.context_processors.cart',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'myworld.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'verceldb',  # Replace with your database name
        'USER': 'default',   # Replace with your database username
        'PASSWORD': 'AZ1s4miXNlPB',  # Replace with your database password
        'HOST': 'ep-yellow-salad-a4bnv0ob.us-east-1.aws.neon.tech',  # Replace with your database host
        'PORT': '5432',      # Replace with your database port
        'OPTIONS': {
            'sslmode': 'require',
        },
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
    BASE_DIR / "staticfiles",
]
STATIC_ROOT = str(BASE_DIR / 'productionfiles')

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

# Media root directory where uploaded files will be stored
MEDIA_ROOT = BASE_DIR / 'media'

# Media URL to serve uploaded files
MEDIA_URL = '/media/'



# IMAGE CROPPING Configuration
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}

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

# IMAGE CROPPING Configuration
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}