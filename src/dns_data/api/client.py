from bloxone_client import ApiClient
import dns_data as api

class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.records_api = api.RecordApi(self.APIClient)