# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.create_next_available_ip_response import CreateNextAvailableIPResponse


class TestCreateNextAvailableIPResponse(unittest.TestCase):
    """CreateNextAvailableIPResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateNextAvailableIPResponse:
        """Test CreateNextAvailableIPResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateNextAvailableIPResponse`
        """
        model = CreateNextAvailableIPResponse()
        if include_optional:
            return CreateNextAvailableIPResponse(
                results = [
                    ipam.models.address.Address(
                        address = '10.0.0.0', 
                        comment = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        dhcp_info = ipam.models.dhcp_info.DHCPInfo(
                            client_hostname = '', 
                            client_hwaddr = '', 
                            client_id = '', 
                            end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            fingerprint = '', 
                            iaid = 56, 
                            lease_type = '', 
                            preferred_lifetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            remain = 56, 
                            start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            state = '', 
                            state_ts = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        disable_dhcp = True, 
                        discovery_attrs = ipam.models.discovery_attrs.discovery_attrs(), 
                        discovery_metadata = ipam.models.discovery_metadata.discovery_metadata(), 
                        host = '', 
                        hwaddr = '', 
                        id = '', 
                        interface = '', 
                        names = [
                            ipam.models.name.Name(
                                name = 'example.com', 
                                type = 'FQDN', )
                            ], 
                        parent = '', 
                        protocol = '', 
                        range = '', 
                        space = '', 
                        state = '', 
                        tags = ipam.models.tags.tags(), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        usage = [
                            ''
                            ], )
                    ]
            )
        else:
            return CreateNextAvailableIPResponse(
        )
        """

    def testCreateNextAvailableIPResponse(self):
        """Test CreateNextAvailableIPResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
