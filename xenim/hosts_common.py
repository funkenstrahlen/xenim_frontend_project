from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'tracker.streams.xenim', 'xenim.urls.tracker', name="rt", scheme="https://"),
    host(r'wiki.xenim.de', 'xenim.urls.wiki', name="wiki", scheme="https://"),
)
