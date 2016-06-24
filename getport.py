#!/srv/xenim/frontend/venv/bin/python
import os
import sys

from configurations import importer

os.environ["DJANGO_SETTINGS_MODULE"] = "xenim.settings"
os.environ["DJANGO_CONFIGURATION"] = "%sSettings" % sys.argv[1]

importer.install(check_options=True)
from django.conf import settings

print settings.SITE_ID
