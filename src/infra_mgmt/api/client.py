from bloxone_client import ApiClient
import infra_mgmt.api as api

class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.details_api = api.DetailApi(self.APIClient)
        self.hosts_api = api.HostsApi(self.APIClient)
        self.services_api = api.ServicesApi(self.APIClient)