from bloxone_client import ApiClient
import dfp.api as api

class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.accounts_api = api.AccountsApi(self.APIClient)
        self.infra_service_api = api.InfraServicesApi(self.APIClient)