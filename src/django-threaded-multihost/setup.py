import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

version = __import__('threaded_multihost').__version__

setup(
    name = 'django-threaded-multihost',
    version = version,
    description = "Django Threaded Multihost",
    long_description = """django-threaded multihost provides support utilities to
    enable easy multi-site awareness in Django apps.""",
    author = 'Bruce Kroeze',
    author_email = 'brucek@solidsitesolutions.com',
    url = 'http://bitbucket.org/bkroeze/django-threaded-multihost/',
    license = 'New BSD License',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django'],
    packages = ['threaded_multihost'],
    #package_dir = {'':'threaded_multihost'},
    include_package_data = False,
    setup_requires = ["setuptools_hg"],
)
