import os
import sys
import logging
from typing import Optional

sys.path.append("../src")

import dns_config , dns_data
from bloxone_client import ApiClient , Configuration
from dns_data.models import Record
from dns_config.models import View, AuthZone
from dns_config.api import ViewApi, AuthZoneApi
from dns_data.api import RecordApi


def create_view(view_api, view_body) -> Optional[View]:
    """Creates a DNS view."""
    return view_api.create(
        body=view_body
    )


def create_auth_zone(auth_zone_api, auth_zone_body) -> Optional[AuthZone]:
    """Creates an authentication zone."""
    return auth_zone_api.create(
        body=auth_zone_body
    )


def create_dns_record(record_api , record_body) -> Optional[Record]:
    """Creates a generic DNS record based on the type."""
    print(record_body)
    response = record_api.create(
        body=record_body
    )
    print(response)
    return response


def cleanup_resources(resource_apis, resource_ids: list):
    """Deletes created resources for cleanup."""
    for resource_type, resource_id in reversed(resource_ids):
        try:
            resource_apis[resource_type].delete(resource_id)
            logging.info(f"Deleted {resource_type} with ID: {resource_id}")
        except Exception as e:
            logging.error(f"Failed to delete {resource_type} with ID {resource_id}: {e}")


def sample_dns_records():
    """Runs a sample DNS configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    api_client = ApiClient()
    view_api = dns_config.ViewApi(api_client)
    auth_zone_api = dns_config.AuthZoneApi(api_client)
    record_api = RecordApi(api_client)
    resource_ids = []
    resource_apis = {
        "view": view_api,
        "auth_zone": auth_zone_api,
        "record": record_api
    }


    try:

        view_body = View(
            name="view-example",
            comment="View created through Python client"
        )
        view_response = create_view(view_api, view_body)
        if view_response:
            resource_ids.append(("view", view_response.result.id))
            logging.info("View created successfully")

        auth_zone_body  = AuthZone(
            view=view_response.result.id,
            fqdn="mydomain.com.",
            primary_type="cloud",
            comment = "Auth zone created through Python client"
        )
        auth_zone_response = create_auth_zone(
            auth_zone_api, auth_zone_body
        )
        if auth_zone_response:
            resource_ids.append(("auth_zone", auth_zone_response.result.id))
            logging.info("Auth zone created successfully")

        # Prepare individual record configurations
        a_record = Record(
            type = "A",
            #"name_in_zone": "a-record",
            rdata = {"address": "10.0.0.10"},
            zone = auth_zone_response.result.id,
            comment = "IPv4 A record example",
            #"ttl": 3600
        )

        aaaa_record = {
            "type": "aaaa",
            "rdata": {"address": "2001:db8::1"},
            "zone": auth_zone_response.result.id,
            "comment": "IPv6 AAAA record example",
            "ttl": 3600
        }

        cname_record = {
            "type": "cname",
            "name": "cname-record",
            "rdata": {"cname": "example.com."},
            "zone": auth_zone_response.result.id,
            "comment": "Canonical Name record example",
            "ttl": 3600
        }

        txt_record = {
            "type": "txt",
            "name": "txt-record",
            "rdata": {"text": "text record data"},
            "zone": auth_zone_response.result.id,
            "comment": "Text record example",
            "ttl": 3600
        }

        ns_record = {
            "type": "ns",
            "name": "ns-record",
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

        a_record_response  = record_api.create(body=Record(
            type="A",
            rdata={"address": "10.0.0.10"},
            zone=auth_zone_response.result.id,
            comment="IPv4 A record example",
        ))
        if a_record_response:
            print(a_record_response)
        else:
            print("Failed")

        # Create records individually
        record_list = [
            a_record, aaaa_record, cname_record,
            txt_record, ns_record, ptr_record
        ]

        # Iterate through and create each record type
        for record_body in record_list:
            record_response = create_dns_record(record_api, record_body)

            if record_response:
                print("here")
                logging.info(f"{record_body['type']} record '{record_body['name']}' created successfully")
            else:
                logging.warning(f"Failed to create {record_body['type']} record '{record_body['name']}'")

        logging.info("All records processed!")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        cleanup_resources(resource_apis, resource_ids)
        logging.info("Cleanup done.")
        print("Done")


if __name__ == "__main__":
    sample_dns_records()