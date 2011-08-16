from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

     url(r'^campanhas/$', 'socialcrm.campanhas.views.index'),
     url(r'^campanhas/nova/$', 'socialcrm.campanhas.views.nova'),
     url(r'^campanhas/cadastrar_nova/$', 'socialcrm.campanhas.views.cadastrarNova'),
     #url(r'^resultados/', 'crm.resultados.views.index'),
     #url(r'^relacionamentos/', 'crm.relacionamentos.views.index'),
     url(r'^$', 'socialcrm.index.views.index'),
     url(r'^erro_autenticacao/$', 'socialcrm.index.views.erroAutenticacao'),
     (r'^grappelli/', include('grappelli.urls')),
     (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
     (r'^static/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
     url(r'^admin/', include(admin.site.urls)),
)

