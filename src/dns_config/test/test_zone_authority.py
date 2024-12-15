# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.models.zone_authority import ZoneAuthority


class TestZoneAuthority(unittest.TestCase):
    """ZoneAuthority unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ZoneAuthority:
        """Test ZoneAuthority
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ZoneAuthority`
        """
        model = ZoneAuthority()
        if include_optional:
            return ZoneAuthority(
                default_ttl = 56,
                expire = 56,
                mname = '',
                negative_ttl = 56,
                protocol_mname = '',
                protocol_rname = '',
                refresh = 56,
                retry = 56,
                rname = '',
                use_default_mname = True
            )
        else:
            return ZoneAuthority(
        )
        """

    def testZoneAuthority(self):
        """Test ZoneAuthority"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()