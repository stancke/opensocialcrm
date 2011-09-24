from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os
from django.contrib import admin
from resultados.views import index

admin.autodiscover()

urlpatterns = patterns('',

     (r'^sistema/$', 'opensocialcrm.dashboard.views.index'),
     (r'^sistema/resultados/$', 'opensocialcrm.resultados.views.index'),
     (r'^sistema/leads/$', 'opensocialcrm.crm.views.index'),
     url(r'^$', 'opensocialcrm.index.views.index'),
     (r'^grappelli/', include('grappelli.urls')),
     (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
     (r'^static/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
     url(r'^sistema/painel/', include(admin.site.urls)),
     (r'^i18n/', include('django.conf.urls.i18n')),
     (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

