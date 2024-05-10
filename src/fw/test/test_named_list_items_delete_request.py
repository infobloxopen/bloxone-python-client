# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from fw.models.named_list_items_delete_request import NamedListItemsDeleteRequest


class TestNamedListItemsDeleteRequest(unittest.TestCase):
    """NamedListItemsDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NamedListItemsDeleteRequest:
        """Test NamedListItemsDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NamedListItemsDeleteRequest`
        """
        model = NamedListItemsDeleteRequest()
        if include_optional:
            return NamedListItemsDeleteRequest(
                id = 56,
                items = [example1.somedomain.com, 193.56.2.11, 2001:db8:ffff:ffff:ffff:ffff:ffff:fff1, 34.2.176.0/24, 2001:db8:abcd:0012::0/64],
                items_described = [{description=Item 1 Description, item=example1.somedomain.com}, {description=Item 2 Description, item=193.56.2.11/32}, {description=Item 3 Description, item=2001:db8:ffff:ffff:ffff:ffff:ffff:fff1/128}, {description=Item 4 Description, item=193.56.2.11}]
            )
        else:
            return NamedListItemsDeleteRequest(
        )
        """

    def testNamedListItemsDeleteRequest(self):
        """Test NamedListItemsDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
