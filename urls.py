from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

     (r'^sistema/$', 'opensocialcrm.dashboard.views.index'),
     (r'^sistema/leads/$', 'opensocialcrm.crm.views.index'),
     (r'^sistema/leads/prospeccao/$', 'opensocialcrm.crm.views.prospeccao'),
     (r'^sistema/leads/adicionar/$', 'opensocialcrm.crm.views.adicionar_lead'),
     (r'^sistema/campanhas/$', 'opensocialcrm.campanhas.views.index'),
     (r'^sistema/campanhas/autoriza_linkedin/$', 'opensocialcrm.campanhas.views.autoriza_linkedin'),
     (r'^sistema/campanhas/confirma_linkedin/$', 'opensocialcrm.campanhas.views.confirma_linkedin'),
     (r'^sistema/campanhas/resultados/$', 'opensocialcrm.campanhas.views.resultados'),
     url(r'^$', 'opensocialcrm.index.views.index'),
     (r'^grappelli/', include('grappelli.urls')),
     (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
     (r'^static/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
     url(r'^sistema/painel/', include(admin.site.urls)),
     (r'^i18n/', include('django.conf.urls.i18n')),
     (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

