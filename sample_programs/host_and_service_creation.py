import sys



sys.path.append("../src")

import logging
from typing import Optional

from auth_zone_with_records import cleanup_resources

from bloxone_client import ApiClient

from ipam import  IpSpaceApi

from infra_mgmt import  HostsApi , ServicesApi

from ipam.models import  IPSpace

from infra_mgmt.models import Host , Service

from subnet_with_dhcp_options import create_ip_space

from auth_zone_with_records import cleanup_resources

def create_infra_host(api_client: HostsApi, body) -> Optional[Host]:

    return api_client.create(body=body)

def create_infra_service(api_client: ServicesApi, body) -> Optional[Service]:

    return api_client.create(body=body)


def host_with_services_creation():

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    api_client = ApiClient()

    ip_space_api = IpSpaceApi(api_client)
    host_api = HostsApi(api_client)
    service_api = ServicesApi(api_client)

    resource_ids = []
    resource_apis = {
        "ip_space": ip_space_api,
        "host": host_api,
        "service": service_api
    }

    try:

        ip_space_body = {
            "name": "example_space1",
            "comment": "Space for Sample Example Program"
        }

        ip_space_response = create_ip_space(ip_space_api, ip_space_body)

        if ip_space_response:
            logging.info("IP Space is created successfully")
            resource_ids.append(("ip_space", ip_space_response.result.id))

        host_body = {
            "display_name": "example_python_client_host",
            "space": ip_space_response.result.id
        }


        infra_host_response = create_infra_host(host_api, host_body)

        if infra_host_response:
            logging.info("Host is created successfully")
            resource_ids.append(("host", infra_host_response.result.id))

        infra_service_body_dns  = {
            "name": "example_infra_service_dns",
            "description": "Example DNS service",
            "pool_id": infra_host_response.result.pool_id,
            "service_type": "dns",
            "desired_state": "start",
            "wait_for_state": False
        }

        infra_service_response_dns = create_infra_service(service_api,infra_service_body_dns)

        if infra_service_response_dns:
            logging.info("DNS Service created Enabled on the Host")
            resource_ids.append(("service", infra_service_response_dns.result.id))

        infra_service_body_dhcp  = {
            "name": "example_infra_service_dhcp",
            "description": "Example DHCP service",
            "pool_id": infra_host_response.result.pool_id,
            "service_type": "dhcp",
            "desired_state": "start",
        }

        infra_service_response_dhcp = create_infra_service(service_api,infra_service_body_dhcp)

        if infra_service_response_dhcp:
            logging.info("DHCP Service created Enabled on the Host")
            resource_ids.append(("service", infra_service_response_dhcp.result.id))


    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        print("done")
        #cleanup_resources(resource_apis,resource_ids)

if __name__ == "__main__":
    host_with_services_creation()
