


def custom_show_toolbar(request):
    #return request.META['REMOTE_ADDR'] in DebugToolBar.INTERNAL_IPS
    return True # Always show toolbar, for example purposes only.

class DebugToolBar(object):

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(DebugToolBar, self).MIDDLEWARE_CLASSES + (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

    @property
    def INSTALLED_APPS(self):
        return super(DebugToolBar, self).INSTALLED_APPS + (
            'debug_toolbar',
        )

    INTERNAL_IPS = ()

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': True,
        'SHOW_TOOLBAR_CALLBACK': 'xenim.settings.debugtoolbar.custom_show_toolbar',
        'ENABLE_STACKTRACES': True,
    }
