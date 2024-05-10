# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.models.lbdn import LBDN


class TestLBDN(unittest.TestCase):
    """LBDN unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LBDN:
        """Test LBDN
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LBDN`
        """
        model = LBDN()
        if include_optional:
            return LBDN(
                comment = '',
                disabled = True,
                dtc_policy = dns_config.models.dtc_policy.DTCPolicy(
                    name = '', 
                    policy_id = '', ),
                id = '',
                inheritance_sources = dns_config.models.ttl_inheritance.TTLInheritance(
                    ttl = dns_config.models.inherited_u_int32.InheritedUInt32(
                        action = '', 
                        display_name = '', 
                        source = '', 
                        value = 56, ), ),
                name = 'example.com',
                precedence = 56,
                tags = dns_config.models.tags.tags(),
                ttl = 56,
                view = 'dns/view/23311109-fad4-448f-a7a7-55ad791ae7eb'
            )
        else:
            return LBDN(
                name = 'example.com',
                view = 'dns/view/23311109-fad4-448f-a7a7-55ad791ae7eb',
        )
        """

    def testLBDN(self):
        """Test LBDN"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
