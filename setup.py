#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test


setup(
    name='django-flatpages-nav',
    version='0.1',
    author='Sumit Chachra',
    author_email='chachra@tivix.com',
    url='http://github.com/tivix/django-flatpages-nav',
    description = 'Manage your Django flatpages much more easily using this app. Adding them to header / footer nav was never easier!',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Django>=1.2.2',
        'South>=0.7.2'
    ],
    # test_suite = 'flatpages_nav.tests',
    include_package_data=True,
    # cmdclass={},
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
