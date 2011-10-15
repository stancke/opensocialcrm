from setuptools import setup, find_packages

version = __import__('signals_ahoy').__version__

setup(
    name = 'django-signals-ahoy',
    version = version,
    description = "signals-ahoy",
    long_description = """Django Signals Ahoy provides very useful common signals for larger Django applications.""",
    author = 'Bruce Kroeze',
    author_email = 'brucek@ecomsmith.com',
    url = 'http://bitbucket.org/bkroeze/django-signals-ahoy/',
    license = 'New BSD License',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django'],
    packages = find_packages(),
    include_package_data = True,
)
