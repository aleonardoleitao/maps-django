from .common import *


INSTALLED_APPS += (
#    "debug_toolbar",
)

STATIC_ROOT = os.environ.get("STATIC_ROOT", "/mnt/projetos/")

STATIC_URL = os.environ.get("STATIC_URL", "/staticfiles/")


MEDIA_ROOT = os.environ.get("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))

MEDIA_URL = os.environ.get("MEDIA_URL", "/mediafiles/")

