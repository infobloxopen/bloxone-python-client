# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from fw.models.named_lists_update_named_list_partial404_response import NamedListsUpdateNamedListPartial404Response


class TestNamedListsUpdateNamedListPartial404Response(unittest.TestCase):
    """NamedListsUpdateNamedListPartial404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self,
            include_optional) -> NamedListsUpdateNamedListPartial404Response:
        """Test NamedListsUpdateNamedListPartial404Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NamedListsUpdateNamedListPartial404Response`
        """
        model = NamedListsUpdateNamedListPartial404Response()
        if include_optional:
            return NamedListsUpdateNamedListPartial404Response(
                error = fw.models.named_lists_update_named_list_partial_404_response_error.named_listsUpdateNamedListPartial_404_response_error(
                    code = 'NOT_FOUND', 
                    message = 'Given Named List does not exist', 
                    status = '404', )
            )
        else:
            return NamedListsUpdateNamedListPartial404Response(
        )
        """

    def testNamedListsUpdateNamedListPartial404Response(self):
        """Test NamedListsUpdateNamedListPartial404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
