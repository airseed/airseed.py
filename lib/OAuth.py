#!/usr/bin/env python
"""
Copyright 2014 Airseed, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""
import sys
import os
import urllib
import random

import Airseed

AUTH_BASE_URL = "https://auth.airseed.com"

class OAuth:
    """Airseed Auth client"""


    def __init__(self, airseed, callback_url = None):
        self.client = airseed.client
        self.callback_url = callback_url


    def login(self, provider):
        params = {
            'client_id': self.client.client_id,
            'redirect_uri': self.callback_url,
            'response_type': 'code',
            'state': self._state(),
            'provider': provider
        }

        query_params = {}
        # Need to remove None values, these should not be sent
        for param, value in params.items():
            if value != None:
                query_params[param] = self.client.to_path_value(value)

        url = self._request_url("/oauth/authenticate")
        url = str(url) + '?' + str(urllib.urlencode(query_params))

        return url


    def handle_callback(self, params):
        if not params['state'] == _state:
            raise Client.APIError('csrf_detected', 'CSRF detected')

        if params['code']:
            self.state = None
            return access_token(params['code'])


    def access_token(self, code):
        params = {
            'client_id': self.client.client_id,
            'client_secret': self.client.client_secret,
            'redirect_uri': self.callback_url,
            'code': code,
            'grant_type': 'authorization_code'
        }

        return self.client.request(self._request_url('/oauth/token'), 'POST', params)


    def refresh_token(self, refresh_token):
        params = {
            'client_id': self.client.client_id,
            'client_secret': self.client.client_secret,
            'redirect_uri': self.callback_url,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }

        return self.client.request(self._request_url('/oauth/token'), 'POST', params)


    def _state(self):
        if not(hasattr(self, 'state')) or self.state is None:
            self.state = '%024x' % random.randrange(16**24)
        return self.state


    def _request_url(self, path):
        return str(AUTH_BASE_URL) + str(path)

