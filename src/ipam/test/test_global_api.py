# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.api.global_api import GlobalApi


class TestGlobalApi(unittest.TestCase):
    """GlobalApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GlobalApi()

    def tearDown(self) -> None:
        pass

    def test_Read(self) -> None:
        """Test case for Read

        Retrieve the global configuration.
        """
        pass

    def test_ReadById(self) -> None:
        """Test case for ReadById

        Retrieve the global configuration.
        """
        pass

    def test_Update(self) -> None:
        """Test case for Update

        Update the global configuration.
        """
        pass

    def test_UpdateById(self) -> None:
        """Test case for UpdateById

        Update the global configuration.
        """
        pass


if __name__ == '__main__':
    unittest.main()
