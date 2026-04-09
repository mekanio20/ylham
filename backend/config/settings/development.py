from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# ─── DATABASE (SQLite - geliştirme için yeterli) ──────────────────────────────

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ─── CORS (geliştirmede tümüne izin ver) ──────────────────────────────────────

CORS_ALLOW_ALL_ORIGINS = True

# ─── DRF (geliştirmede browsable API aktif) ───────────────────────────────────

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

# ─── EMAIL (geliştirmede konsola yaz) ─────────────────────────────────────────

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ylham.goldaw.com.tm@gmail.com'
EMAIL_HOST_PASSWORD = 'tgkc xhjy bkxg hiko'

# ─── DEBUG TOOLBAR (opsiyonel, pip install django-debug-toolbar) ──────────────
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# INTERNAL_IPS = ['127.0.0.1']