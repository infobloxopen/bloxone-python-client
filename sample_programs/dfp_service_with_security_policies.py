import sys
sys.append("../src")
import logging
from typing import Optional


from bloxone_client import ApiClient
from dfp.api import InfraServicesApi
from fw.api import AccessCodesApi , InternalDomainListsApi , NamedListsApi , SecurityPoliciesApi
from infra_mgmt.api import HostsApi
from fw.models import InternalDomainsDeleteRequest, InternalDomains
from dfp.models import DfpCreateOrUpdatePayload

from anycast_with_ha_group import get_infra_host

def filter_infra_host(api_client , filter):
    return api_client.list(filter=filter)


def create_infra_service(api_client,infra_service_body)-> Optional[InfraService]:
    """get an infra sservice list."""
    infra_service_response = api_client.create(body = infra_service_body)
    return infra_service_response.results


def create_internal_domain_list(
        fw_client: FwApiClient, name: str, domains: list, comment: str
) -> Optional[InternalDomains]:
    """Creates an internal domain list."""
    return fw_client.internal_domain_lists_api.create_internal_domains(
        body=InternalDomains(name=name, internal_domains=domains)
    )


def create_dfp_service(
        dfp_client: DfpApiClient, service_id: str, domain_list_id: str, comment: str
) -> Optional[DfpCreateOrUpdatePayload]:
    """Creates or updates a DFP service."""
    return dfp_client.infra_service_api.create_or_update_dfp_service(
        payload_service_id=service_id,
        body=DfpCreateOrUpdatePayload(internal_domain_lists=[domain_list_id])
    )


def delete_internal_domain_list(
        fw_client: FwApiClient, domain_list_id: str
):
    """Deletes an internal domain list."""
    try:
        delete_response = fw_client.internal_domain_lists_api.delete_internal_domains(
            body=InternalDomainsDeleteRequest(ids=[domain_list_id])
        )
        logging.info(f"Deleted internal domain list with ID: {domain_list_id}")
        return delete_response
    except Exception as e:
        logging.error(f"Failed to delete internal domain list with ID {domain_list_id}: {e}")


def sample_dfp():
    """Runs a sample DFP configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    api_client = ApiClient()

    infra_host_api  = HostsApi(api_client)
    access_codes_api = AccessCodesApi(api_client)
    internal_domain_lists_api = InternalDomainListsApi(api_client)
    named_lists_api = NamedListsApi(api_client)
    security_policies_api = SecurityPoliciesApi(api_client)
    dfp_service_api = InfraServicesApi(api_client)
    resource_ids = []

    try:

        infra_host_response = filter_infra_host(infra_host_api ,filter="display_name==\"TF_TEST_HOST_01\"")

        if len(infra_host_response.results) == 0:
            raise Exception("No infra hosts found")

        # Step 1: Get Infra service information

        infra_service_body  = {
            "name": "example_infra_service",
            "description": "Example infra service",
            "pool_id": infra_host_response.results[0].pool_id,
            "service_type": "DFP",
            "desired_state": "start",
        }

        dfp_service_response = create_infra_service(dfp_service_api,infra_service_body)
        if dfp_service_response:
            logging.info("DFP Service created Enabled on the Host")
            resource_ids.append(("infra_service", dfp_service_response.results.id))

        # Step 2: Create internal domain list
        internal_domain_list_response = create_internal_domain_list(
            fw_client, "example_internal_domain_list_test1", ["example.domain.com"], "Internal domain list created"
        )
        if internal_domain_list_response:
            resource_ids.append(("internal_domain_list", internal_domain_list_response.results.id))
            logging.info("Internal domain list created successfully")

        # Step 3: Create or update DFP service
        service_id = infra_service_response[0].id
        dfp_service_response = create_dfp_service(
            dfp_client, service_id, internal_domain_list_response.results.id, "DFP service created or updated"
        )
        if dfp_service_response:
            logging.info("DFP service created or updated successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        delete_internal_domain_list(fw_client,internal_domain_list_response.results.id)


if __name__ == "__main__":
    sample_dfp()