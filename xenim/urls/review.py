from django.conf.urls import patterns, url, include
from django.http import HttpResponse

from . import handler500

urlpatterns = patterns('',
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^', include('radioportal_review.urls')),
)

