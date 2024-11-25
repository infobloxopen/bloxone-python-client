from bloxone_client import ApiClient
import dns_config.api as api


class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.acl_api = api.AclApi(self.APIClient)
        self.auth_nsg_api = api.AuthNsgApi(self.APIClient)
        self.auth_zone_api = api.AuthZoneApi(self.APIClient)
        self.cache_flush_api = api.CacheFlushApi(self.APIClient)
        self.convert_domain_name_api = api.ConvertDomainNameApi(self.APIClient)
        self.convert_rname_api = api.ConvertRnameApi(self.APIClient)
        self.delegation_api = api.DelegationApi(self.APIClient)
        self.forward_nsg_api = api.ForwardNsgApi()
        self.forward_zone_api = api.ForwardZoneApi(self.APIClient)
        self.global_api = api.GlobalApi(self.APIClient)
        self.host_api = api.HostApi(self.APIClient)
        self.lbdn_api = api.LbdnApi(self.APIClient)
        self.server_api = api.ServerApi(self.APIClient)
        self.view_api = api.ViewApi(self.APIClient)