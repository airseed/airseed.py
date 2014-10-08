#!/usr/bin/env python
"""Wordnik.com's Swagger generic API client. This client handles the client-
server communication, and is invariant across implementations. Specifics of
the methods and models for each application are generated from the Swagger
templates."""

import sys
import os
import re
import base64
import urllib
import urllib2
import httplib
import json
import datetime


class Client:
    """Generic API client for Swagger client library builds"""


    def __init__(self, client_id = None, client_secret = None):
        self.client_id = client_id
        self.client_secret = client_secret


    def request(self, url, method, params):
        headers = {}
        data = None

        bearer_token = (params.pop('bearer_token') if 'bearer_token' in params else None)
        query_params = {}

        if params:
            # Need to remove None values, these should not be sent
            for param, value in params.items():
                if value != None:
                    query_params[param] = self.to_path_value(value, param)

        if method in ['GET']:
            url = url + '?' + urllib.urlencode(query_params)

        elif method in ['POST']:
            if query_params:
                headers['Content-type'] = 'application/json'
                data = self.sanitize_for_serialization(query_params)
                data = json.dumps(data)

        else:
            raise Exception('Method ' + method + ' is not recognized.')

        if bearer_token:
            headers['Authorization'] = "Bearer %s" % bearer_token

        else:
            base64string = base64.encodestring('%s:%s' % (self.client_id, self.client_secret)).replace('\n', '')
            headers['Authorization'] = "Basic %s" % base64string

        request = MethodRequest(method=method, url=url, headers=headers,
                                data=data)

        # print request.get_full_url()
        # print request.get_method()
        # print request.header_items()
        # print request.get_data()

        # Make the request
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError,e:
            raise APIError(str(e), 'API call failed', url)

        try:
            string = response.read()
            data = json.loads(string)
        except ValueError:  # PUT requests don't return anything
            data = None

        # print data
        return data


    def to_path_value(self, obj, key=None):
        """Convert a string or object to a path-friendly value
        Args:
            obj -- object or string value
        Returns:
            string -- quoted value
        """
        # if "token" in key:
        return str(obj)
        # if type(obj) == list:
        #     return urllib.quote(','.join(obj))
        # else:
        #     return urllib.quote(str(obj))


    def sanitize_for_serialization(self, obj):
        """Dump an object into JSON for POSTing."""

        if type(obj) == type(None):
            return None
        elif type(obj) in [str, int, long, float, bool]:
            return obj
        elif type(obj) == list:
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif type(obj) == datetime.datetime:
            return obj.isoformat()
        else:
            if type(obj) == dict:
                obj_dict = obj
            else:
                obj_dict = obj.__dict__
            return {key: self.sanitize_for_serialization(val)
                    for (key, val) in obj_dict.iteritems()
                    if key != 'swaggerTypes'}


    def deserialize(self, obj, obj_class):
        """Derialize a JSON string into an object.

        Args:
            obj -- string or object to be deserialized
            obj_class -- class literal for deserialzied object, or string
                of class name
        Returns:
            object -- deserialized object"""

        # Have to accept obj_class as string or actual type. Type could be a
        # native Python type, or one of the model classes.
        if type(obj_class) == str:
            if 'list[' in obj_class:
                match = re.match('list\[(.*)\]', obj_class)
                sub_class = match.group(1)
                return [self.deserialize(sub_obj, sub_class) for sub_obj in obj]

            if (obj_class in ['int', 'float', 'long', 'dict', 'list', 'str', 'bool', 'datetime']):
                obj_class = eval(obj_class)
            else:  # not a native type, must be model class
                obj_class = eval(obj_class + '.' + obj_class)

        if obj_class in [int, long, float, dict, list, str, bool]:
            return obj_class(obj)
        elif obj_class == datetime:
            # Server will always return a time stamp in UTC, but with
            # trailing +0000 indicating no offset from UTC. So don't process
            # last 5 characters.
            return datetime.datetime.strptime(obj[:-5],
                                              "%Y-%m-%dT%H:%M:%S.%f")

        instance = obj_class()

        for attr, attr_type in instance.swaggerTypes.iteritems():
            if obj is not None and attr in obj and type(obj) in [list, dict]:
                value = obj[attr]
                if attr_type in ['str', 'int', 'long', 'float', 'bool']:
                    attr_type = eval(attr_type)
                    try:
                        value = attr_type(value)
                    except UnicodeEncodeError:
                        value = unicode(value)
                    except TypeError:
                        value = value
                    setattr(instance, attr, value)
                elif (attr_type == 'datetime'):
                    setattr(instance, attr, datetime.datetime.strptime(value[:-5],
                                              "%Y-%m-%dT%H:%M:%S.%f"))
                elif 'list[' in attr_type:
                    match = re.match('list\[(.*)\]', attr_type)
                    sub_class = match.group(1)
                    sub_values = []
                    if not value:
                        setattr(instance, attr, None)
                    else:
                        for sub_value in value:
                            sub_values.append(self.deserialize(sub_value,
                                                              sub_class))
                    setattr(instance, attr, sub_values)
                else:
                    setattr(instance, attr, self.deserialize(value,
                                                             obj_class))

        return instance


class MethodRequest(urllib2.Request):


    def __init__(self, *args, **kwargs):
        """Construct a MethodRequest. Usage is the same as for
        `urllib2.Request` except it also takes an optional `method`
        keyword argument. If supplied, `method` will be used instead of
        the default."""

        if 'method' in kwargs:
            self.method = kwargs.pop('method')
        return urllib2.Request.__init__(self, *args, **kwargs)


    def get_method(self):
        return getattr(self, 'method', urllib2.Request.get_method(self))


class APIError(Exception):
    pass
