import os
from pathlib import Path

from dotenv import load_dotenv
from google.oauth2 import service_account

# NOTE: Loads env Variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = bool(os.getenv("DEBUG"))
if DEBUG is True:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    ENVIRONMENT_NAME = "Development server"
    ENVIRONMENT_COLOR = "#800080"
else:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    ENVIRONMENT_NAME = "Production server"
    ENVIRONMENT_COLOR = "#FF2222"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    os.getenv("SERVER_NAME"),
    os.getenv("DNS_NAME"),
    "0.0.0.0",
]
INSTALLED_APPS = [
    "django_admin_env_notice",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap4",
    "web",
    "portal",
    "employee",
    "announcements",
    "compliance",
    "phonenumber_field",
    "localflavor",
    "minio_storage",
    "google",
    "captcha",
    "corsheaders",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "NettHandsHomeCare.urls"
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "django_admin_env_notice.context_processors.from_settings",
            ],
        },
    },
]
AUTH_USER_MODEL = "employee.Employee"
WSGI_APPLICATION = "NettHandsHomeCare.wsgi.application"
if DEBUG is False:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "DB_Sandbox",
        },
    }
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
STATIC_ROOT = "/staticfiles/"
# STATICFILES_STORAGE = 'NettHandsHomeCare.gcsUtils.Static'
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_ACCESS_KEY = os.getenv("MINIO_STORAGE_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY = os.getenv("MINIO_STORAGE_SECRET_KEY")
MINIO_STORAGE_MEDIA_BUCKET_NAME = "employee-uploads"
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
MINIO_STORAGE_MEDIA_OBJECT_METADATA = {"Cache-Control": "max-age=1000"}
MINIO_STORAGE_ENDPOINT = "localhost:9000"
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BACKUP_BUCKET = "Recycle Bin"
MINIO_STORAGE_MEDIA_BACKUP_FORMAT = "%c/"
MINIO_STORAGE_STATIC_BUCKET_NAME = "local-static"
GS_BUCKET_NAME = os.getenv("GCP_BUCKET")
STATIC_URL = "static/"

MEDIA_URL = "https://console.cloud.google.com/storage/browser/nhhc_cloud_storage/"

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, "credentials.json"),
)
# SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"https://storage.googleapis.com/nhhc_cloud_storage/*",
]
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
DATETIME_FORMAT = "m/d/yyyy h:mm A"
ADMINS = [("Terry Brooks", "Terry@BrooksJr.com"), ("Admin", "admin@netthandshome.care")]
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_SERVER")
EMAIL_USE_TLS = True
EMAIL_PORT = os.getenv("EMAIL_TSL_PORT")
EMAIL_HOST_USER = os.getenv("NOTIFICATION_SENDER_EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_ACCT_PASSWORD")
