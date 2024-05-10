# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.option_filter_rule import OptionFilterRule


class TestOptionFilterRule(unittest.TestCase):
    """OptionFilterRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionFilterRule:
        """Test OptionFilterRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionFilterRule`
        """
        model = OptionFilterRule()
        if include_optional:
            return OptionFilterRule(
                compare = 'equals',
                option_code = 'dhcp/option_code/0b41ec0d-2675-455e-af6d-0bfb3b4220ba',
                option_value = '',
                substring_offset = 56
            )
        else:
            return OptionFilterRule(
                compare = 'equals',
                option_code = 'dhcp/option_code/0b41ec0d-2675-455e-af6d-0bfb3b4220ba',
        )
        """

    def testOptionFilterRule(self):
        """Test OptionFilterRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
