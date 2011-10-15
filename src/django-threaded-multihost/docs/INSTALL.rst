Installing Django-Threaded-Multihost
====================================

With threaded_multihost on your PYTHONPATH, just add the Threadlocal middleware to your MIDDLEWARE_CLASSES entry in your "settings.py" file.

For example::

 MIDDLEWARE_CLASSES = (
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
 )
