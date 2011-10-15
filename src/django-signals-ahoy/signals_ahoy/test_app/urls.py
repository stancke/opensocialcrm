from django.conf.urls.defaults import *
from django.contrib import admin
import logging
log = logging.getLogger('satchmo_store.urls')

# discover all admin modules - if you override this for your
# own base URLs, you'll need to autodiscover there.
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include('tests.localsite.urls'))
)
