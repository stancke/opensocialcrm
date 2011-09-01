from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

     (r'^resultados/(?P<url>\w+)/$', 'opensocialcrm.resultados.views.index'),
     url(r'^$', 'opensocialcrm.index.views.index'),
     (r'^grappelli/', include('grappelli.urls')),
     (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
     (r'^static/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
     url(r'^sistema/', include(admin.site.urls)),
     (r'^i18n/', include('django.conf.urls.i18n')),
)

