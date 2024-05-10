# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.read_ipam_host_response import ReadIpamHostResponse


class TestReadIpamHostResponse(unittest.TestCase):
    """ReadIpamHostResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadIpamHostResponse:
        """Test ReadIpamHostResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadIpamHostResponse`
        """
        model = ReadIpamHostResponse()
        if include_optional:
            return ReadIpamHostResponse(
                result = ipam.models.ipam_host.IpamHost(
                    addresses = [
                        ipam.models.addresses.Addresses(
                            address = '', 
                            ref = '', 
                            space = '', )
                        ], 
                    auto_generate_records = True, 
                    comment = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    host_names = [
                        ipam.models.host_name.HostName(
                            alias = True, 
                            name = 'Example Host Name', 
                            primary_name = True, 
                            zone = 'dns/auth_zone/45d344c2-004e-42e4-9a41-fc5d0b38fd58', )
                        ], 
                    id = '', 
                    name = 'Example IPAM Host', 
                    tags = ipam.models.tags.tags(), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ReadIpamHostResponse(
        )
        """

    def testReadIpamHostResponse(self):
        """Test ReadIpamHostResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
