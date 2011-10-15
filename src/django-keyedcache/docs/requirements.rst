Requirements
============

You must add a "CACHE_PREFIX = 'whatever'" to your settings.py file.  This allows you to avoid collisions when running more than one site with the same backend.

(optional) If you want to use the threaded first-level cache, you need to install `threaded_multihost`_.

.. _`threaded_multihost`: http://bitbucket.org/bkroeze/django-threaded-multihost/