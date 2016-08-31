"""
WSGI config for highlightsapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/mnt/projetos/maps-django')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "localidades.settings.producao")

application = get_wsgi_application()

try:
    from dj_static import Cling
    application = Cling(application)
except:
    pass
