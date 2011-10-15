"""A central mechanism for settings with defaults.
"""

from django.conf import settings

threadlocal_settings_defaults = {
    'DEBUG_DOMAIN' : None, # formatted as "dev" or "dev=com", which means to try substituting 'com' for 'dev'
    'AUTO_WWW' : True # try with or without www
}

def add_setting_defaults(newdefaults):
    """
    This method can be used by other applications to define their
    default values.

    newdefaults has to be a dictionary containing name -> value of
    the settings.
    """
    threadlocal_settings_defaults.update(newdefaults)


def set_threadlocal_setting(name, value):
    if not hasattr(settings, 'THREADED_MULTIHOST_SETTINGS'):
        settings.THREADED_MULTIHOST_SETTINGS = {}
    settings.THREADED_MULTIHOST_SETTINGS[name] = value


def get_threadlocal_setting(name, default_value = None):
    if not hasattr(settings, 'THREADED_MULTIHOST_SETTINGS'):
        return threadlocal_settings_defaults.get(name, default_value)

    return settings.THREADED_MULTIHOST_SETTINGS.get(name, threadlocal_settings_defaults.get(name, default_value))

