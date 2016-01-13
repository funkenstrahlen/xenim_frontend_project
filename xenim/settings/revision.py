
''' Note: always include the INSTALLED_APPS and MIDDLEWARE_CLASSES functions
          even, if you don't modify this settings
'''


class Revision(object):
    @property
    def INSTALLED_APPS(self):
        return super(Revision, self).INSTALLED_APPS + (
            'reversion',
        )

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Revision, self).MIDDLEWARE_CLASSES + (
            'reversion.middleware.RevisionMiddleware',
        )
