from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'127.0.0.1:8002', 'xenim.urls.feeds', name="feeds", scheme="http://"),
    host(r'127.0.0.1:8003', 'xenim.urls.review', name="review", scheme="http://"),
    host(r'127.0.0.1:8001', 'xenim.urls.dashboard', name="dashboard", scheme="http://"),
    host(r'127.0.0.1:8000', 'xenim.urls.www', name="www", scheme="http://"),
    host(r'127.0.0.1:8004', 'xenim.urls.shorturl', name="shorturl", scheme="http://"),
)
