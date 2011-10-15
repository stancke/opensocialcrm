from django.conf.urls.defaults import *

custompatterns = patterns('tests.customapp.views',
    (r'^collect_urls/$', 'collect_urls', {}),
    (r'^async_note/$', 'async_note_create')
)

