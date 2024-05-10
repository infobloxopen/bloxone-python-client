# coding: utf-8

"""
    DFP API

    BloxOne Cloud is a SaaS offering designed to provide protection to devices on and off-premises, including roaming, remote, and branch offices. It provides visibility into infected and compromised devices, prevents DNS-based data exfiltration, and automatically stops device communications with command-and-control servers (C&Cs) and botnets, in addition to providing recursive DNS services in the cloud. You can access the services by deploying the BloxOne Endpoint agent or the DNS forwarding proxy.  For remote office deployments or in cases where installing an endpoint agent is not desirable or possible, you can use the DNS forwarding proxy. It is a software that runs on bare-metal, VM infrastructures, or Infoblox NIOS appliances; and it embeds the client IPs in DNS queries before forwarding them to BloxOne Cloud. The communications are encrypted and client visibility is maintained. The proxy also provides DNS resolution to local DNS zones when you configure local resolvers. Once you set up a DNS forwarding proxy, it becomes the main DNS server for your remote site. It will also cache responses to speed resolution of future queries.  By implementing the DNS forwarding proxy, you can rest assured that BloxOne Cloud effectively enforces DNS client-based security policies at your remote sites. On-premises devices that send DNS queries reveal their actual client IP addresses (instead of their NAT IP address), which allows BloxOne Cloud to apply the security policies applicable to the respective endpoints and identify infected clients. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dfp.models.infra_services_create_or_update_dfp_service404_response_error import InfraServicesCreateOrUpdateDfpService404ResponseError


class TestInfraServicesCreateOrUpdateDfpService404ResponseError(
        unittest.TestCase):
    """InfraServicesCreateOrUpdateDfpService404ResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> InfraServicesCreateOrUpdateDfpService404ResponseError:
        """Test InfraServicesCreateOrUpdateDfpService404ResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfraServicesCreateOrUpdateDfpService404ResponseError`
        """
        model = InfraServicesCreateOrUpdateDfpService404ResponseError()
        if include_optional:
            return InfraServicesCreateOrUpdateDfpService404ResponseError(
                code = 'NOT_FOUND',
                message = 'Dfp does not exist',
                status = '404'
            )
        else:
            return InfraServicesCreateOrUpdateDfpService404ResponseError(
        )
        """

    def testInfraServicesCreateOrUpdateDfpService404ResponseError(self):
        """Test InfraServicesCreateOrUpdateDfpService404ResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
