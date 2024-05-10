# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.models.delegation import Delegation


class TestDelegation(unittest.TestCase):
    """Delegation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Delegation:
        """Test Delegation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Delegation`
        """
        model = Delegation()
        if include_optional:
            return Delegation(
                comment = '',
                delegation_servers = [
                    dns_config.models.delegation_server.DelegationServer(
                        address = '', 
                        fqdn = 'ns1.example.com', 
                        protocol_fqdn = '', )
                    ],
                disabled = True,
                fqdn = '',
                id = '',
                parent = '',
                protocol_fqdn = '',
                tags = dns_config.models.tags.tags(),
                view = ''
            )
        else:
            return Delegation(
        )
        """

    def testDelegation(self):
        """Test Delegation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
