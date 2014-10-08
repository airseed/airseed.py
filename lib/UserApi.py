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

import Airseed

API_BASE_URL = "https://api.airseed.com"

class UserApi:

    def __init__(self, airseed):
        self.client = airseed.client


    def get_all_users(self, **kwargs):
        """List users

        Args:
            limit, int: Number of users returned (optional)

            offset, int: The offset of the first user returned (optional)

        Returns:
        """

        all_params = ['limit', 'offset']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_all_users" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        return self.client.request(self._request_url(resource_path), method, params)


    def get_user_by_email(self, email, **kwargs):
        """Get the corresponding user's profile information with their email.

        Args:
            email, str: target user's email address (required)

        Returns:
        """

        all_params = ['email', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_user_by_email" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/find'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        return self.client.request(self._request_url(resource_path), method, params)


    def get_user_by_id(self, id, **kwargs):
        """Retrieve info about a user, identified by user id

        Args:
            id, str: User ID (required)

        Returns:
        """

        all_params = ['id', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_user_by_id" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/{id}'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        if ('id' in params):
            replacement = str(self.client.to_path_value(params.pop('id')))
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)

        return self.client.request(self._request_url(resource_path), method, params)


    def get_all_contacts_for_user(self, id, **kwargs):
        """Fetch a user's contact list

        Args:
            id, str: User ID (required)

            limit, int: Number of contacts returned (optional)

            offset, int: The offset of the first contact returned (optional)

        Returns:
        """

        all_params = ['id', 'limit', 'offset', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_all_contacts_for_user" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/{id}/contacts'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        if ('id' in params):
            replacement = str(self.client.to_path_value(params.pop('id')))
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)

        return self.client.request(self._request_url(resource_path), method, params)


    def get_suggested_contacts_for_user(self, id, **kwargs):
        """Fetch a user's suggested contact list

        Args:
            id, str: User ID (required)

            limit, int: Number of contacts returned (optional)

            offset, int: The offset of the first contact returned (optional)

        Returns:
        """

        all_params = ['id', 'limit', 'offset', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_suggested_contacts_for_user" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/{id}/suggested-contacts'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        if ('id' in params):
            replacement = str(self.client.to_path_value(params.pop('id')))
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)

        return self.client.request(self._request_url(resource_path), method, params)


    def get_combined_contacts_for_user(self, id, **kwargs):
        """Fetch a user's contact list and suggested contacts in a combined reposne

        Args:
            id, str: User ID (required)

            limit, int: Number of contacts returned (in each list) (optional)

            offset, int: The offset of the first contact returned (optional)

        Returns:
        """

        all_params = ['id', 'limit', 'offset', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_combined_contacts_for_user" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/{id}/combined-contacts'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        if ('id' in params):
            replacement = str(self.client.to_path_value(params('id')))
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)

        return self.client.request(self._request_url(resource_path), method, params)


    def get_data_for_user(self, id, **kwargs):
        """Gets paginated  content for a target user.

        Args:
            id, str: User ID (required)

            vendor_domain, str: the URL of the vendor's email address (optional)

            since, str: lower bound date in [ISO DateTimeNoMillis](http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTimeNoMillis()) format (optional)

            until, str: upper bound date in [ISO DateTimeNoMillis](http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTimeNoMillis()) format (optional)

            created_since, str: lower bound date for the creation of the item, in [ISO DateTimeNoMillis](http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTimeNoMillis()) format. Note that the created date is when it was created in the Airseed system. (optional)

            callback_url, str: posts the requested data via webhook to the specified callback URL (optional)

            limit, int: Number of  returned (optional)

            offset, int: The offset of the first  returned (optional)

            category, str: data category, for eg products, travel (optional)

            subcategory, str: data sub category, for eg products => electronics, travel => flights (optional)


        Returns:
        """

        all_params = ['id', 'vendor_domain', 'since', 'until', 'created_since', 'callback_url', 'limit', 'offset', 'category', 'subcategory', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_data_for_user" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/{id}'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        if ('id' in params):
            replacement = str(self.client.to_path_value(params.pop('id')))
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)

        if ('category' in params):
            replacement = str(self.client.to_path_value(params.pop('category')))
            resource_path = resource_path + "/" + replacement
            if ('subcategory' in params):
                replacement = str(self.client.to_path_value(params.pop('subcategory')))
                resource_path = resource_path + "/" + replacement

        return self.client.request(self._request_url(resource_path), method, params)


    def get_parsed_email_content_by_id(self, id, eid, **kwargs):
        """Gets structured contents of a specific email of a user.

        Args:
            id, str: the unique Airseed ID of the user (required)

            eid, str: the unique Airseed ID of the email (required)

        Returns:
        """

        all_params = ['id', 'eid', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_parsed_email_content_by_id" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/{id}/emails/{eid}'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        if ('id' in params):
            replacement = str(self.client.to_path_value(params.pop('id')))
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        if ('eid' in params):
            replacement = str(self.client.to_path_value(params.pop('eid')))
            resource_path = resource_path.replace('{' + 'eid' + '}',
                                                replacement)

        return self.client.request(self._request_url(resource_path), method, params)


    def reparse_email_for_user(self, id, eid, **kwargs):
        """Initiates a reparse request for a specific email of a user

        Args:
            id, str: the unique Airseed ID of the user (required)

            eid, str: the unique Airseed ID of the email (required)

            callback_url, str: URL to notify (by POST) when the reparse is completed (optional)

        Returns:
        """

        all_params = ['id', 'eid', 'callback_url', 'bearer_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method reparse_email_for_user" % key)
            params[key] = val
        del params['kwargs']
        del params['self']
        del params['all_params']

        resource_path = '/v1/users/{id}/emails/{eid}/reparse'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'POST'

        if ('id' in params):
            replacement = str(self.client.to_path_value(params.pop('id')))
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        if ('eid' in params):
            replacement = str(self.client.to_path_value(params.pop('eid')))
            resource_path = resource_path.replace('{' + 'eid' + '}',
                                                replacement)

        return self.client.request(self._request_url(resource_path), method, params)


    def _request_url(self, path):
        return str(API_BASE_URL) + str(path)
