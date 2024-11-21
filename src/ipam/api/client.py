from bloxone_client import ApiClient
import ipam.api as api


class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.address_api=api.AddressApi(self.APIClient)
        self.address_block_api=api.AddressBlockApi(self.APIClient)
        self.asm_api=api.AsmApi(self.APIClient)
        self.dhcp_host_api=api.DhcpHostApi(self.APIClient)
        self.dns_usage_api=api.DnsUsageApi(self.APIClient)
        self.filter_api=api.FilterApi(self.APIClient)
        self.fixed_address_api=api.FixedAddressApi(self.APIClient)
        self.global_api=api.GlobalApi(self.APIClient)
        self.ha_group_api=api.HaGroupApi(self.APIClient)
        self.hardware_filter_api=api.HardwareFilterApi(self.APIClient)
        self.ip_space_api=api.IpSpaceApi(self.APIClient)
        self.ipam_host_api=api.IpamHostApi(self.APIClient)
        self.leases_command_api=api.LeasesCommandApi(self.APIClient)
        self.option_code_api=api.OptionCodeApi(self.APIClient)
        self.option_filter_api=api.OptionFilterApi(self.APIClient)
        self.option_group_api=api.OptionGroupApi(self.APIClient)
        self.option_space_api=api.OptionSpaceApi(self.APIClient)
        self.range_api=api.RangeApi(self.APIClient)
        self.server_api=api.ServerApi(self.APIClient)
        self.subnet_api=api.SubnetApi(self.APIClient)
       