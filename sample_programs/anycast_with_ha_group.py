import logging
import sys
from typing import Optional

# Add source directory to the system path
sys.path.append("../src")

from anycast import OnPremAnycastManagerApi
from bloxone_client import ApiClient
from ipam.api import DhcpHostApi, HaGroupApi

from anycast.models import AnycastConfig
from ipam.models import HAGroup, ListHostResponse


def create_anycast_config(api_client: OnPremAnycastManagerApi, anycast_body: dict) -> Optional[AnycastConfig]:
    """
    Creates an anycast configuration.
    Args:
        api_client (OnPremAnycastManagerApi): API client instance for anycast management.
        anycast_body (dict): Configuration details for the anycast.

    Returns:
        Optional[AnycastConfig]: Created anycast configuration or None.
    """
    return api_client.create_anycast_config(body=anycast_body)


def create_ha_group_with_anycast(api_client: HaGroupApi, ha_group_body: dict) -> Optional[HAGroup]:
    """
    Creates an HA group with anycast.
    Args:
        api_client (HaGroupApi): API client for HA group management.
        ha_group_body (dict): Configuration details for the HA group.

    Returns:
        Optional[HAGroup]: Created HA group or None.
    """
    return api_client.create(body=ha_group_body)


def list_dhcp_hosts(api_client: DhcpHostApi) -> Optional[ListHostResponse]:
    """
    Lists all DHCP hosts.
    Args:
        api_client (DhcpHostApi): API client for DHCP host management.

    Returns:
        Optional[ListHostResponse]: List of DHCP hosts or None on failure.
    """
    try:
        return api_client.list()
    except Exception as e:
        logging.error(f"Failed to list DHCP hosts: {e}")
        return None


def sample_anycast():
    """
    Runs a sample Anycast configuration process.
    This function demonstrates creating an anycast configuration and linking it to an HA group.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Initialize API clients
    api_client = ApiClient()
    anycast_api_client = OnPremAnycastManagerApi(api_client)
    ha_group_api_client = HaGroupApi(api_client)
    dhcp_hosts_api_client = DhcpHostApi(api_client)

    # Maintain a record of created resources for cleanup
    resource_apis = {"ha_group": ha_group_api_client}
    resource_ids = []

    try:
        # Create an anycast configuration
        anycast_body = {
            "name": "anycast_example",
            "service": "DHCP",
            "anycast_ip_address": "192.2.2.35"
        }
        anycast_config_response = create_anycast_config(anycast_api_client, anycast_body)

        if anycast_config_response:
            resource_ids.append(("on_prem_anycast_manager", anycast_config_response.results.id))
            logging.info("Anycast config created successfully.")

        # List DHCP hosts
        dhcp_hosts = list_dhcp_hosts(dhcp_hosts_api_client)
        if not dhcp_hosts or len(dhcp_hosts.results) < 2:
            raise Exception("Not enough DHCP hosts found.")

        # Create an HA group with the anycast configuration
        ha_group_body = {
            "name": "example_ha_group",
            "mode": "anycast",
            "hosts": [
                {"host": dhcp_hosts.results[0].id, "role": "active"},
                {"host": dhcp_hosts.results[1].id, "role": "passive"}
            ],
            "anycast_config_id": f"accm/ac_configs/{anycast_config_response.results.id}"
        }
        ha_group_with_anycast_response = create_ha_group_with_anycast(ha_group_api_client, ha_group_body)

        if ha_group_with_anycast_response:
            resource_ids.append(("ha_group", ha_group_with_anycast_response.result.id))
            logging.info("HA group created successfully.")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        # Clean up created resources
        if resource_ids and resource_ids[1][1]:
            ha_group_api_client.delete(resource_ids[1][1])
            logging.info("HA group deleted successfully.")
        if resource_ids and resource_ids[0][1]:
            anycast_api_client.delete_anycast_config(resource_ids[0][1])
            logging.info("Anycast config deleted successfully.")


if __name__ == "__main__":
    sample_anycast()
