#!/usr/bin/env python
import sys
import os
import unittest
import urlparse

from BaseApiTest import BaseApiTest

sys.path = ['./'] + sys.path

class OauthTest(BaseApiTest):

    def test_login(self):
        provider = 'google_oauth2'
        login = self.oauth.login(provider)
        params = urlparse.parse_qs(urlparse.urlparse(login).query)

        assert login != "", 'login should exist'
        assert 'client_id' in params, 'client_id exists in params'
        assert 'provider' in params, 'provider exists in params'
        assert 'state' in params, 'state exists in params'

    def test_refresh_token(self):
        response = self.oauth.refresh_token(self.config.get('refresh_token'))
        assert 'access_token' in response, 'access_token exists in response'
        assert 'expires_in' in response, 'expires_in exists in response'

        if response['access_token'] != self.config.get('access_token'):
            self.config.set('access_token', response['access_token'])

if __name__ == "__main__":
    unittest.main()
