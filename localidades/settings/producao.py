from .common import *

import dj_database_url


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = os.environ.get("STATIC_ROOT", "/mnt/projetos/static/")
MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "/mnt/projetos/media")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "NAME": os.environ.get("DATABASE_NAME", "svc_maps_django"),
        "USER": os.environ.get("DATABASE_USER", "maps"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "q1w2e3r4"),
    }
}