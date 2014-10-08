#!/usr/bin/env python
"""Unit tests for SwaggerPython Petstore sample app API client.

Run all tests:

    python BaseApiTest.py

"""

import sys
import os
import unittest
import ConfigParser

sys.path = ['./'] + sys.path

import Airseed
from lib import *

class BaseApiTest(unittest.TestCase):
    # function doesnt follow convention but that's how unittest library is written
    def setUp(self):
        self.config = Configs()
        self.client_id = self.config.get('client_id')
        self.client_secret = self.config.get('client_secret')

        airseed = Airseed.Airseed(self.client_id, self.client_secret)

        self.user_api = UserApi.UserApi(airseed)
        self.oauth =  OAuth.OAuth(airseed, self.config.get('oauth_callback_url'))

class Configs:

    def __init__(self):
        self.conf_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.conf_file)

    def get(self, key):
        return self.config.get('test', key)

    def set(self, key, val):
        self.config.set('test', key, val)
        self.config.write(open(self.conf_file, 'w'))

    def items(self):
        return self.config.items('test')

if __name__ == "__main__":

    from UserApiTest import UserApiTest

    unittest.main()
