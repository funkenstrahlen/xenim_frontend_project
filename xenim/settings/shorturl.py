

class ShortURLs(object):
    @property
    def INSTALLED_APPS(self):
        return super(ShortURLs, self).INSTALLED_APPS + (
            'shorturls',
            'extshorturls',
        )

    SHORTEN_MODELS = {
        's': 'radioportal.show',
        'e': 'radioportal.episode',
        'a': 'radioportal.stream',
        '-': 'extshorturls.externalshorturl',
    }

    SHORT_BASE_URL = "http://xsn.io/"

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(ShortURLs, self).MIDDLEWARE_CLASSES
