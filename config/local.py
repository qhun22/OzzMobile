# Cấu hình môi trường phát triển (Development)
from .base import *

# Debug mode - hiển thị lỗi chi tiết
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database - SQLite cho development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email - Console backend (in ra terminal)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Caching - Dummy cache cho development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Static files - Serve trực tiếp trong development
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Ghi đè INSTALLED_APPS để loại bỏ debug_toolbar (optional)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'django_cleanup',
    'storages',
    # Local apps
    'apps.core',
    'apps.home',
    'apps.accounts',
    'apps.products',
    'apps.cart',
    'apps.orders',
    'apps.reviews',
    'apps.promotions',
    'apps.payments',
    'apps.admin_dashboard',
]
