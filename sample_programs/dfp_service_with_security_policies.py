import sys

sys.path.append("../src")
import logging
from typing import Optional
from datetime import datetime, timedelta
import random


from bloxone_client import ApiClient
from dfp.api import InfraServicesApi
from fw.api import AccessCodesApi , InternalDomainListsApi , NamedListsApi , SecurityPoliciesApi
from infra_mgmt import HostsApi , Service ,ServicesApi
from fw.models import InternalDomainsDeleteRequest, InternalDomains , AccessCode , NamedList , SecurityPolicy
from dfp.models import Dfp


from auth_zone_with_records import cleanup_resources

def filter_infra_host(api_client , filter):
    return api_client.list(filter=filter)


def create_infra_service(api_client,infra_service_body)-> Optional[Service]:
    """get an infra sservice list."""
    infra_service_response = api_client.create(body = infra_service_body)
    return infra_service_response

def create_dfp_service(api_client,payload_service_id,dfp_service_body)-> Optional[Dfp]:
    """get an infra sservice list."""
    dfp_service_response = (api_client.
                            create_or_update_dfp_service(body = dfp_service_body ,
                                                         payload_service_id = payload_service_id))
    return dfp_service_response

def create_internal_domain_list(
        api_client: InternalDomainListsApi, body) -> Optional[InternalDomains]:
    """Creates an internal domain list."""
    return api_client.create_internal_domains(
        body=body
    )

def create_access_code(
        api_client: AccessCodesApi ,access_code_body) -> Optional[AccessCode]:
    """Creates an access code."""
    return api_client.create_access_code(
        body=access_code_body
    )

def create_named_list(
        api_client: NamedListsApi ,named_list_body) -> Optional[NamedList]:
    """Creates a named list."""
    return api_client.named_lists_api.create_named_list(
        body=named_list_body
    )

def create_security_policy(
        api_client: SecurityPoliciesApi ,security_policy_body) -> Optional[SecurityPolicy]:
    """Creates a security policy."""
    return api_client.create_security_policy(
        body=security_policy_body
    )


# def delete_internal_domain_list(
#         fw_client: FwApiClient, domain_list_id: str
# ):
#     """Deletes an internal domain list."""
#     try:
#         delete_response = fw_client.internal_domain_lists_api.delete_internal_domains(
#             body=InternalDomainsDeleteRequest(ids=[domain_list_id])
#         )
#         logging.info(f"Deleted internal domain list with ID: {domain_list_id}")
#         return delete_response
#     except Exception as e:
#         logging.error(f"Failed to delete internal domain list with ID {domain_list_id}: {e}")


def sample_dfp():
    """Runs a sample DFP configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    api_client = ApiClient()

    infra_host_api  = HostsApi(api_client)
    infra_service_api = ServicesApi(api_client)
    access_codes_api = AccessCodesApi(api_client)
    internal_domain_lists_api = InternalDomainListsApi(api_client)
    named_lists_api = NamedListsApi(api_client)
    security_policies_api = SecurityPoliciesApi(api_client)
    dfp_service_api = InfraServicesApi(api_client)
    resource_ids = []

    resource_apis = {
        "infra_service": infra_service_api,
        "internal_domain_lists": internal_domain_lists_api,
        "dfp_service": dfp_service_api ,
        "access_codes": access_codes_api,
        "named_lists": named_lists_api,
        "security_policies": security_policies_api,
    }

    try:

        infra_host_response = filter_infra_host(infra_host_api ,filter="display_name==\"TF_TEST_HOST_01\"")

        if len(infra_host_response.results) == 0:
            raise Exception("No infra hosts found")

        infra_service_body = {
            "name": "DFP Service",
            "description": "Example infra service",
            "pool_id": infra_host_response.results[0].pool_id,
            "service_type": "dfp",
            "desired_state": "start",
            "wait_for_state": False
        }

        infra_service_response = create_infra_service(infra_service_api,infra_service_body)
        if infra_service_response:
            logging.info("Infra Service created Enabled on the Host")
            resource_ids.append(("infra_service", infra_service_response.result.id))


        random_number = random.randint(10000, 99999)
        internal_domain_lists_body = {
            "name": f"example_domain_list-{random_number}",
            "internal_domains": ["example.com"],
        }

        internal_domain_list_response = create_internal_domain_list(
            internal_domain_lists_api, internal_domain_lists_body
        )
        if internal_domain_list_response:
            resource_ids.append(("internal_domain_list", internal_domain_list_response.results.id))
            logging.info("Internal domain list created successfully")


        dfp_service_body  = {
            "service_id" : infra_service_response.result.id,
            "pool_id": infra_host_response.results[0].pool_id,
            "resolvers_all": [
                {
                    "address": "1.1.1.1",
                    "is_fallback": True,
                    "is_local": False,
                    "protocols": ["DO53"]
                }
            ]
        }

        dfp_service_response = create_dfp_service(dfp_service_api,infra_service_response.result.id,dfp_service_body)
        if dfp_service_response:
            logging.info("DFP Service created on the Host")
            resource_ids.append(("infra_service", dfp_service_response.results.id))


        named_list_body = {
            "name": "example_named_list",
            "items_described": [
                {
                    "item": "pc-domain.com",
                    "description": "Example Domain"
                }
            ],
            "type": "custom_list"
        }

        named_list_response = create_named_list(named_lists_api, named_list_body)

        if named_list_response:
            resource_ids.append(("named_list", named_list_response.results.id))
            logging.info("Named list created successfully")

        current_timestamp = datetime.now()

        access_code_body = {
            "name": "example_access_code",
            # Get Timestamp

            "activation": current_timestamp,
            "expiration": current_timestamp + timedelta(hours=24)
            ,
            "rules": [
                {
                    "data": named_list_response.results.name,
                    "type": named_list_response.results.type
                }
            ],
            "description": "Example Access Code"
        }


        access_code_response = create_access_code(
            access_codes_api, access_code_body
        )

        if access_code_response:
            resource_ids.append(("access_code", access_code_response.result.id))
            logging.info("Access code created successfully")

        security_policy_body = {
            "name": "example_security_policy",
            "rules": [
                {
                    "action": "action_allow",
                    "data": named_list_response.result.name,
                    "type": named_list_response.result.type
                }
            ],
            "description": "Example Security Policy",
            "dfps": [
                dfp_service_response.results.id
            ],
            "ecs": True,
            "onprem_resolve": True,
            "safe_search": False,
            "tags": {
                "site": "Site A"
            },
            "access_codes": [
                access_code_response.result.id
            ]
        }

        security_policy_response = create_security_policy(
            security_policies_api, security_policy_body
        )

        if security_policy_response:
            resource_ids.append(("security_policy", security_policy_response.result.id))
            logging.info("Security policy created successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        cleanup_resources(resource_apis, resource_ids)


if __name__ == "__main__":
    sample_dfp()