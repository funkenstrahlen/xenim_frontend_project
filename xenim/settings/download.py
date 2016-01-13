

class Download(object):
    RP_DL_SECRET = "**CHANGEME**"
    RP_DL_PREFIX = "http://archiv.streams.xenim.de/dl/"
    RP_DL_BASEDIR = "/srv/streaming/data/recordings/"

    @property
    def INSTALLED_APPS(self):
        return super(Download, self).INSTALLED_APPS

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Download, self).MIDDLEWARE_CLASSES
