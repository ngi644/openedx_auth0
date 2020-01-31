# encoding: utf-8

"""
Auth0 for OEDX
"""

from setuptools import setup, find_packages

from openedx_auth0.auth0 import __version__

__author__ = 'nagai'


setup(
    name='openedx_auth0',
    description='User authentication of Open edX using Auth0',
    author='Takashi Nagai',
    author_email='ngi644@gmail.com',
    url='',
    version=__version__,
    license='GPL-3.0',
    keywords=['openedx', 'auth0'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-social-auth',
        'social-auth-app-django'
    ],
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
