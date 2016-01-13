import os
import raven

from deployment import phase

class Logging(object):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.handlers.SysLogHandler',
                'formatter': 'verbose'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
            }
        },
        'loggers': {
            'django': {
                'handlers': ['null'],
                'propagate': True,
                'level': 'INFO',
            },
            'django.request': {
                'handlers': ['mail_admins', 'sentry'],
                'level': 'ERROR',
                'propagate': False,
            },
            'radioportal': {
                'handlers': ['sentry', 'console', 'mail_admins'],
                'level': 'INFO',
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        }
    }

    SERVER_EMAIL = '**CHANGEME**'
    DEFAULT_FROM_EMAIL = '**CHANGEME**'
    EMAIL_HOST = '**CHANGEME**'
    EMAIL_HOST_USER = '**CHANGEME**'
    EMAIL_HOST_PASSWORD = '**CHANGEME**'
    EMAIL_USE_TLS = True
    # EMAIL_PORT = 465
    EMAIL_SUBJECT_PREFIX = "[xenim%s] " % ("",phase.replace(".",""))[bool(phase)]

    ADMINS = (
        ('Arno Nymous', 'arno@example.com'),
    )

    MANAGERS = ADMINS

    @property
    def INSTALLED_APPS(self):
        return super(Logging, self).INSTALLED_APPS + (
            'raven.contrib.django.raven_compat',
        )

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Logging, self).MIDDLEWARE_CLASSES + (
            'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
        )

    RAVEN_CONFIG = {
        'dsn': '**CHANGEME**',
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': raven.fetch_git_sha(os.path.join(os.path.dirname(__file__), "..", "..")),
    }
