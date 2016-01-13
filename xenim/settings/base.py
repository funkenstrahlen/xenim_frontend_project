
from deployment import phase

class Base(object):
    # Django settings for frontend project.

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # On Unix systems, a value of None will cause Django to use the same
    # timezone as the operating system.
    # If running in a Windows environment this must be set to the same as your
    # system time zone.
    TIME_ZONE = 'Europe/Berlin'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'de-de'

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale
    USE_L10N = True

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', list(TEMPLATE_LOADERS)),
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        'django.core.context_processors.static',
        "django.core.context_processors.request",
        "xenim.utils.get_canonical",
        "xenim.utils.deployment",
        "radioportal.context_processors.get_current_path",
        "radioportal.context_processors.get_jquery_url",
    )

    # This is the path to jQuery you want to use.
    # It can be used in templates using {{ jquery_url }}
    # The template variable already includes prepended static file path, if applicable.
    JQUERY_URL = 'js/jquery/jquery-1.11.3.min.js'

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Base, self).MIDDLEWARE_CLASSES + (
            'django_hosts.middleware.HostsRequestMiddleware',
            # 'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            # 'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
            'django_hosts.middleware.HostsResponseMiddleware',
        )

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',  # this is default
        'guardian.backends.ObjectPermissionBackend',
    )

    @property
    def INSTALLED_APPS(self):
        return super(Base, self).INSTALLED_APPS + (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.admin',
            'django.contrib.staticfiles',
            'django.contrib.flatpages',
            'django_hosts',
            'radioportal',
            'autoslug',
            'guardian',
            'easy_thumbnails',
            'polymorphic',
            'hijack',
            'compat',
        )

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

    AUTH_PROFILE_MODULE = 'radioportal.UserProfile'
    LOGIN_REDIRECT_URL = '/'
    LOGIN_URL = 'login'
    LOGOUT_URL = 'logout'

    SESSION_COOKIE_DOMAIN = '.%sxenim.de' % phase

    WSGI_APPLICATION = 'xenim.wsgi.application'

    # App specific settings

    # django-hosts
    ROOT_HOSTCONF = 'xenim.hosts'
    DEFAULT_HOST = 'xenim.www'

    # django-autoslug
    AUTOSLUG_SLUGIFY_FUNCTION = 'xenim.utils.slugify'

    # guardian
    ANONYMOUS_USER_ID = -1

    REALM = "xenim"

    LOGIN_REDIRECT_WHITELIST = ('streams.%sxenim.de' % phase,'review.streams.xenim.de','wiki.xenim.de')

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    USE_X_FORWARDED_HOST = True
