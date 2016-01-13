from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

from . import FaviconRedirectView, handler500

urlpatterns = patterns('')

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
        }),
    )
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'^favicon.ico$', FaviconRedirectView.as_view()),
    url(r'^apple-touch-icon-precomposed.png$', FaviconRedirectView.as_view()),
    url(r'^apple-touch-icon.png$', FaviconRedirectView.as_view()),
    url(r'^archiv/(?P<path>.*)$', RedirectView.as_view(url="/%(path)s", permanent=True)),
    url(r'^planned/(?P<path>.*)$', RedirectView.as_view(url="/upcoming/%(path)s", permanent=True)),
    url(r'^(blog|tag|dyn|kategorie|page)/(?P<path>.*)$', RedirectView.as_view(url="/", permanent=True)),
    url(r'^news/', include('radioportal_news.urls')),
    url(r'^', include('radioportal.urls')),
)

