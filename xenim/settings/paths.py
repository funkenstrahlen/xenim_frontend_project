
import os

from deployment import phase

class Paths(object):
    PROJECT_DIR = os.path.dirname(__file__)
    PROJECT_DIR = os.path.normpath(os.path.join(PROJECT_DIR, ".."))

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/"
    MEDIA_ROOT = "/srv/www/de/xenim/streams/media/html/"

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash if there is a path component (optional in other cases).
    # Examples: "http://media.lawrence.com", "http://example.com/media/"
    STATIC_URL = "//static.streams.%sxenim.de/" % phase

    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )

#    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(PROJECT_DIR, 'templates'),
    )

    MEDIA_URL = '//media.streams.%sxenim.de/' % phase

    STATIC_ROOT = "/srv/www/de/xenim/streams/static/html/"

    LOCALE_PATHS = (
        os.path.join(PROJECT_DIR, 'locale'),
    )

    # ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

    @property
    def INSTALLED_APPS(self):
        return super(Paths, self).INSTALLED_APPS

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Paths, self).MIDDLEWARE_CLASSES
