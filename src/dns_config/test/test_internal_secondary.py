# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.models.internal_secondary import InternalSecondary


class TestInternalSecondary(unittest.TestCase):
    """InternalSecondary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalSecondary:
        """Test InternalSecondary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalSecondary`
        """
        model = InternalSecondary()
        if include_optional:
            return InternalSecondary(
                host = 'dns/host/23311109-fad4-448f-a7a7-55ad791ae7eb'
            )
        else:
            return InternalSecondary(
                host = 'dns/host/23311109-fad4-448f-a7a7-55ad791ae7eb',
        )
        """

    def testInternalSecondary(self):
        """Test InternalSecondary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
