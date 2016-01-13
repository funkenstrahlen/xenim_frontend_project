from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django_hosts.resolvers import reverse_lazy

from . import handler500

class MountRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = reverse_lazy(host='www', viewname='mount', kwargs={'stream': kwargs["stream"]})
        return url


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy(host='www', viewname='root'), permanent=True)),
    url(r'^(?P<stream>.*\.(mp3|ogg|ogm|nsv|aac|m3u8))$', MountRedirectView.as_view(permanent=True)),
    url(r'^', include('shorturls.urls')),
    url(r'^', include('extshorturls.urls')),
)
