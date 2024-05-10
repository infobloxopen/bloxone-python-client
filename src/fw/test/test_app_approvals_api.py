# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from fw.api.app_approvals_api import AppApprovalsApi


class TestAppApprovalsApi(unittest.TestCase):
    """AppApprovalsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AppApprovalsApi()

    def tearDown(self) -> None:
        pass

    def test_ListAppApprovals(self) -> None:
        """Test case for ListAppApprovals

        """
        pass

    def test_ReplaceAppApprovals(self) -> None:
        """Test case for ReplaceAppApprovals

        Update Application Approval.
        """
        pass

    def test_UpdateAppApprovals(self) -> None:
        """Test case for UpdateAppApprovals

        """
        pass


if __name__ == '__main__':
    unittest.main()
