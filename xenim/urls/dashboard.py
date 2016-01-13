from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

from . import handler500
import external_auth.views
from xenim.utils import RedirectView
from django.contrib import admin
admin.autodiscover()

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

#    url(r'^', include('radioportal.urls')),
    # legacy redirect
#    url(r'^dashboard/', RedirectView.as_view(rmstr=[("dashboard/",""),("streams\.","")])),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^archive/', include('radioportal_archive.urls')),
    url(r'^extauth/trust_external/', external_auth.views.trust_external),
    url(r'^extauth/retrieve_groups/', external_auth.views.retrieve_groups),
    url(r'^hijack/', include('hijack.urls')),
    url(r'^', include('radioportal.dashboard.urls')),
)

