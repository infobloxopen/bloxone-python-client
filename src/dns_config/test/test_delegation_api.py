# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.api.delegation_api import DelegationApi


class TestDelegationApi(unittest.TestCase):
    """DelegationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DelegationApi()

    def tearDown(self) -> None:
        pass

    def test_Create(self) -> None:
        """Test case for Create

        Create the Delegation object.
        """
        pass

    def test_Delete(self) -> None:
        """Test case for Delete

        Moves the Delegation object to Recyclebin.
        """
        pass

    def test_List(self) -> None:
        """Test case for List

        List Delegation objects.
        """
        pass

    def test_Read(self) -> None:
        """Test case for Read

        Read the Delegation object.
        """
        pass

    def test_Update(self) -> None:
        """Test case for Update

        Update the Delegation object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
