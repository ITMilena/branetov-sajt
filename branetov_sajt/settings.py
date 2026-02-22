"""
Django settings for branetov_sajt project.
Django 6.0.1
"""

from pathlib import Path
import os

# -------------------------
# PATHS
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# CORE SECURITY
# -------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-insecure-change-me")
DEBUG = os.getenv("DEBUG", "1") == "1"

# Render host (ako deployuješ)
RENDER_HOST = os.getenv("RENDER_EXTERNAL_HOSTNAME", "")

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
if RENDER_HOST:
    ALLOWED_HOSTS.append(RENDER_HOST)

extra_hosts = os.getenv("DJANGO_ALLOWED_HOSTS", "")
if extra_hosts:
    ALLOWED_HOSTS += [h.strip() for h in extra_hosts.split(",") if h.strip()]

CSRF_TRUSTED_ORIGINS = []
if RENDER_HOST:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_HOST}")

# -------------------------
# APPLICATIONS
# -------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "gradnja",
]

if DEBUG:
    INSTALLED_APPS += ["django_browser_reload"]

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------
# URL / WSGI
# -------------------------
ROOT_URLCONF = "branetov_sajt.urls"
WSGI_APPLICATION = "branetov_sajt.wsgi.application"

# -------------------------
# TEMPLATES
# -------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # tvoj meni (ako ga koristiš)
                "gradnja.context_processors.nav_categories",
            ],
        },
    },
]

# -------------------------
# DATABASE
# -------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------------------------
# PASSWORD VALIDATION
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------
# INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = "sr-latn"
TIME_ZONE = "Europe/Belgrade"
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC FILES (WhiteNoise)
# -------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}

# WhiteNoise dodatne opcije (ne mora, ali je lepo)
WHITENOISE_MAX_AGE = 31536000  # 1 godina cache za verzionisane fajlove

# -------------------------
# MEDIA FILES
# -------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------
# EMAIL (SIGURNO - preko ENV)
# -------------------------
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "1") == "1"

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)

# -------------------------
# PRODUCTION SECURITY (opciono preko ENV)
# -------------------------
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "0") == "1"
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "0") == "1"
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "0") == "1"

# Preporuka za Render kad DEBUG=0:
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# -------------------------
# DEFAULT PRIMARY KEY
# -------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
