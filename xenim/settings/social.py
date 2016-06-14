

class Social(object):
    @property
    def INSTALLED_APPS(self):
        return super(Social, self).INSTALLED_APPS

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Social, self).MIDDLEWARE_CLASSES

    AUPHONIC_CLIENT_ID = "**CHANGEME**"
    AUPHONIC_CLIENT_SECRET = "**CHANGEME**"

    TWITTER_ACCOUNT_TOKEN = "**CHANGEME**"
    TWITTER_ACCOUNT_SECRET = "**CHANGEME**"

    TWITTER_CONSUMER_KEY = "**CHANGEME**"
    TWITTER_CONSUMER_SECRET = "**CHANGEME**"

    PUSH_URL = ()
    PUSH_APPLICATION_ID = "**CHANGEME**"
    PUSH_MASTER_KEY = "**CHANGEME**"
