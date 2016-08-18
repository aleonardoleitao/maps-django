import os


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "zqx_83=qe#ddf8%0no+a*#4rt#5$*4kw5%i2bck*gn@w3@f&-&"

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition.

INSTALLED_APPS = (
    # Django apps.
    "django_admin_bootstrapped",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps.
    "django_extensions",
    "django_object_actions",

    # Local apps.
    "localidades.app",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
)

ROOT_URLCONF = "localidades.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "localidades.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "NAME": os.environ.get("DATABASE_NAME", "svc_maps_django"),
        "USER": os.environ.get("DATABASE_USER", "root"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

STATIC_URL = "/static/"

STATIC_ROOT = "staticfiles"


# Media files (user-uploaded files)

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")