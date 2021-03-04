# encoding: utf-8
"""
Auth0 backend.
"""

import logging
from django.conf import settings
from social_core.backends.oauth import BaseOAuth2

__version__ = '0.1.2'

__author__ = 'Takashi NAGAI'


class Auth0OAuth2(BaseOAuth2):
    """
    Auth0 backend
    """
    name = "oa2-auth0"

    REDIRECT_STATE = False
    AUTHORIZATION_URL = 'https://{domain}/authorize'
    ACCESS_TOKEN_URL = 'https://{domain}/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    REVOKE_TOKEN_URL = 'https://{domain}/logout'
    REVOKE_TOKEN_METHOD = 'GET'
    USER_DATA_URL = 'https://{domain}/userinfo'

    def _get_base_uri(self):
        return settings.FEATURES.get('AUTH0_DOMAIN', u'auth0.com')

    def authorization_url(self):
        return self.AUTHORIZATION_URL.format(domain=self._get_base_uri())

    def access_token_url(self):
        return self.ACCESS_TOKEN_URL.format(domain=self._get_base_uri())

    def revoke_token_url(self, token, uid):
        return self.REVOKE_TOKEN_URL.format(domain=self._get_base_uri())

    def get_user_details(self, response):
        """Return user details from Auth0 account"""
        fullname, first_name, last_name = self.get_user_names(
            response.get('name', u''),
            response.get('first_name', u''),
            response.get('last_name', u'')
        )
        return {'username': response.get('nickname', response.get('name')),
                'email': response.get('email', u''),
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name,
                }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from Auth0"""
        params = dict()
        params['access_token'] = access_token
        return self.get_json(self.USER_DATA_URL.format(domain=self._get_base_uri()), params=params)

    def get_user_id(self, details, response):
        """ Get the permanent ID for this user from Auth0. """
        return response.get('sub', u'')
