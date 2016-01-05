#!/usr/bin/env python
"""
sentry-auth-neptulon
==================

:copyright: (c) 2015 GetSentry LLC
"""
from setuptools import setup, find_packages


tests_require = [
    'pytest',
    'mock',
]

install_requires = [
]

setup(
    name='sentry-auth-neptulon',
    version='0.1.0',
    author='CMGS',
    author_email='ilskdw@gmail.com',
    url='https://www.neptulon.com',
    description='Neptulon authentication provider for Sentry',
    long_description=__doc__,
    license='',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'auth_neptulon = sentry_auth_neptulon',
         ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
