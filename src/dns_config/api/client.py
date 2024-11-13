from bloxone_client import ApiClient
from dns_config.api import AclApi , AuthNsgApi , AuthZoneApi , CacheFlushApi , ConvertDomainNameApi , ConvertRnameApi , DelegationApi , ForwardNsgApi , ForwardZoneApi , GlobalApi , HostApi , LbdnApi , ServerApi , ViewApi



class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.acl_api = AclApi(self.APIClient)
        self.auth_nsg_api = AuthNsgApi(self.APIClient)
        self.auth_zone_api = AuthZoneApi(self.APIClient)
        self.cache_flush_api = CacheFlushApi(self.APIClient)
        self.convert_domain_name_api = ConvertDomainNameApi(self.APIClient)
        self.convert_rname_api = ConvertRnameApi(self.APIClient)
        self.delegation_api = DelegationApi(self.APIClient)
        self.forward_nsg_api = ForwardNsgApi()
        self.forward_zone_api = ForwardZoneApi(self.APIClient)
        self.global_api = GlobalApi(self.APIClient)
        self.host_api = HostApi(self.APIClient)
        self.lbdn_api = LbdnApi(self.APIClient)
        self.server_api = ServerApi(self.APIClient)
        self.view_api = ViewApi(self.APIClient)