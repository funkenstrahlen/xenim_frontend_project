import os
import raven

class SentryCfg(object):
    @property
    def LOGGING_HANDLERS(self):
        HANDLERS = super(SentryCfg, self).LOGGING_HANDLERS
        HANDLERS['sentry'] = {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        }
        return HANDLERS

    @property
    def LOGGING_LOGGERS(self):
        loggers = super(SentryCfg, self).LOGGING_LOGGERS
        loggers.update({
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            }
        })
        return loggers

    @property
    def INSTALLED_APPS(self):
        return super(SentryCfg, self).INSTALLED_APPS + (
            'raven.contrib.django.raven_compat',
        )

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(SentryCfg, self).MIDDLEWARE_CLASSES + (
            'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
        )

    RAVEN_CONFIG = {
        'dsn': '**CHANGEME**',
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': raven.fetch_git_sha(os.path.join(os.path.dirname(__file__), "..", "..")),
    }
