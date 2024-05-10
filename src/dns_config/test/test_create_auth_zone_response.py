# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.models.create_auth_zone_response import CreateAuthZoneResponse


class TestCreateAuthZoneResponse(unittest.TestCase):
    """CreateAuthZoneResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAuthZoneResponse:
        """Test CreateAuthZoneResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAuthZoneResponse`
        """
        model = CreateAuthZoneResponse()
        if include_optional:
            return CreateAuthZoneResponse(
                result = dns_config.models.auth_zone.AuthZone(
                    comment = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    disabled = True, 
                    external_primaries = [
                        dns_config.models.external_primary.ExternalPrimary(
                            address = '', 
                            fqdn = '', 
                            nsg = '', 
                            protocol_fqdn = '', 
                            tsig_enabled = True, 
                            tsig_key = dns_config.models.tsig_key.TSIGKey(
                                algorithm = '', 
                                comment = '', 
                                key = '', 
                                name = '', 
                                protocol_name = '', 
                                secret = '', ), 
                            type = 'nsg', )
                        ], 
                    external_providers = [
                        dns_config.models.external_provider.ExternalProvider(
                            id = '', 
                            name = '', 
                            type = '', )
                        ], 
                    external_secondaries = [
                        dns_config.models.external_secondary.ExternalSecondary(
                            address = '192.0.2.0', 
                            fqdn = 'ns1.example.com', 
                            protocol_fqdn = '', 
                            stealth = True, 
                            tsig_enabled = True, )
                        ], 
                    fqdn = '', 
                    gss_tsig_enabled = True, 
                    id = '', 
                    inheritance_assigned_hosts = [
                        dns_config.models.assigned_host.AssignedHost(
                            display_name = '', 
                            host = '', 
                            ophid = '', )
                        ], 
                    inheritance_sources = dns_config.models.config_auth_zone_inheritance.configAuthZoneInheritance(
                        gss_tsig_enabled = dns_config.models.inherited_bool.InheritedBool(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = True, ), 
                        notify = dns_config.models.inherited_bool.InheritedBool(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = True, ), 
                        query_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = [
                                dns_config.models.acl_item.ACLItem(
                                    access = 'allow', 
                                    acl = '', 
                                    address = '', 
                                    element = 'ip', )
                                ], ), 
                        transfer_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        update_acl = , 
                        use_forwarders_for_subzones = , 
                        zone_authority = dns_config.models.inherited_zone_authority.InheritedZoneAuthority(
                            default_ttl = dns_config.models.inherited_u_int32.InheritedUInt32(
                                action = '', 
                                display_name = '', 
                                source = '', ), 
                            expire = dns_config.models.inherited_u_int32.InheritedUInt32(
                                action = '', 
                                display_name = '', 
                                source = '', ), 
                            mname_block = dns_config.models.inherited_authority_m_name_block.InheritedAuthorityMNameBlock(
                                action = '', 
                                display_name = '', 
                                source = '', ), 
                            negative_ttl = , 
                            protocol_rname = dns_config.models.inherited_string.InheritedString(
                                action = '', 
                                display_name = '', 
                                source = '', ), 
                            refresh = , 
                            retry = , 
                            rname = dns_config.models.inherited_string.InheritedString(
                                action = '', 
                                display_name = '', 
                                source = '', ), ), ), 
                    initial_soa_serial = 56, 
                    internal_secondaries = [
                        dns_config.models.internal_secondary.InternalSecondary(
                            host = 'dns/host/23311109-fad4-448f-a7a7-55ad791ae7eb', )
                        ], 
                    mapped_subnet = '', 
                    mapping = '', 
                    notify = True, 
                    nsgs = [
                        ''
                        ], 
                    parent = '', 
                    primary_type = '', 
                    protocol_fqdn = '', 
                    query_acl = [
                        dns_config.models.acl_item.ACLItem(
                            access = 'allow', 
                            acl = '', 
                            address = '', 
                            element = 'ip', )
                        ], 
                    tags = dns_config.models.tags.tags(), 
                    transfer_acl = [
                        
                        ], 
                    update_acl = [
                        
                        ], 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    use_forwarders_for_subzones = True, 
                    view = '', 
                    warnings = [
                        dns_config.models.warning.Warning(
                            message = '', 
                            name = '', )
                        ], 
                    zone_authority = dns_config.models.zone_authority.ZoneAuthority(
                        mname = '', 
                        protocol_mname = '', 
                        use_default_mname = True, ), )
            )
        else:
            return CreateAuthZoneResponse(
        )
        """

    def testCreateAuthZoneResponse(self):
        """Test CreateAuthZoneResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
