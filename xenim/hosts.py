from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'tracker.streams.xenim', 'xenim.urls.tracker', name="rt", scheme="https://"),
    host(r'wiki.xenim.de', 'xenim.urls.wiki', name="wiki", scheme="https://"),
)

try:
    from hosts_local import host_patterns as main_pattern
except ImportError:
    from settings.deployment import phase

    main_pattern = patterns('',
        host(r'feeds.streams.%sxenim.de' % phase, 'xenim.urls.feeds', name="feeds", scheme="http://"),
        host(r'review.streams.%sxenim.de' % phase, 'xenim.urls.review', name="review", scheme="https://"),
        host(r'dashboard.%sxenim.de' % phase, 'xenim.urls.dashboard', name="dashboard", scheme="https://"),
        host(r'streams.%sxenim.de' % phase, 'xenim.urls.www', name="www"),
        host(r'%sxsn.io' % phase, 'xenim.urls.shorturl', name="shorturl"),
    )

host_patterns += main_pattern
