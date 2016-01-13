
''' Note: always include the INSTALLED_APPS and MIDDLEWARE_CLASSES functions
          even, if you don't modify this settings
'''


class Example(object):
    @property
    def INSTALLED_APPS(self):
        return super(Example, self).INSTALLED_APPS + (
            'radioportal_example',
        )

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Example, self).MIDDLEWARE_CLASSES

    EXAMPLE_SETTING = "some value"
    EXAMPLE_SECRET = "**CHANGEME**"
