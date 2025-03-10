# coding: utf-8

"""
    IPAM Federation API

    The DDI IPAM Federation application enables a SaaS administrator to manage multiple IPAM systems from one central control point CSP.    

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam_federation.api.reserved_block_api import ReservedBlockApi

from universal_ddi_client.api_client import ApiClient


class TestReservedBlockApi(unittest.TestCase):
    """ReservedBlockApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = ReservedBlockApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the reserved block.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete the reserved block.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        Retrieve the reserved block.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Retrieve the reserved block.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the reserved block.
        """
        pass


if __name__ == '__main__':
    unittest.main()
