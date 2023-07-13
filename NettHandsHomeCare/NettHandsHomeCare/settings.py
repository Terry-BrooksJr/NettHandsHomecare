import os
from pathlib import Path
from google.oauth2 import service_account
from dotenv import load_dotenv

# NOTE: Loads env Variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
if DEBUG is True:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "nett-hands-site-and-portal.onrender.com",
    "www.netthandshome.care",
]
INSTALLED_APPS = [
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
    "phonenumber_field",
    "localflavor",
    "minio_storage",
    "google",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"
MIDDLEWARE = [
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
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
AUTH_USER_MODEL = "portal.Employee"
WSGI_APPLICATION = "NettHandsHomeCare.wsgi.application"
DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.environ.get("DB_NAME"),
    #     "USER": os.environ.get("DB_USER"),
    #     "PASSWORD": os.environ.get("DB_PASSWORD"),
    #     "HOST": os.environ.get("DB_HOST"),
    #     "PORT": os.environ.get("DB_PORT"),
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "offline-db",
    },
    # },
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
STATIC_URL = '/static/'
STATIC_ROOT = './static_files/'
# STATIC_ROOT = f"{BASE_DIR}/staticfiles"
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_ACCESS_KEY = os.getenv("MINIO_STORAGE_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY = os.getenv("MINIO_STORAGE_SECRET_KEY")
MINIO_STORAGE_MEDIA_BUCKET_NAME = "employee-uploads"
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
MINIO_STORAGE_MEDIA_OBJECT_METADATA = {"Cache-Control": "max-age=1000"}
MINIO_STORAGE_ENDPOINT = "localhost:9000"
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BACKUP_BUCKET = 'Recycle Bin'
MINIO_STORAGE_MEDIA_BACKUP_FORMAT = '%c/'
MINIO_STORAGE_STATIC_BUCKET_NAME = 'local-static'
GS_BUCKET_NAME = os.getenv("GCP_BUCKET")
    
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    
MEDIA_URL = "https://console.cloud.google.com/storage/browser/nhhc_cloud_storage"

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, "credentials.json")
)
