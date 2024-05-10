# coding: utf-8

"""
    DFP API

    BloxOne Cloud is a SaaS offering designed to provide protection to devices on and off-premises, including roaming, remote, and branch offices. It provides visibility into infected and compromised devices, prevents DNS-based data exfiltration, and automatically stops device communications with command-and-control servers (C&Cs) and botnets, in addition to providing recursive DNS services in the cloud. You can access the services by deploying the BloxOne Endpoint agent or the DNS forwarding proxy.  For remote office deployments or in cases where installing an endpoint agent is not desirable or possible, you can use the DNS forwarding proxy. It is a software that runs on bare-metal, VM infrastructures, or Infoblox NIOS appliances; and it embeds the client IPs in DNS queries before forwarding them to BloxOne Cloud. The communications are encrypted and client visibility is maintained. The proxy also provides DNS resolution to local DNS zones when you configure local resolvers. Once you set up a DNS forwarding proxy, it becomes the main DNS server for your remote site. It will also cache responses to speed resolution of future queries.  By implementing the DNS forwarding proxy, you can rest assured that BloxOne Cloud effectively enforces DNS client-based security policies at your remote sites. On-premises devices that send DNS queries reveal their actual client IP addresses (instead of their NAT IP address), which allows BloxOne Cloud to apply the security policies applicable to the respective endpoints and identify infected clients. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dfp.models.dfp_read_response import DfpReadResponse


class TestDfpReadResponse(unittest.TestCase):
    """DfpReadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DfpReadResponse:
        """Test DfpReadResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DfpReadResponse`
        """
        model = DfpReadResponse()
        if include_optional:
            return DfpReadResponse(
                results = dfp.models.atcdfp_dfp.atcdfpDfp(
                    created_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    elb_ip_list = [1.1.1.1, 2001:cdba:9abc:5678:ffff:ffff:ffff:ffff], 
                    forwarding_policy = '', 
                    host = [
                        dfp.models.atcdfp_dfp_host.atcdfpDfpHost(
                            legacy_host_id = 56, 
                            name = 'dfp_a', 
                            ophid = 'aed8263b8900bfb178e0bb7c57ba5af8', 
                            site_id = '134997289555407a8527bea7957ea7a0', )
                        ], 
                    id = 56, 
                    internal_domain_lists = [
                        56
                        ], 
                    name = 'dfp_a', 
                    net_addr_policy_ids = [
                        dfp.models.atcdfp_net_addr_policy_assignment.atcdfpNetAddrPolicyAssignment(
                            addr_net = '', 
                            policy_id = 56, )
                        ], 
                    ophid = 'aed8263b8900bfb178e0bb7c57ba5af8', 
                    policy_id = 52134, 
                    pop_region_id = 56, 
                    resolvers_all = [
                        dfp.models.atcdfp_resolver.atcdfpResolver(
                            address = '', 
                            is_fallback = True, 
                            is_local = True, 
                            protocols = [DO53, DOT], )
                        ], 
                    service_id = 'u2y3w3fuhhtx7aykfkuergkuboc33wyqrrmjnr5tyrlyredwow374gu5uwzqnsb6', 
                    service_name = 'dfp_service_1', 
                    site_id = '134997289555407a8527bea7957ea7a0', 
                    updated_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return DfpReadResponse(
        )
        """

    def testDfpReadResponse(self):
        """Test DfpReadResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
