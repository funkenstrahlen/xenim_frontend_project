'''
Created on 24.05.2011

@author: robert
'''

import translitcodec
import re

PUNCT_RE = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(value, delim=u'-'):
    """
    Generates an ASCII-only slug.
    
    Borrowed from http://flask.pocoo.org/snippets/5/
    """
    result = []
    for word in PUNCT_RE.split(value.lower()):
        word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))


from settings.deployment import phase

def deployment(request):
    return {'phase': phase}

# inject canonical url into context
def get_canonical(request):
    host = request.get_host()
    if ":" in host:
        host, port = host.split(":", 1)
    else:
        port = None
    if not host.endswith(".de"):
        host = host.split(".")
        host[-1] = "de"
        host = ".".join(host)
    else:
        return { 'is_canonical': True }
    if port:
        host += ":%s" % port
    path = request.get_full_path()
    url = "http://%s%s" % (host, path)

    return {
        'is_canonical': False,
        'canonical': url
    }

from django.views.generic.base import TemplateView
import re

class RedirectView(TemplateView):

    template_name = "redirect.html"

    rmstr = []

    def get_context_data(self, **kwargs):
        context = super(RedirectView, self).get_context_data(**kwargs)
        url = self.request.build_absolute_uri(self.request.get_full_path())
        for pattern, replacement in self.rmstr:
            url = re.sub(pattern, replacement, url)
        context['url'] = url
        return context

