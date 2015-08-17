import unittest
import requests_mock


from base_api import BaseAPI


@requests_mock.mock()
class TestPerformRequest(unittest.TestCase):
    def setUp(self):
        self.base_api = BaseAPI()
        self.base_api.set_connection(
            user_name="test_user",
            password="test_password",
            end_point="mock:://api.test.com",
            session_verify=False
        )

    def test__perform_request_with_get(self, mock):
        headers = {'x-em7-status-code': 'OK'}
        response_data = {'test': 'data'}
        mock.get(requests_mock.ANY, json=response_data, headers=headers)
        test = self.base_api._perform_request(self.base_api.end_point)
        self.assertEqual(test.headers, headers)


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
