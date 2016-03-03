"""
WSGI config for taskproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

#Allows us to see useful stuff in Gunicorn output
sys.stdout = sys.stderr

#Rely upon env var 'DYNO` to determine if we are
#running within Heroku
if 'DYNO' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskproject.settings_heroku")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskproject.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)