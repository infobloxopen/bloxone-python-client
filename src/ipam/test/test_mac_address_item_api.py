# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a Universal DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.api.mac_address_item_api import MacAddressItemApi

from universal_ddi_client.api_client import ApiClient


class TestMacAddressItemApi(unittest.TestCase):
    """MacAddressItemApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = MacAddressItemApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_bulk_create(self) -> None:
        """Test case for bulk_create

        Bulk create the mac address items.
        """
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the mac address item.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete the mac address item.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        Retrieve mac address items.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Retrieve the mac address item.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the mac address item.
        """
        pass

    def test_upload(self) -> None:
        """Test case for upload

        Upload mac addresses to a large scale hardware filter.
        """
        pass


if __name__ == '__main__':
    unittest.main()
