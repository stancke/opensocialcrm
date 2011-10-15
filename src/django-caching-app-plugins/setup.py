from setuptools import setup, find_packages

setup(
    name='django-caching-app-plugins',
    version='0.1.2',
    description='',
    author='Bruce Kroeze',
    author_email='bruce@ecomsmith.com',
    url='http://bitbucket.org/bkroeze/django-caching-app-plugins',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['setuptools_hg'],
)
