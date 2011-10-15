# Django settings for signals_ahoy test
import logging
import os, os.path

DIRNAME = os.path.dirname(__file__)

DJANGO_PROJECT = 'tests'
DJANGO_SETTINGS_MODULE = 'tests.settings'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('', ''),
)

MANAGERS = ADMINS

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
gettext_noop = lambda s:s

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
   ('en', gettext_noop('English')),
)

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#Image files will be stored off of this path
MEDIA_ROOT = os.path.join(DIRNAME, 'static/')
#MEDIA_ROOT = "/static"
# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
#MEDIA_URL = 'site_media'
MEDIA_URL="/static/"
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.auth',)

ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'signals_ahoy',
    'localsite',
    'customapp',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SITE_NAME = "tests"

# "simple" doesn't have any custom templates, usually you'd have one here for your site.
TEMPLATE_DIRS = (
    os.path.join(DIRNAME, "templates"),
)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(DIRNAME, 'tests.db')
SECRET_KEY = 'EXAMPLE SECRET KEY'

##### For Email ########
# If this isn't set in your settings file, you can set these here
#EMAIL_HOST = 'host here'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'your user here'
#EMAIL_HOST_PASSWORD = 'your password'
#EMAIL_USE_TLS = True

#These are used when loading the test data
SITE_DOMAIN = "localhost"
SITE_NAME = "Signals Ahoy tests"

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
CACHE_BACKEND = "locmem:///"
CACHE_TIMEOUT = 60*5
CACHE_PREFIX = "Z"

#Configure logging
LOGFILE = "tests.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
logging.info("Tests Started")
