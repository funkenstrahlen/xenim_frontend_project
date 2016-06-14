from configurations import Settings

try:
    from amqp_local import Amqp
except ImportError:
    from amqp import Amqp

try:
    from social_local import Social
except ImportError:
    from social import Social

try:
    from base_local import Base
except ImportError:
    from base import Base

try:
    from database_ro_local import ReadOnlyDatabase
except ImportError:
    from database_ro import ReadOnlyDatabase

try:
    from database_rw_local import ReadWriteDatabase
except ImportError:
    from database_rw import ReadWriteDatabase

try:
    from debugtoolbar_local import DebugToolBar
except ImportError:
    from debugtoolbar import DebugToolBar

try:
    from download_local import Download
except ImportError:
    from download import Download

try:
    from logging_cfg_local import Logging
except ImportError:
    from logging_cfg import Logging

try:
    from sentry_local import SentryCfg
except ImportError:
    from sentry import SentryCfg

try:
    from paths_local import Paths
except ImportError:
    from paths import Paths

try:
    from shorturl_local import ShortURLs
except ImportError:
    from shorturl import ShortURLs

try:
    from revision_local import Revision
except ImportError:
    from revision import Revision

try:
    from review_local import ReviewSett
except ImportError:
    from review import ReviewSett

try:
    from tastypie_local import Tastypie
except ImportError:
    from tastypie import Tastypie

# Configuration is splitted up in several classes, which acts as "mixins" to form the final config.
# See example.py and example_local.py for a hint on how this classes look like

from deployment import phase

class DashboardSettingsBase(Social, Tastypie, Revision, ReadWriteDatabase, Download, Logging, Paths, ShortURLs, Base, Settings):

    @property
    def INSTALLED_APPS(self):
        return super(DashboardSettingsBase, self).INSTALLED_APPS + (
            #'radioportal_control',
            'radioportal_archive',
            'radioportal_news',
            'django_extensions',
            'external_auth',
            'markitup',
        )

    MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
    MARKITUP_SET = 'markitup/sets/markdown'
    # MARKITUP_SKIN = 'markitup/skins/markitup'

    DEFAULT_HOST = 'dashboard'

    ROOT_URLCONF = 'xenim.urls.dashboard'

    MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})

    DEBUG = False
    TEMPLATE_DEBUG = False

    SITE_ID = 6

    ALLOWED_HOSTS = ["dashboard.%sxenim.de" % phase,]


class WWWSettingsBase(ReadOnlyDatabase, Logging, Paths, ShortURLs, Base, Settings):

    DEFAULT_HOST = 'www'

    ROOT_URLCONF = 'xenim.urls.www'

    DEBUG = False
    TEMPLATE_DEBUG = False

    @property
    def INSTALLED_APPS(self):
        return super(WWWSettingsBase, self).INSTALLED_APPS + (
            'radioportal_news',
            'django_markup',
        )

    SITE_ID = 1

    AMQP = False

    ALLOWED_HOSTS = ["streams.%sxenim.de" % phase, "*"]

class FeedsSettingsBase(ReadOnlyDatabase, Logging, Paths, ShortURLs, Base, Settings):

    AMQP = False

    DEFAULT_HOST = 'feeds'

    ROOT_URLCONF = 'xenim.urls.feeds'

    DEBUG = False
    TEMPLATE_DEBUG = False

    API_LIMIT_PER_PAGE = 0

    TASTYPIE_DEFAULT_FORMATS = ['json',]
    HOST_SCHEME = 'http://'
    MEDIA_URL = 'http://media.streams.%sxenim.de/' % phase

    @property
    def INSTALLED_APPS(self):
        return super(FeedsSettingsBase, self).INSTALLED_APPS + (
            'tastypie',
            'django_extensions',
        )

    SITE_ID = 5

    ALLOWED_HOSTS = ["feeds.streams.%sxenim.de" % phase,]

class ReviewSettingsBase(Tastypie, ReviewSett, ReadWriteDatabase, Logging, Paths, ShortURLs, Base, Settings):

    AMQP = False

    DEFAULT_HOST = 'review'

    ROOT_URLCONF = 'xenim.urls.review'

    DEBUG = True
    TEMPLATE_DEBUG = True

    LOGIN_URL = 'https://dashboard.xenim.de/accounts/login/'

    REVIEW_RECEIVER = 'info@streams.xenim.de'
    REVIEW_MAILINGLIST = 'stream-orga@streams.xenim.de'
    REVIEW_MAILINGLIST_SENDER = 'noreply@streams.xenim.de'

    @property
    def INSTALLED_APPS(self):
        return super(ReviewSettingsBase, self).INSTALLED_APPS + (
            'django_markup',
            'markitup',
        )


    SITE_ID = 7

    ALLOWED_HOSTS = ["review.streams.%sxenim.de" % phase,]

    JQUERY_URL = 'jquery-1.6.2.min.js'
    MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
    MARKITUP_SET = 'markitup/sets/markdown'
    # MARKITUP_SKIN = 'markitup/skins/markitup'


class ShorturlSettingsBase(ReadOnlyDatabase, Logging, Paths, ShortURLs, Base, Settings):

    DEFAULT_HOST = 'shorturl'
    ROOT_URLCONF = 'xenim.urls.shorturl'

    DEBUG = False
    TEMPLATE_DEBUG = False

    AMQP = False

    SITE_ID = 4

    ALLOWED_HOSTS = ["%sxenim.de" % phase, "%sxsn.io" % phase, "%sxn--m-6na.de" % phase]


class ProdSettingsMixin(SentryCfg, Amqp, object):
    pass


class DevSettingsMixin(object):
    DEBUG = True
    TEMPLATE_DEBUG = True

    MEDIA_URL = "/media/"
    STATIC_URL = "/static/"

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    AMQP = False

    ROOT_HOSTCONF = 'xenim.hosts_dev'

    INTERNAL_IPS = ('127.0.0.1',)

    ALLOWED_HOSTS = ['*',]

    SESSION_COOKIE_DOMAIN = ''

class DevDashboardSettings(DevSettingsMixin, DebugToolBar, DashboardSettingsBase):
    pass

class DevWWWSettings(DevSettingsMixin, WWWSettingsBase):
    pass

class DevFeedsSettings(DevSettingsMixin, FeedsSettingsBase):
    pass

class DevReviewSettings(DevSettingsMixin, ReviewSettingsBase):
    pass

class DevShorturlSettings(DevSettingsMixin, ShorturlSettingsBase):
    pass


class DashboardSettings(ProdSettingsMixin, DashboardSettingsBase):
    pass

class WWWSettings(ProdSettingsMixin, WWWSettingsBase):
    pass

class FeedsSettings(ProdSettingsMixin, FeedsSettingsBase):
    pass

class ReviewSettings(ProdSettingsMixin, ReviewSettingsBase):
    pass

class ShorturlSettings(ProdSettingsMixin, ShorturlSettingsBase):
    pass
