from .common import *

import dj_database_url


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "NAME": os.environ.get("DATABASE_NAME", "svc_maps_django"),
        "USER": os.environ.get("DATABASE_USER", "maps"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "q1w2e3r4"),
    }
}