
''' Note: always include the INSTALLED_APPS and MIDDLEWARE_CLASSES functions
          even, if you don't modify this settings
'''


class Tastypie(object):
    @property
    def INSTALLED_APPS(self):
        return super(Tastypie, self).INSTALLED_APPS + (
            'tastypie',
        )

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Tastypie, self).MIDDLEWARE_CLASSES

