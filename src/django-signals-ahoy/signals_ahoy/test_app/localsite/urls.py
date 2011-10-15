from django.conf.urls.defaults import *
from signals_ahoy import signals
import localsite

urlpatterns = patterns('tests.localsite.views',
    (r'example/', 'example', {}),
    (r'^search/$', 'search', {}),
    (r'^sigview/$', 'signalled_view', {}),
    (r'^form/$', 'form_example', {}),
    (r'^$', 'index', {}, 'test_index')
)

signals.collect_urls.send(sender=localsite, patterns=urlpatterns)
