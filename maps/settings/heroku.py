from .common import *

import dj_database_url


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get("DATABASE_HOST", "d6q8diwwdmy5c9k9.cbetxkdyhwsb.us-east-1.rds.amazonaws.com"),
        "NAME": os.environ.get("DATABASE_NAME", "ap0wimq3utu9ufv9"),
        "USER": os.environ.get("DATABASE_USER", "jfbuhl798frmfxnb"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "tsu45i1o2yxyolg9"),
    }
}