# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from fw.models.internal_domain_lists_delete_internal_domains400_response import InternalDomainListsDeleteInternalDomains400Response


class TestInternalDomainListsDeleteInternalDomains400Response(
        unittest.TestCase):
    """InternalDomainListsDeleteInternalDomains400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> InternalDomainListsDeleteInternalDomains400Response:
        """Test InternalDomainListsDeleteInternalDomains400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalDomainListsDeleteInternalDomains400Response`
        """
        model = InternalDomainListsDeleteInternalDomains400Response()
        if include_optional:
            return InternalDomainListsDeleteInternalDomains400Response(
                error = fw.models.internal_domain_lists_delete_internal_domains_400_response_error.internal_domain_listsDeleteInternalDomains_400_response_error(
                    code = 'FAILED_PRECONDITION', 
                    message = 'Internal Domains List ids can't be empty', 
                    status = '400', )
            )
        else:
            return InternalDomainListsDeleteInternalDomains400Response(
        )
        """

    def testInternalDomainListsDeleteInternalDomains400Response(self):
        """Test InternalDomainListsDeleteInternalDomains400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
