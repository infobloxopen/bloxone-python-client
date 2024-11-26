import sys
import logging
from typing import Optional
import dns_config
from dns_config.api import NewApiClient
from dns_config.models import (
    View,
    AuthZone,
    Delegation,
    DelegationServer,
    AuthNSG,
    ForwardZone,
    ForwardNSG,
    Forwarder,
    ACL,
    Server,
)

sys.path.append("../src")


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


def create_delegation(
    api_client: NewApiClient, view_id: str, fqdn: str, delegation_server: DelegationServer, comment: str
) -> Optional[Delegation]:
    """Creates a DNS delegation."""
    return api_client.delegation_api.create(
        body=Delegation(
            fqdn=fqdn,
            delegation_servers=[delegation_server],
            view=view_id,
            comment=comment,
            disabled=True,
        )
    )


def create_auth_nsg(api_client: NewApiClient, name: str, comment: str) -> Optional[AuthNSG]:
    """Creates an Auth NSG."""
    return api_client.auth_nsg_api.create(body=AuthNSG(name=name, comment=comment))


def create_forward_zone(api_client: NewApiClient, fqdn: str, view_id: str, comment: str) -> Optional[ForwardZone]:
    """Creates a forward zone."""
    return api_client.forward_zone_api.create(
        body=ForwardZone(fqdn=fqdn, view=view_id, comment=comment)
    )


def create_forward_nsg(api_client: NewApiClient, name: str, forwarder: Forwarder, comment: str) -> Optional[ForwardNSG]:
    """Creates a forward NSG."""
    return api_client.forward_nsg_api.create(
        body=ForwardNSG(name=name, external_forwarders=[forwarder], comment=comment)
    )


def create_acl(api_client: NewApiClient, name: str, comment: str) -> Optional[ACL]:
    """Creates an ACL."""
    return api_client.acl_api.create(body=ACL(name=name, comment=comment))


def create_dns_server(api_client: NewApiClient, name: str) -> Optional[Server]:
    """Creates a DNS server."""
    return api_client.server_api.create(body=Server(name=name))


def cleanup_resources(api_client: NewApiClient, resource_ids: list):
    """Deletes created resources for cleanup."""
    for resource_type, resource_id in resource_ids:
        try:
            getattr(api_client, f"{resource_type}_api").delete(resource_id)
            logging.info(f"Deleted {resource_type} with ID: {resource_id}")
        except Exception as e:
            logging.error(f"Failed to delete {resource_type} with ID {resource_id}: {e}")


def sample_dns_config():
    """Runs a sample DNS configuration process."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    api_client = NewApiClient()
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

        delegation_response = create_delegation(
            api_client,
            view_response.result.id,
            "del.domain.com.",
            DelegationServer(address="12.0.0.0", fqdn="ns1.com."),
            "Delegation created through Python client",
        )
        if delegation_response:
            resource_ids.append(("delegation", delegation_response.result.id))
            logging.info("Delegation created successfully")

        auth_nsg_response = create_auth_nsg(api_client, "example_dns_auth_nsg", "Auth NSG created")
        if auth_nsg_response:
            resource_ids.append(("auth_nsg", auth_nsg_response.result.id))
            logging.info("Auth NSG created successfully")

        forward_zone_response = create_forward_zone(api_client, "forward_zone.com.", view_response.result.id, "Forward zone created")
        if forward_zone_response:
            resource_ids.append(("forward_zone", forward_zone_response.result.id))
            logging.info("Forward zone created successfully")

        forward_nsg_response = create_forward_nsg(
            api_client,
            "example_dns_forward_nsg",
            Forwarder(address="12.10.2.1", fqdn="ext.primary.com."),
            "Forward NSG created",
        )
        if forward_nsg_response:
            resource_ids.append(("forward_nsg", forward_nsg_response.result.id))
            logging.info("Forward NSG created successfully")

        acl_response = create_acl(api_client, "example_dns_acl", "ACL created through Python client")
        if acl_response:
            resource_ids.append(("acl", acl_response.result.id))
            logging.info("ACL created successfully")

        dns_server_response = create_dns_server(api_client, "my-dns-server")
        if dns_server_response:
            resource_ids.append(("server", dns_server_response.result.id))
            logging.info("DNS server created successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        cleanup_resources(api_client, resource_ids)


if __name__ == "__main__":
    sample_dns_config()