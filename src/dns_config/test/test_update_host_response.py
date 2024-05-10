# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.models.update_host_response import UpdateHostResponse


class TestUpdateHostResponse(unittest.TestCase):
    """UpdateHostResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateHostResponse:
        """Test UpdateHostResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateHostResponse`
        """
        model = UpdateHostResponse()
        if include_optional:
            return UpdateHostResponse(
                result = dns_config.models.host.Host(
                    absolute_name = '', 
                    address = '', 
                    anycast_addresses = [
                        ''
                        ], 
                    associated_server = dns_config.models.config_host_associated_server.configHostAssociatedServer(
                        id = '', 
                        name = '', ), 
                    comment = '', 
                    current_version = '', 
                    dfp = True, 
                    dfp_service = '', 
                    id = '', 
                    inheritance_sources = dns_config.models.host_inheritance.HostInheritance(
                        kerberos_keys = dns_config.models.inherited_kerberos_keys.InheritedKerberosKeys(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = [
                                dns_config.models.kerberos_key.KerberosKey(
                                    algorithm = '', 
                                    domain = '', 
                                    key = 'keys/kerberos/23311109-fad4-448f-a7a7-55ad791ae7eb', 
                                    principal = '', 
                                    uploaded_at = '', 
                                    version = 56, )
                                ], ), ), 
                    kerberos_keys = [
                        dns_config.models.kerberos_key.KerberosKey(
                            algorithm = '', 
                            domain = '', 
                            key = 'keys/kerberos/23311109-fad4-448f-a7a7-55ad791ae7eb', 
                            principal = '', 
                            uploaded_at = '', 
                            version = 56, )
                        ], 
                    name = '', 
                    ophid = '', 
                    protocol_absolute_name = '', 
                    provider_id = '', 
                    server = '', 
                    site_id = '', 
                    tags = dns_config.models.tags.tags(), 
                    type = '', )
            )
        else:
            return UpdateHostResponse(
        )
        """

    def testUpdateHostResponse(self):
        """Test UpdateHostResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
