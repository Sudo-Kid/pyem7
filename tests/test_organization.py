import unittest
import requests_mock
import json
import os


from pyem7.organization import Organization
from pyem7.custom_errors import AuthError


def get_test_data():
    with open(os.path.join(os.path.dirname(__file__),
              'data/add-organization.json')) as data_file:
        data = json.load(data_file)
    data_file.closed
    return data


@requests_mock.mock()
class TestPerformRequest(unittest.TestCase):
    data = get_test_data()

    def setUp(self):
        self.organization = Organization()
        self.organization.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )

    @unittest.skip("Not yet ready")
    def test__perform_request_with_no_user_name(self, mock):
        headers = self.data['auth-error-header']
        response_data = self.data['auth-error-content']
        self.organization.set_connection(
            user_name='',
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        with self.assertRaises(AuthError):
            self.organization._perform_request(self.organization.end_point)

    @unittest.skip("Not yet ready")
    def test__perform_request_with_with_none_as_user_name(self, mock):
        headers = self.data['auth-error-header']
        response_data = self.data['auth-error-content']
        self.organization.set_connection(
            user_name=None,
            password="test_password",
            end_point="http://api.test.com",
            session_verify=False
        )
        mock.get(requests_mock.ANY, json=response_data, headers=headers)

        with self.assertRaises(AuthError):
            self.organization._perform_request(self.organization.end_point)
