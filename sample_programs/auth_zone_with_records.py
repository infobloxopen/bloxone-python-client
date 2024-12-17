import sys
import logging
import time
from typing import Optional

sys.path.append("../src")

# Import necessary modules from bloxone_client and dns_data
from bloxone_client import ApiClient, Configuration
from dns_data.models import Record
from dns_config.models import View, AuthZone
from dns_config.api import ViewApi, AuthZoneApi
from dns_data.api import RecordApi


def create_view(view_api, view_body) -> Optional[View]:
    """
    Creates a DNS view.

    Args:
        view_api: The ViewApi object to interact with the View API.
        view_body: The data (body) for creating a new view.

    Returns:
        View object if creation is successful, None otherwise.
    """
    return view_api.create(body=view_body)


def create_auth_zone(auth_zone_api, auth_zone_body) -> Optional[AuthZone]:
    """
    Creates an authentication zone.

    Args:
        auth_zone_api: The AuthZoneApi object to interact with the AuthZone API.
        auth_zone_body: The data (body) for creating a new authentication zone.

    Returns:
        AuthZone object if creation is successful, None otherwise.
    """
    return auth_zone_api.create(body=auth_zone_body)


def create_dns_record(record_api, record_body) -> Optional[Record]:
    """
    Creates a DNS record based on the provided record type and body.

    Args:
        record_api: The RecordApi object to interact with the Record API.
        record_body: The data (body) for creating a new DNS record.

    Returns:
        Record object if creation is successful, None otherwise.
    """
    response = record_api.create(body=record_body)
    return response


def cleanup_resources(resource_apis, resource_ids: list):
    """
    Deletes created resources to clean up.

    Args:
        resource_apis: A dictionary mapping resource types to their respective API objects.
        resource_ids: A list of tuples containing resource types and their corresponding IDs.
    """
    for resource_type, resource_id in reversed(resource_ids):
        try:
            resource_apis[resource_type].delete(resource_id)
            logging.info(f"Deleted {resource_type} with ID: {resource_id}")
        except Exception as e:
            logging.error(f"Failed to delete {resource_type} with ID {resource_id}: {e}")


def sample_dns_records():
    """Runs a sample DNS configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Initialize API client and associated API objects
    api_client = ApiClient()
    view_api = ViewApi(api_client)
    auth_zone_api = AuthZoneApi(api_client)
    record_api = RecordApi(api_client)

    resource_ids = []
    resource_apis = {
        "view": view_api,
        "auth_zone": auth_zone_api,
        "record": record_api
    }

    try:

        view_body = {
            "name": "view-example",
            "comment": "View created through Python client"
        }
        view_response = create_view(view_api, view_body)
        if view_response:
            resource_ids.append(("view", view_response.result.id))
            logging.info("View created successfully")

        auth_zone_body  = {
            "view": view_response.result.id,
            "fqdn": "mydomain.com.",
            "primary_type": "cloud",
            "comment": "Auth zone created through Python client"
        }
        auth_zone_response = create_auth_zone(
            auth_zone_api, auth_zone_body
        )
        if auth_zone_response:
            resource_ids.append(("auth_zone", auth_zone_response.result.id))
            logging.info("Auth zone created successfully")

        # Prepare individual record configurations
        a_record = {
            "type": "A",
            "name_in_zone": "a-record",
            "rdata": {
                "address": "10.0.0.10"
            },
            "zone": auth_zone_response.result.id,
            "comment": "IPv4 A record example",
            "ttl": 3600
        }
        aaaa_record = {
            "type": "aaaa",
            "name_in_zone": "aaaa-record",
            "rdata": {"address": "2001:db8::1"},
            "zone": auth_zone_response.result.id,
            "comment": "IPv6 AAAA record example",
            "ttl": 3600
        }

        cname_record = {
            "type": "cname",
            "name_in_zone": "cname-record",
            "rdata": {"cname": "example.com."},
            "zone": auth_zone_response.result.id,
            "comment": "Canonical Name record example",
            "ttl": 3600
        }

        txt_record = {
            "type": "txt",
            "name_in_zone": "txt-record",
            "rdata": {"text": "text record data"},
            "zone": auth_zone_response.result.id,
            "comment": "Text record example",
            "ttl": 3600
        }

        ns_record = {
            "type": "ns",
            "name_in_zone": "ns-record",
            "rdata": {"dname": "ns1.domain.com."},
            "zone": auth_zone_response.result.id,
            "comment": "Name Server record example",
            "ttl": 3600
        }

        ptr_record = {
            "type": "ptr",
            "name_in_zone": "ptr-record",
            "rdata": {"dname": "10.0.0.10.in-addr.arpa."},
            "zone": auth_zone_response.result.id,
            "comment": "Pointer record example",
            "ttl": 3600
        }

        time.sleep(1)
        # Create records individually
        record_list = [
            a_record, aaaa_record, cname_record,
            txt_record, ns_record, ptr_record
        ]

        for record_body in record_list:
            record_response = create_dns_record(record_api, record_body)

            if record_response:
                logging.info(f"{record_response.result.type} record '{record_response.result.name_in_zone}' created successfully")
            else:
                logging.warning(f"Failed to create {record_body['type']} record '{record_body['name']}'")

        logging.info("All records processed!")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        # Cleanup resources created during the process
        cleanup_resources(resource_apis, resource_ids)
        logging.info("Cleanup done.")
        print("Done")


if __name__ == "__main__":
    sample_dns_records()