from bloxone_client import ApiClient
import fw.api as api

class NewApiClient :
    def __init__(self):
        self.APIClient = ApiClient.new_api_client(self)
        self.access_codes_api = api.AccessCodesApi(self.APIClient)
        self.app_approvals_api = api.AppApprovalsApi(self.APIClient)
        self.application_filters_api = api.ApplicationFiltersApi(self.APIClient)
        self.category_filters_api = api.CategoryFiltersApi(self.APIClient)
        self.content_categories_api = api.ContentCategoriesApi(self.APIClient)
        self.internal_domain_lists_api = api.InternalDomainListsApi(self.APIClient)
        self.named_list_api = api.NamedListsApi(self.APIClient)
        self.named_list_items_api = api.NamedListItemsApi(self.APIClient)
        self.network_lists_api = api.NetworkListsApi(self.APIClient)
        self.pop_regions_api = api.PopRegionsApi(self.APIClient)
        self.security_policies_api = api.SecurityPoliciesApi(self.APIClient)
        self.security_policy_rules_api = api.SecurityPolicyRulesApi(self.APIClient)
        self.threat_feeds_api = api.ThreatFeedsApi(self.APIClient)


