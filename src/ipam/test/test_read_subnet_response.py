# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.read_subnet_response import ReadSubnetResponse


class TestReadSubnetResponse(unittest.TestCase):
    """ReadSubnetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadSubnetResponse:
        """Test ReadSubnetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadSubnetResponse`
        """
        model = ReadSubnetResponse()
        if include_optional:
            return ReadSubnetResponse(
                result = ipam.models.subnet.Subnet(
                    address = '', 
                    asm_config = ipam.models.asm_config.ASMConfig(
                        asm_threshold = 56, 
                        enable = True, 
                        enable_notification = True, 
                        forecast_period = 56, 
                        growth_factor = 56, 
                        growth_type = 'percent', 
                        history = 56, 
                        min_total = 56, 
                        min_unused = 56, 
                        reenable_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    asm_scope_flag = 56, 
                    cidr = 1, 
                    comment = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    ddns_client_update = '', 
                    ddns_conflict_resolution_mode = '', 
                    ddns_domain = '', 
                    ddns_generate_name = True, 
                    ddns_generated_prefix = '', 
                    ddns_send_updates = True, 
                    ddns_ttl_percent = 1.337, 
                    ddns_update_on_renew = True, 
                    ddns_use_conflict_resolution = True, 
                    dhcp_config = ipam.models.dhcp_config.DHCPConfig(
                        abandoned_reclaim_time = 56, 
                        abandoned_reclaim_time_v6 = 56, 
                        allow_unknown = True, 
                        allow_unknown_v6 = True, 
                        echo_client_id = True, 
                        filters = [
                            ''
                            ], 
                        filters_v6 = [
                            ''
                            ], 
                        ignore_client_uid = True, 
                        ignore_list = [
                            ipam.models.ignore_item.IgnoreItem(
                                type = 'client_hex', 
                                value = '01:23:45:67:89:AB', )
                            ], 
                        lease_time = 56, 
                        lease_time_v6 = 56, ), 
                    dhcp_host = '', 
                    dhcp_options = [
                        ipam.models.option_item.OptionItem(
                            group = '', 
                            option_code = '', 
                            option_value = '', 
                            type = '', )
                        ], 
                    dhcp_utilization = ipam.models.dhcp_utilization.DHCPUtilization(
                        dhcp_free = '', 
                        dhcp_total = '', 
                        dhcp_used = '', ), 
                    disable_dhcp = True, 
                    discovery_attrs = ipam.models.discovery_attrs.discovery_attrs(), 
                    discovery_metadata = ipam.models.discovery_metadata.discovery_metadata(), 
                    header_option_filename = '', 
                    header_option_server_address = '', 
                    header_option_server_name = '', 
                    hostname_rewrite_char = '', 
                    hostname_rewrite_enabled = True, 
                    hostname_rewrite_regex = '', 
                    id = '', 
                    inheritance_assigned_hosts = [
                        ipam.models.assigned_host.AssignedHost(
                            display_name = '', 
                            host = '', 
                            ophid = '', )
                        ], 
                    inheritance_parent = '', 
                    inheritance_sources = ipam.models.dhcp_inheritance.DHCPInheritance(
                        ddns_client_update = ipam.models.inherited_string.InheritedString(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = '', ), 
                        ddns_conflict_resolution_mode = ipam.models.inherited_string.InheritedString(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = '', ), 
                        ddns_enabled = ipam.models.inherited_bool.InheritedBool(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = True, ), 
                        ddns_hostname_block = ipam.models.inherited_ddns_hostname_block.InheritedDDNSHostnameBlock(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = ipam.models.ddns_hostname_block.DDNSHostnameBlock(
                                ddns_generate_name = True, 
                                ddns_generated_prefix = '', ), ), 
                        ddns_ttl_percent = ipam.models.inherited_float.InheritedFloat(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        ddns_update_block = ipam.models.inherited_ddns_update_block.InheritedDDNSUpdateBlock(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        ddns_update_on_renew = ipam.models.inherited_bool.InheritedBool(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        ddns_use_conflict_resolution = , 
                        header_option_filename = , 
                        header_option_server_address = , 
                        header_option_server_name = , 
                        hostname_rewrite_block = ipam.models.inherited_hostname_rewrite_block.InheritedHostnameRewriteBlock(
                            action = '', 
                            display_name = '', 
                            source = '', ), ), 
                    name = '', 
                    parent = '', 
                    protocol = '', 
                    rebind_time = 56, 
                    renew_time = 56, 
                    space = '', 
                    tags = ipam.models.tags.tags(), 
                    threshold = ipam.models.utilization_threshold.UtilizationThreshold(
                        enabled = True, 
                        high = 100, 
                        low = 10, ), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    usage = [
                        ''
                        ], 
                    utilization = ipam.models.utilization.Utilization(
                        abandon_utilization = 56, 
                        abandoned = '', 
                        dynamic = '', 
                        free = '', 
                        static = '', 
                        total = '', 
                        used = '', ), 
                    utilization_v6 = ipam.models.utilization_v6.UtilizationV6(
                        abandoned = 'YQ==', 
                        dynamic = 'YQ==', 
                        static = 'YQ==', 
                        total = 'YQ==', 
                        used = 'YQ==', ), )
            )
        else:
            return ReadSubnetResponse(
        )
        """

    def testReadSubnetResponse(self):
        """Test ReadSubnetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
