import logging.config

from deployment import phase

class Logging(object):
    def make_logging(self):
        cfg = {
            'version': 1,
            'disable_existing_loggers': True,
            'formatters': self.LOGGING_FORMATTERS,
            'handlers': self.LOGGING_HANDLERS,
            'loggers': self.LOGGING_LOGGERS,
        }
        return logging.config.dictConfig(cfg)

    @property
    def LOGGING_CONFIG(self):
        return self.make_logging

    LOGGING_FORMATTERS = {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    }
    
    @property
    def LOGGING_HANDLERS(self):
        return {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
            'sentry': {
                'level': 'ERROR',
                'class': 'django.utils.log.NullHandler',
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
        }

    @property
    def LOGGING_LOGGERS(self):
        return {
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
