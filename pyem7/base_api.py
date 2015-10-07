"""Comunicating with the API server."""
import json
import logging
import requests
import hashlib
import ast

from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin

from .custom_errors import AuthError
from .custom_errors import KeywordArgument


class BaseAPI(object):

    keyword_arguments = None
    lists = None
    bools = None
    dicts = None

    @classmethod
    def __init__(cls, **kwargs):
        [setattr(cls, key, value) for key, value in kwargs.items()]

    @classmethod
    def set_connection(cls, user_name, password, end_point, session_verify):
        """Setting the connection settings for the API server.

            :param user_name: the API accounts user name
            :param password: the API account password
            :param end_point: the API's URL/end point
            :param session_verify: if you want to check the API cert or not
        """
        if not session_verify:
            requests.packages.urllib3.disable_warnings()

        cls.user_name = user_name
        cls.password = password
        cls.end_point = end_point

        cls.session = requests.Session()
        cls.session.auth = HTTPBasicAuth(user_name, password)
        cls.session.verify = session_verify

    @classmethod
    def _perform_request(cls, url='', request_type='GET', params=None):
        """
            This method will perform the real request,
            in this way we can customize only the "output".
            This method will return the request object.
        """

        get = 'GET'
        post = 'POST'
        delete = 'DELETE'
        put = 'PUT'

        if params:
            params = json.dumps(params)

        if cls.user_name is None or not cls.user_name:
            raise AuthError("Missing user name. Please provide a valid user name.")
        if cls.password is None or not cls.password:
            raise AuthError("Missing password. Please provide a valid password.")

        url = cls.end_point + url

        if request_type.upper() == get:
            return cls.session.get(url, stream=False)
        elif request_type.upper() == post:
            logging.info('{0} - {1}'.format(request_type, params))
            return cls.session.post(url, data=params, stream=False)
        elif request_type.upper() == delete:
            logging.info('{0} - {1}'.format(request_type, params))
            return cls.session.delete(url, stream=False)
        elif request_type.upper() == put:
            logging.info('{0} - {1}'.format(request_type, params))
            return cls.session.put(url, data=params, stream=False)

    @classmethod
    def post(cls, uri, payload):
        """Create an item on the Science Logic server

            :param uri: The name of the item you wish to create
            :param payload: The payload for the item you wish to create

            :return: returns servers response to the POST request
        """
        return cls._perform_request(uri, 'POST', payload)

    @classmethod
    def delete(cls, uri):
        """Delete a record from the API server

            :param uri: The URI to the item you wish to delete

            :return: returns servers response to the DELETE request
        """
        return cls._perform_request(uri, 'DELETE')

    @classmethod
    def get(cls, uri):
        """Get an item by the URI

            :param uri : The URI for the item you wish to get data for.

            :return: returns servers response to the GET request
        """
        return cls._perform_request(uri, 'GET')

    @classmethod
    def find(cls, uri='/api/', search_spec='name', search_string='test', extended_fetch=False):
        """Find an Organization by name not id

            :note: extended_fetch= True to return full objects

            :param uri: The URI for you wish to preform the search at
            :apram search_spec: What you  are shearching by
            :param search_string: What you are searching for
            :param extended_fetch: Do you want the full objects or just the
                URI and description

            :return: returns With organization you searched for
        """
        if extended_fetch:
            options = "?limit=100&hide_filterinfo=1&extended_fetch=1&filter."
        else:
            options = "?limit=100&hide_filterinfo=1&filter."

        search = "{uri}{options}{search_spec}={search_string}".format(
            uri=uri,
            options=options,
            search_spec=search_spec,
            search_string=search_string
        )

        return cls._perform_request(url=search, request_type='GET')

    @classmethod
    def get_uri(cls, uri='/api/', search_spec='name', search_string='test'):
        """Get the URI for an item

            :note: extended_fetch= True to return full objects

            :param uri: The URI for you wish to preform the search at
            :apram search_spec: What you  are shearching by
            :param search_string: What you are searching for
            :param extended_fetch: Do you want the full objects or just the
                URI and description

            :example:
                response = BaseAPI().get_uri(
                    uri='/api/organization',
                    search_string='test'
                )
                print(response)
                # Output
                {'test': '/api/organization/123'}

            :return: returns a dict with the URI or URI's.
        """
        response = cls.find(
            uri=uri,
            search_spec=search_spec,
            search_string=search_string,
            extended_fetch=False
        )

        uri_list = {}
        if len(response.json()) == 1:
            # Create a dict out of the response
            uri_list = {response.json()[0]['description']: response.json()[0]['URI']}
        else:
            # Create a dict out of the response
            for value in response.json():
                uri_list.update({value['description']: value['URI']})

        return uri_list

    @classmethod
    def payload(cls, **kwargs):
        """Creat a payload for a post or update request

            :return: returns a dict with arguments as keyvalue pairs
        """
        payload = {}

        # If no lists, bools, or dicts have been defind
        if cls.lists is None:
            cls.lists = []
        if cls.bools is None:
            cls.bools = []
        if cls.dicts is None:
            cls.dicts = []
        if cls.keyword_arguments is None:
            cls.keyword_arguments = []

        # If nothing has been passed in
        if not kwargs:
            kwargs = {}

        for key, value in kwargs.items():
            if key not in cls.keyword_arguments:
                raise KeywordArgument('The keyword argument', key, 'is not supported')
                continue

            # Change strings to lists, bools, or dicts based on a provided list
            if key in cls.lists:
                if isinstance(value, str):
                    list_values = []
                    [list_values.append(value.strip(',')) for value in value.splitlines()]
                else:
                    list_values = [value]
                payload[key] = list_values
            elif key in cls.bools:
                payload[key] = ast.literal_eval(value)
            elif key in cls.dicts:
                payload[key] = json.loads(value)
            elif key == 'passwd':
                payload[key] = hashlib.md5(str.encode(value, 'utf-8')).hexdigest()
            else:
                payload[key] = value

        return payload

    @classmethod
    def create(cls, uri=None, search_spec=None, search_string=None,
               payload=None, **kwargs):
        """Creates an item on the server"""
        exists = cls.find(uri=uri, search_spec=search_spec,
                          search_string=search_string, extended_fetch=False)

        if not exists.json():
            return cls.post(uri, payload)
        else:
            return exists

    @classmethod
    def update(cls, uri, search_spec='name', search_string='test', extended_fetch=False,
               **kwargs):
        """Upate an Organization on the server"""
        exists = cls.find(uri=uri, search_spec=search_spec, search_string=search_string)

        if not exists.json():
            updates = cls.payload(**kwargs)
            return cls.post(uri, updates)
        else:
            return exists

    @classmethod
    def close(cls):
        cls.session.close()
