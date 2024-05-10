# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.models.inherited_acl_items import InheritedACLItems


class TestInheritedACLItems(unittest.TestCase):
    """InheritedACLItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InheritedACLItems:
        """Test InheritedACLItems
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InheritedACLItems`
        """
        model = InheritedACLItems()
        if include_optional:
            return InheritedACLItems(
                action = '',
                display_name = '',
                source = '',
                value = [
                    dns_config.models.acl_item.ACLItem(
                        access = 'allow', 
                        acl = '', 
                        address = '', 
                        element = 'ip', 
                        tsig_key = dns_config.models.tsig_key.TSIGKey(
                            algorithm = '', 
                            comment = '', 
                            key = '', 
                            name = '', 
                            protocol_name = '', 
                            secret = '', ), )
                    ]
            )
        else:
            return InheritedACLItems(
        )
        """

    def testInheritedACLItems(self):
        """Test InheritedACLItems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
