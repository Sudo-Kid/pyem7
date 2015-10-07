import unittest
import requests_mock
import json
import os
import requests


from pyem7.base_api import BaseAPI
from pyem7.custom_errors import AuthError


def get_test_data():
    with open(os.path.join(os.path.dirname(__file__), 'data/base_api.json')) as data_file:
        data = json.load(data_file)
    data_file.closed
    return data


@requests_mock.mock()
class TestSetConnection(unittest.TestCase):
    data = get_test_data()

    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )

    def test_set_connection(self, mock):
        self.assertEqual("test_user", self.base_api.user_name)
        self.assertEqual("test_password", self.base_api.password)
        self.assertEqual("http://api.test.com", self.base_api.end_point)

    def test_set_connection_with_bad_values(self, mock):
        self.assertNotEqual("user", self.base_api.user_name)
        self.assertNotEqual("password", self.base_api.password)
        self.assertNotEqual("http://test.com", self.base_api.end_point)


@requests_mock.mock()
class TestPerformRequest(unittest.TestCase):
    data = get_test_data()

    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )

    def test__perform_request_with_no_user_name(self, mock):
        headers = self.data['auth-error-header']
        response_data = self.data['auth-error-content']
        self.base_api.set_connection(
            user_name='',
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        with self.assertRaises(AuthError):
            self.base_api._perform_request(self.base_api.end_point)

    def test__perform_request_with_with_none_as_user_name(self, mock):
        headers = self.data['auth-error-header']
        response_data = self.data['auth-error-content']
        self.base_api.set_connection(
            user_name=None,
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        with self.assertRaises(AuthError):
            self.base_api._perform_request(self.base_api.end_point)

    def test__perform_request_with_no_password_name(self, mock):
        headers = self.data['auth-error-header']
        response_data = self.data['auth-error-content']
        self.base_api.set_connection(
            user_name='test',
            password="",
            end_point="http://api.test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        with self.assertRaises(AuthError):
            self.base_api._perform_request(self.base_api.end_point)

    def test__perform_request_with_none_as_password_name(self, mock):
        headers = self.data['auth-error-header']
        response_data = self.data['auth-error-content']
        self.base_api.set_connection(
            user_name='test',
            password=None,
            end_point="http://api.test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        with self.assertRaises(AuthError):
            self.base_api._perform_request(self.base_api.end_point)

    def test__perform_request_returns_requests_object(self, mock):
        headers = self.data['good-header']
        response_data = self.data['good-content']
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        test = self.base_api._perform_request(self.base_api.end_point)

        self.assertIsInstance(test, requests.models.Response)


@requests_mock.mock()
class TestPost(unittest.TestCase):
    pass


@requests_mock.mock()
class TestDelete(unittest.TestCase):
    pass


@requests_mock.mock()
class TestGet(unittest.TestCase):
    data = get_test_data()

    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )

    def test__perform_request_returns_requests_object(self, mock):
        headers = self.data['good-header']
        response_data = self.data['good-content']
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        test = self.base_api._perform_request(self.base_api.end_point)

        self.assertIsInstance(test, requests.models.Response)


@requests_mock.mock()
class TestFind(unittest.TestCase):
    data = get_test_data()

    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )

    def test_find_returns_requests_object(self, mock):
        headers = self.data['good-header']
        response_data = self.data['good-content']
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        test = self.base_api.find(
            self.base_api.end_point,
            search_spec='test',
            search_string='test',
            extended_fetch=False
        )

        self.assertIsInstance(test, requests.models.Response)


@requests_mock.mock()
class TestGetURI(unittest.TestCase):
    data = get_test_data()

    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )

    def test_get_uri_with_multiple_resaults(self, mock):
        headers = self.data['good-header']
        response_data = self.data['good-content']
        self.base_api.set_connection(
            user_name='test',
            password="test_password",
            end_point="http:://test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        test = self.base_api.get_uri(
            search_string='Get/Delete Access Locks',
            search_spec='test')
        self.assertEquals(test['Get/Delete Access Locks'], "/api/access_lock")
        self.assertEquals(test['Get/Update/Add/Delete User Accounts'], "/api/account")

    def test_get_uri_with_single_resaults(self, mock):
        headers = self.data['good-header']
        response_data = self.data['get_uri_with_single_resaults']
        self.base_api.set_connection(
            user_name='test',
            password="test_password",
            end_point="http:://test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        test = self.base_api.get_uri(
            search_string='Get/Delete Access Locks',
            search_spec='test')
        self.assertEquals(test['Get/Delete Access Locks'], "/api/access_lock")


@requests_mock.mock()
class TestPayload(unittest.TestCase):
    pass


@requests_mock.mock()
class TestCreate(unittest.TestCase):
    pass


@requests_mock.mock()
class TestUpdate(unittest.TestCase):
    pass
