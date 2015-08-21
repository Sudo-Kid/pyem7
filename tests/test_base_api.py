import unittest
import requests_mock
import json
import os


from pyem7.base_api import BaseAPI


@requests_mock.mock()
class TestSetConnection(unittest.TestCase):
    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="mock:://api.test.com",
            session_verify=False
        )

    def test_set_connection(self, mock):
        self.assertEqual("test_user", self.base_api.user_name)
        self.assertEqual("test_password", self.base_api.password)
        self.assertEqual("mock:://api.test.com", self.base_api.end_point)

    def test_set_connection_with_bad_values(self, mock):
        self.assertNotEqual("user", self.base_api.user_name)
        self.assertNotEqual("password", self.base_api.password)
        self.assertNotEqual("mock:://test.com", self.base_api.end_point)


@requests_mock.mock()
class TestPerformRequest(unittest.TestCase):
    with open(os.path.join(
            os.path.dirname(__file__),
            'data/base_api.json'
    )) as data_file:
        data = json.load(data_file)

    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="mock:://api.test.com",
            session_verify=False
        )

    def test__perform_request_with_get(self, mock):
        headers = self.data['good-header']
        response_data = self.data['good-content']
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        test = self.base_api._perform_request(self.base_api.end_point)

        self.assertEqual(test.headers['content-type'], 'application/json')
