# coding: utf-8

"""
    BloxOne Anycast API

    Anycast capability enables HA (High Availability) configuration of BloxOne applications that run on equipment located on customer's premises (on-prem hosts). Anycast supports DNS, as well as DNS-forwarding services.  Anycast-enabled application setups use multiple on-premises installations for one particular application type. Multiple application instances are configured to use the same endpoint address. Anycast capability is collocated with such application instance, monitoring the local application instance and advertising to the upstream router (a customer equipment) a per-instance, local route to the common application endpoint address, as long as the local application instance is available. Depending on the type of the upstream router, the customer may configure local route advertisement via either BGP (Boarder Gateway Protocol) or OSPF (Open Shortest Path First) routing protocols. Both protocols may be enabled as well. Multiple routes to the common application service address provide redundancy without the need to reconfigure application clients.  Should an application instance become unavailable, the local route advertisements stop, resulting in withdrawal of the route (in the upstream router) to the application instance that has gone out of service and ensuring that subsequent application requests thus get routed to the remaining available application instances.  

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from anycast.models.onprem_host import OnpremHost


class TestOnpremHost(unittest.TestCase):
    """OnpremHost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnpremHost:
        """Test OnpremHost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnpremHost`
        """
        model = OnpremHost()
        if include_optional:
            return OnpremHost(
                anycast_config_refs = [
                    anycast.models.struct_anycast_configuration_reference.Struct anycast configuration reference(
                        anycast_config_name = '', 
                        routing_protocols = [BGP, OSPF], )
                    ],
                config_bgp = anycast.models.struct_bgp_configuration;_defines_bgp_configuration_for_one_anycast_enabled_on_prem_host.Struct BGP configuration; defines BGP configuration for one anycast-enabled on-prem host(
                    asn = 56, 
                    asn_text = '', 
                    fields = anycast.models.`field_mask`_represents_a_set_of_symbolic_field_paths,_for_example:.`FieldMask` represents a set of symbolic field paths, for example:(
                        paths = [
                            ''
                            ], ), 
                    holddown_secs = 56, 
                    keep_alive_secs = 56, 
                    link_detect = True, 
                    neighbors = [
                        anycast.models.struct_bgp_neighbor;_describes_one_of_the_bgp_neighbors_that_participate_in_bgp_configuration_for_one_anycast_enabled_on_prem_host.Struct BGP neighbor; describes one of the BGP neighbors that participate in BGP configuration for one anycast-enabled on-prem host(
                            asn = 56, 
                            asn_text = '', 
                            ip_address = '11.83.17.55', 
                            max_hop_count = 56, 
                            multihop = True, 
                            password = '', )
                        ], 
                    preamble = '', ),
                config_ospf = anycast.models.struct_ospf_configuration;_defines_ospf_configuration_for_one_anycast_enabled_on_prem_host.Struct OSPF configuration; defines OSPF configuration for one anycast-enabled on-prem host(
                    area = '0.0.0.1', 
                    area_type = '', 
                    authentication_key = '', 
                    authentication_key_id = 56, 
                    authentication_type = '', 
                    cost = 56, 
                    dead_interval = 56, 
                    hello_interval = 56, 
                    interface = 'eth0', 
                    preamble = '', 
                    retransmit_interval = 56, 
                    transmit_delay = 56, ),
                config_ospfv3 = anycast.models.struct_ospfv3_configuration;_defines_ospfv3_configuration_for_one_anycast_enabled_on_prem_host.Struct OSPFv3 configuration; defines OSPFv3 configuration for one anycast-enabled on-prem host(
                    area = '0.0.0.1', 
                    cost = 56, 
                    dead_interval = 56, 
                    hello_interval = 56, 
                    interface = 'eth0', 
                    retransmit_interval = 56, 
                    transmit_delay = 56, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                ip_address = '11.83.17.55',
                ipv6_address = '2607:f0d0:1002:0051:0000:0000:0000:0004',
                name = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return OnpremHost(
        )
        """

    def testOnpremHost(self):
        """Test OnpremHost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
