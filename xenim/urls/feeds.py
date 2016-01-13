from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView

from . import handler500

urlpatterns = patterns('',
    url(r'^news/', include('radioportal_news.urls')),
    url(r'^planned/(?P<path>.*)$', RedirectView.as_view(url="/upcoming/%(path)s", permanent=True)),
    url(r'^', include('radioportal.feeds.urls')),
)

