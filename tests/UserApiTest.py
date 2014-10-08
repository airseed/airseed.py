#!/usr/bin/env python
import sys
import unittest

from BaseApiTest import BaseApiTest

sys.path = ['./'] + sys.path

class UserApiTest(BaseApiTest):

    def test_get_user_by_id(self):
        user = self.user_api.get_user_by_id('me', bearer_token=self.config.get('access_token'))

        assert user['email'] == 'airseed.test@gmail.com', 'email matches user'
        assert user['first_name'] == 'Airseed', 'first_name matches user'
        assert user['last_name'] == 'Test', 'last_name matches user'

    def test_get_data_for_user(self):
        endpoints = [
            'products', 'products/apparel', 'travel', 'travel/flights',
        ]

        for endpoint in endpoints:
            users_data = self.user_api.get_data_for_user('me', bearer_token=self.config.get('access_token'), category=endpoint)
            assert all (k in users_data for k in ("_links","_embedded")), 'has _links and _embedded'
            assert all (k in users_data['_links'] for k in ("self","next")), 'has self and next'
            # assert all (k in users_data['_embedded'] for k in ("data")), 'has data'


if __name__ == "__main__":
    unittest.main()
