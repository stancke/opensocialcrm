from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^cache/', include('keyedcache.urls')),
    (r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    (r'^admin/', include(admin.site.urls)),
)
