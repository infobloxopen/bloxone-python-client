import string
import sys

sys.path.append("../src")
import logging
import random

from bloxone_client import ApiClient
import anycast.models as models
from ipam.api import HaGroupApi
from typing import List, Optional
from anycast import OnPremAnycastManagerApi
from ipam import HaGroupApi , DhcpHostApi
from infra_mgmt import HostsApi
from auth_zone_with_records import cleanup_resources

from anycast.models import (
    AnycastConfig,
)
from ipam.models import (
    HAGroup,
    HAGroupHost,
    ListHostResponse,
)

from infra_mgmt.api import hosts_api

def create_anycast_config(api_client,anycast_body:dict)-> Optional[AnycastConfig]:
    """Creates anycast config"""
    return api_client.create_anycast_config(
        body=anycast_body
    )

def create_ha_group_with_anycast(api_client:HaGroupApi,ha_group_body)-> Optional[HAGroup]:
    """Creates a HA Group with anycast"""
    return api_client.create(
        body= ha_group_body
    )


def list_dhcp_hosts(api_client:DhcpHostApi)->Optional[ListHostResponse]:
    try:
        return api_client.list()
    except Exception as e:
        logging.error(f"Failed to list dhcp hosts: {e}")
        return None

def get_infra_host():
    return hosts_api.HostsApi.list()


def sample_anycast():
    """Runs a sample Anycast configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    api_client  = ApiClient()
    anycast_api_client = OnPremAnycastManagerApi(api_client)
    ha_group_api_client=HaGroupApi(api_client)
    dhcp_hosts_api_client = DhcpHostApi(api_client)
    resource_apis = {
        #"on_prem_anycast_manager": anycast_api_client,
        "ha_group": ha_group_api_client
    }


    resource_ids = []

    try:
        anycast_body = {
            "name": f"anycast_example-{random.choices(string.digits,k=4)}",
            "service": "DHCP",
            "anycast_ip_address": f"192.2.2.35"
        }
        anycast_config_response=create_anycast_config(anycast_api_client,anycast_body)
        if anycast_config_response:
            resource_ids.append(("on_prem_anycast_manager", f"accm/ac_configs/{anycast_config_response.results.id}"))
            logging.info("Anycast config created successfully")



        dhcp_hosts=list_dhcp_hosts(dhcp_hosts_api_client)

        if len(dhcp_hosts.results) < 2:
            raise Exception("Enough DHCP hosts not found")

        ha_group_body = {
            "name": "example_ha_group",
            "mode": "anycast",
            "hosts": [
                {
                    "host": dhcp_hosts.results[0].id,
                    "role": "active"
                },
                {
                    "host": dhcp_hosts.results[1].id,
                    "role": "passive"
                }
            ],
            "anycast_config_id": f"accm/ac_configs/{anycast_config_response.results.id}"

        }
        ha_group_with_anycast_response=create_ha_group_with_anycast(ha_group_api_client, ha_group_body)

        if ha_group_with_anycast_response:
            logging.info("HA group created successfully")
            resource_ids.append(("ha_group", ha_group_with_anycast_response.result.id))


        if anycast_config_response is not None:
            print(type(anycast_config_response.results.id))

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        cleanup_resources(resource_apis, resource_ids)
        if resource_ids[0][1]:
            anycast_api_client.delete_anycast_config(resource_ids[0][1])



if __name__ == "__main__":
    sample_anycast()