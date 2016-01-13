from django.conf.urls import patterns, url
from django.views.generic.base import View

urlpatterns = patterns('',
    url(r'^$', View.as_view(), name="landing"),
    url(r'^(?P<page>[\w-]+)$', View.as_view(), name="wiki-page"),
    url(r'^(?P<category>[\w-]+)/(?P<page>[\w-]+)$', View.as_view(), name="wiki-category-page"),
)

