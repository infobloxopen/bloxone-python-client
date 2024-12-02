import sys
import logging
from typing import Optional
import dns_config
from dns_config.api import NewApiClient
from dns_data.api import NewApiClient as RecordsApiClient
from dns_data.models import Record
from dns_config.models import View, AuthZone


def create_view(api_client: NewApiClient, name: str, comment: str) -> Optional[View]:
    """Creates a DNS view."""
    return api_client.view_api.create(
        body=View(name=name, comment=comment)
    )


def create_auth_zone(
    api_client: NewApiClient, view_id: str, fqdn: str, comment: str
) -> Optional[AuthZone]:
    """Creates an authentication zone."""
    return api_client.auth_zone_api.create(
        body=AuthZone(view=view_id, fqdn=fqdn, primary_type="cloud", comment=comment)
    )


def create_dns_record(
    r_client: RecordsApiClient, auth_zone_id: str, record_type: str, name: str, ttl: int, rdata: dict, comment: str, tags: Optional[dict] = None
) -> Optional[Record]:
    """Creates a generic DNS record based on the type."""
    try:
        record = Record(
            type=record_type,
            zone=auth_zone_id,
            name_in_zone=name,
            comment=comment,
            disabled=False,
            ttl=ttl,
            rdata=rdata,
            tags=tags or {}
        )
        return r_client.records_api.create(body=record)
    except Exception as e:
        logging.error(f"Failed to create {record_type} record '{name}': {e}")
        return None


def cleanup_resources(api_client: NewApiClient, resource_ids: list):
    """Deletes created resources for cleanup."""
    for resource_type, resource_id in reversed(resource_ids):
        try:
            getattr(api_client, f"{resource_type}_api").delete(resource_id)
            logging.info(f"Deleted {resource_type} with ID: {resource_id}")
        except Exception as e:
            logging.error(f"Failed to delete {resource_type} with ID {resource_id}: {e}")


def sample_dns_records():
    """Runs a sample DNS configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    api_client = NewApiClient()
    r_client = RecordsApiClient()
    resource_ids = []

    try:
        # Create resources
        view_response = create_view(api_client, "view-example", "View created through Python client")
        if view_response:
            resource_ids.append(("view", view_response.result.id))
            logging.info("View created successfully")

        auth_zone_response = create_auth_zone(
            api_client, view_response.result.id, "domain.com.", "Auth zone created through Python client"
        )
        if auth_zone_response:
            resource_ids.append(("auth_zone", auth_zone_response.result.id))
            logging.info("Auth zone created successfully")

        # Define record details in a dictionary
        record_details = [
            {"type": "a", "name": "a-record", "rdata": {"address": "10.0.0.10"}, "comment": "Temp A record", "ttl": 3600},
            {"type": "aaaa", "name": "aaaa-record", "rdata": {"address": "2001:db8::1"}, "comment": "Temp AAAA record", "ttl": 3600},
            {"type": "cname", "name": "cname-record", "rdata": {"cname": "example.com."}, "comment": "Temp CNAME record", "ttl": 3600},
            {"type": "txt", "name": "txt-record", "rdata": {"text": "text record data"}, "comment": "Temp TXT record", "ttl": 3600},
            {"type": "ns", "name": "ns-record", "rdata": {"dname": "ns1.domain.com."}, "comment": "Temp NS record", "ttl": 3600},
            {"type": "ptr", "name": "ptr-record", "rdata": {"dname": "10.0.0.10.in-addr.arpa."}, "comment": "Temp PTR record", "ttl": 3600},
            # {"type": "soa", "name": "",
            #     "rdata": {
            #         "mname": "ns1.domain.com.",
            #         "rname": "example.domain.com.",
            #         "serial": 1,
            #         "refresh": 860,
            #         "retry": 7200,
            #         "expire": 3600000,
            #         "negative_ttl": 3600,
            #     }, "comment": "Temp SOA record",
            #  "ttl": 86400},
        ]

        # Create the DNS records
        for record in record_details:
            record_response = create_dns_record(
                r_client,
                auth_zone_response.result.id,
                record["type"],
                record["name"],
                record["ttl"],
                record["rdata"],
                record["comment"]
            )
            if record_response:
                logging.info(f"{record['type']} record '{record['name']}' created successfully")

        logging.info("All records created successfully!")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        cleanup_resources(api_client, resource_ids)
        logging.info("Cleanup done.")
        print("Done")


if __name__ == "__main__":
    sample_dns_records()
