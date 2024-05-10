# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.fixed_address import FixedAddress


class TestFixedAddress(unittest.TestCase):
    """FixedAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FixedAddress:
        """Test FixedAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FixedAddress`
        """
        model = FixedAddress()
        if include_optional:
            return FixedAddress(
                address = '192.168.1.10',
                comment = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dhcp_options = [
                    ipam.models.option_item.OptionItem(
                        group = '', 
                        option_code = '', 
                        option_value = '', 
                        type = '', )
                    ],
                disable_dhcp = True,
                header_option_filename = '',
                header_option_server_address = '',
                header_option_server_name = '',
                hostname = '',
                id = '',
                inheritance_assigned_hosts = [
                    ipam.models.assigned_host.AssignedHost(
                        display_name = '', 
                        host = '', 
                        ophid = '', )
                    ],
                inheritance_parent = '',
                inheritance_sources = ipam.models.fixed_address_inheritance.FixedAddressInheritance(
                    dhcp_options = ipam.models.inherited_dhcp_option_list.InheritedDHCPOptionList(
                        action = '', 
                        value = [
                            ipam.models.inherited_dhcp_option.InheritedDHCPOption(
                                action = '', 
                                display_name = '', 
                                source = '', )
                            ], ), 
                    header_option_filename = ipam.models.inherited_string.InheritedString(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    header_option_server_address = ipam.models.inherited_string.InheritedString(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    header_option_server_name = , ),
                ip_space = '',
                match_type = 'mac',
                match_value = '00:0a:95:9d:68:16',
                name = '',
                parent = '',
                tags = ipam.models.tags.tags(),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return FixedAddress(
                address = '192.168.1.10',
                match_type = 'mac',
                match_value = '00:0a:95:9d:68:16',
        )
        """

    def testFixedAddress(self):
        """Test FixedAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
