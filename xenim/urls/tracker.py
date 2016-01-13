from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.generic.base import View

urlpatterns = patterns('',
    url(r'^Ticket/Display.html\?id=(?P<id>\d+)$', View.as_view(), name="ticket-detail"),
)

