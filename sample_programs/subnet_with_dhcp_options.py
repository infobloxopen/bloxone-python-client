import sys
import logging
from typing import Optional

# Add source directory to the system path
sys.path.append("../src")

from auth_zone_with_records import cleanup_resources
from bloxone_client import ApiClient
from ipam import SubnetApi, IpSpaceApi, OptionSpaceApi, OptionGroupApi, OptionCodeApi
from ipam.models import Subnet, IPSpace, OptionSpace, OptionGroup, OptionCode


def create_ip_space(api_client: IpSpaceApi, body: dict) -> Optional[IPSpace]:
    """
    Creates an IP space.
    Args:
        api_client (IpSpaceApi): API client for IP space management.
        body (dict): Configuration details for the IP space.

    Returns:
        Optional[IPSpace]: Created IP space or None.
    """
    return api_client.create(body=body)


def create_subnet(api_client: SubnetApi, body: dict) -> Optional[Subnet]:
    """
    Creates a subnet.
    Args:
        api_client (SubnetApi): API client for subnet management.
        body (dict): Configuration details for the subnet.

    Returns:
        Optional[Subnet]: Created subnet or None.
    """
    return api_client.create(body=body)


def create_option_space(api_client: OptionSpaceApi, body: dict) -> Optional[OptionSpace]:
    """
    Creates an option space.
    Args:
        api_client (OptionSpaceApi): API client for option space management.
        body (dict): Configuration details for the option space.

    Returns:
        Optional[OptionSpace]: Created option space or None.
    """
    return api_client.create(body=body)


def create_option_group(api_client: OptionGroupApi, body: dict) -> Optional[OptionGroup]:
    """
    Creates an option group.
    Args:
        api_client (OptionGroupApi): API client for option group management.
        body (dict): Configuration details for the option group.

    Returns:
        Optional[OptionGroup]: Created option group or None.
    """
    return api_client.create(body=body)


def create_option_code(api_client: OptionCodeApi, body: dict) -> Optional[OptionCode]:
    """
    Creates an option code.
    Args:
        api_client (OptionCodeApi): API client for option code management.
        body (dict): Configuration details for the option code.

    Returns:
        Optional[OptionCode]: Created option code or None.
    """
    return api_client.create(body=body)


def subnet_with_dhcp_options():
    """
    Demonstrates the creation of a subnet with DHCP options, linking it to
    option groups, option spaces, and IP spaces.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Initialize API clients
    api_client = ApiClient()
    ip_space_api = IpSpaceApi(api_client)
    option_group_api = OptionGroupApi(api_client)
    option_space_api = OptionSpaceApi(api_client)
    option_code_api = OptionCodeApi(api_client)
    subnet_api = SubnetApi(api_client)

    # Maintain resource identifiers for cleanup
    resource_ids = []
    resource_apis = {
        "ip_space": ip_space_api,
        "subnet": subnet_api,
        "option_group": option_group_api,
        "option_space": option_space_api,
        "option_code": option_code_api
    }

    try:
        # Create an IP space
        ip_space_body = {
            "name": "example_space_python_client",
            "comment": "Space for Sample Example Program"
        }
        ip_space_response = create_ip_space(ip_space_api, ip_space_body)

        if ip_space_response:
            logging.info("IP Space is created successfully.")
            resource_ids.append(("ip_space", ip_space_response.result.id))

        # Create an option group
        option_group_body = {
            "name": "example_option_group",
            "type": "ip4"
        }
        option_group_response = create_option_group(option_group_api, option_group_body)

        if option_group_response:
            logging.info("Option Group is created successfully.")
            resource_ids.append(("option_group", option_group_response.result.id))

        # Create an option space
        option_space_body = {
            "name": "example_option_space",
            "protocol": "ip4"
        }
        option_space_response = create_option_space(option_space_api, option_space_body)

        if option_space_response:
            logging.info("Option Space is created successfully.")
            resource_ids.append(("option_space", option_space_response.result.id))

        # Create an option code
        option_code_body = {
            "name": "example_option_code",
            "code": 234,
            "type": "boolean",
            "option_space": option_space_response.result.id
        }
        option_code_response = create_option_code(option_code_api, option_code_body)

        if option_code_response:
            logging.info("Option Code is created successfully.")
            resource_ids.append(("option_code", option_code_response.result.id))

        # Create a subnet with DHCP options
        subnet_body = {
            "address": "10.0.0.0",
            "cidr": 24,
            "space": ip_space_response.result.id,
            "dhcp_options": [
                {
                    "type": "group",
                    "group": option_group_response.result.id,
                },
                {
                    "type": "option",
                    "option_code": option_code_response.result.id,
                    "option_value": "true",
                }
            ]
        }
        subnet_response = create_subnet(subnet_api, subnet_body)

        if subnet_response:
            logging.info("Subnet is created successfully.")
            resource_ids.append(("subnet", subnet_response.result.id))

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        # Cleanup resources
        cleanup_resources(resource_apis, resource_ids)


if __name__ == "__main__":
    subnet_with_dhcp_options()
