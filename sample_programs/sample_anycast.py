import sys
sys.path.append("../src")
import logging

import anycast.models as models
from anycast.api import NewApiClient as AnycastApiClient
from ipam.api import HaGroupApi 
from typing import List, Optional
from ipam.api import NewApiClient as IpamApiClient

from anycast.models import (
     AnycastConfig,
)
from ipam.models import (
    HAGroup,
    HAGroupHost,
    ListHostResponse,
)

from infra_mgmt.api import hosts_api

def create_anycast_config(api_client:AnycastApiClient,name:str,service:str,anycast_ip_address:str)-> Optional[AnycastConfig]:
     """Creates anycast config"""
     return api_client.on_prem_anycast_manager_api.create_anycast_config(
          body=AnycastConfig(name=name,service=service,anycast_ip_address=anycast_ip_address)
     )

def create_ha_group_with_anycast(api_client:IpamApiClient,name:str,mode:str,anycast_config_id:str,hosts:List[HAGroupHost])-> Optional[HAGroup]:
    """Creates a HA Group with anycast"""
    return api_client.ha_group_api.create(
        body=HAGroup(name=name,mode=mode,anycast_config_id=anycast_config_id,hosts=hosts)
    )


def list_dhcp_hosts(api_client:IpamApiClient)->Optional[ListHostResponse]:
    return api_client.dhcp_host_api.list()


def get_infra_host():
    return hosts_api.HostsApi.list()




# def cleanup_resources(api_client: AnycastApiClient, resource_ids: list):
#     # """Deletes created resources for cleanup."""
#     # resource_ids.reverse()
#     # for resource_type, resource_id in resource_ids:
#     #     try:
#     #         getattr(api_client, f"{resource_type}_api").delete(resource_id)
#     #         logging.info(f"Deleted {resource_type} with ID: {resource_id}")
#     #     except Exception as e:
#     #         logging.error(f"Failed to delete {resource_type} with ID {resource_id}: {e}")
#     api_client.on_prem_anycast_manager_api.delete_anycast_config()


def sample_anycast():
    """Runs a sample Anycast configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    anycast_api_client = AnycastApiClient()
    ipam_api_client=IpamApiClient()

    resource_ids = []

    try:
        anycast_config_response=create_anycast_config(anycast_api_client,"anycast_example","DHCP","192.2.2.1")
        if anycast_config_response: 
            resource_ids.append(("on_prem_anycast_manager", anycast_config_response.results.id))
            logging.info("Anycast config created successfully")


        dhcp_hosts=list_dhcp_hosts(ipam_api_client)


        host1=HAGroupHost(host=dhcp_hosts.results[0].id,role="active")
        host2=HAGroupHost(host=dhcp_hosts.results[1].id,role="passive")

        ha_group_with_anycast_response=create_ha_group_with_anycast(ipam_api_client,"example_ha_group_anycast","anycast",f"accm/ac_configs/{anycast_config_response.results.id}",[host1,host2])

        if ha_group_with_anycast_response:
            logging.info("HA group created successfully")


        if anycast_config_response is not None:
            print(type(anycast_config_response.results.id))
            anycast_api_client.on_prem_anycast_manager_api.delete_anycast_config(anycast_config_response.results.id)

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    # finally:
    #     cleanup_resources(anycast_api_client, resource_ids)



if __name__ == "__main__":
    sample_anycast()
