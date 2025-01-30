import unittest

import universal_ddi_client


class TestApiClient(unittest.TestCase):

    def setUp(self) -> None:
        self.api_client = universal_ddi_client.ApiClient()

    def tearDown(self) -> None:
        pass

    def test_default_client(self):
        self.assertIsNotNone(self.api_client.configuration)
        self.assertEqual(self.api_client.configuration.portal_url,
                         'https://csp.infoblox.com')
        self.assertEqual(self.api_client.configuration.client_name,
                         'universal-ddi-python-client')

    def test_path_param_value_with_resource_id_type(self):
        result = self.api_client.path_param_value('id', 'app/type/id',
                                                  'resource_id')
        self.assertEqual(result, 'id')

    def test_path_param_value_with_default_id(self):
        result = self.api_client.path_param_value('id', 'type/id')
        self.assertEqual(result, 'id')

    def test_path_param_value_with_non_id_key(self):
        result = self.api_client.path_param_value('key', 'type/id')
        self.assertEqual(result, 'type/id')

    def test_path_param_value_with_non_id_key_and_resource_id_type(self):
        result = self.api_client.path_param_value('key', 'type/id',
                                                  'resource_id')
        self.assertEqual(result, 'id')

    def test_path_param_value_with_single_value(self):
        result = self.api_client.path_param_value('id', 'id')
        self.assertEqual(result, 'id')

    def test_path_param_value_with_empty_value(self):
        result = self.api_client.path_param_value('id', '')
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
