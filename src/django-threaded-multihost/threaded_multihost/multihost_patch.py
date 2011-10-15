from django.contrib.sites.models import SiteManager
from threaded_multihost import sites
import logging

log = logging.getLogger('threaded_multihost')

def site_get_current(self):
    """Overridden version of get_current, which is multihost aware."""
    return sites.by_host()

SiteManager.get_current = site_get_current
SiteManager.MULTIHOST = True
log.debug('Patched Django for multihost awareness.')
