# coding: utf-8

"""
    DNS Data API

    The DNS Data is a BloxOne DDI service providing primary authoritative zone support. DNS Data is authoritative for all DNS resource records and is acting as a primary DNS server. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_data.models.create_record_response import CreateRecordResponse


class TestCreateRecordResponse(unittest.TestCase):
    """CreateRecordResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRecordResponse:
        """Test CreateRecordResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRecordResponse`
        """
        model = CreateRecordResponse()
        if include_optional:
            return CreateRecordResponse(
                result = dns_data.models.record.Record(
                    absolute_name_spec = '', 
                    absolute_zone_name = '', 
                    comment = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    delegation = '', 
                    disabled = True, 
                    dns_absolute_name_spec = '', 
                    dns_absolute_zone_name = '', 
                    dns_name_in_zone = '', 
                    dns_rdata = '', 
                    id = '', 
                    inheritance_sources = dns_data.models.record_inheritance.RecordInheritance(
                        ttl = dns_data.models.inherited_u_int32.InheritedUInt32(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = 56, ), ), 
                    ipam_host = '', 
                    name_in_zone = '', 
                    options = dns_data.models.options.options(), 
                    provider_metadata = dns_data.models.provider_metadata.provider_metadata(), 
                    rdata = {"address":"10.0.0.0"}, 
                    source = [
                        ''
                        ], 
                    subtype = '', 
                    tags = dns_data.models.tags.tags(), 
                    ttl = 56, 
                    type = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    view = '', 
                    view_name = '', 
                    zone = '', )
            )
        else:
            return CreateRecordResponse(
        )
        """

    def testCreateRecordResponse(self):
        """Test CreateRecordResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
