from bloxone_client import ApiClient
import anycast.api as api


class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.on_prem_anycast_manager_api=api.OnPremAnycastManagerApi(self.APIClient)