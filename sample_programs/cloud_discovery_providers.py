import sys
import logging
from typing import Optional, List, Tuple

sys.path.append("../src")

from bloxone_client import ApiClient
from cloud_discovery import ProvidersApi, DiscoveryConfig


def create_discovery_job(
        api_client: ProvidersApi,
        body: dict
) -> Optional[DiscoveryConfig]:
    """
    Create a cloud discovery job.

    Args:
        api_client (ProvidersApi): API client for providers
        body (dict): Configuration details for the discovery job

    Returns:
        Optional[DiscoveryConfig]: Created discovery job configuration or None
    """
    return api_client.create(body=body)


def delete_discovery_job(
        api_client: ProvidersApi,
        resource_ids: List[Tuple[str, str]]
):
    """
    Delete discovery jobs in reverse order.

    Args:
        api_client (ProvidersApi): API client for providers
        resource_ids (List[Tuple[str, str]]): List of (resource_type, resource_id) tuples
    """
    for resource_type, resource_id in reversed(resource_ids):
        try:
            api_client.delete(resource_id)
            logging.info(f"Deleted {resource_type} with ID: {resource_id}")
        except Exception as e:
            logging.error(f"Failed to delete {resource_type} with ID {resource_id}: {e}")


def sample_dns_records():
    """
    Run a sample cloud discovery job configuration process.

    This script demonstrates creating discovery jobs for three cloud providers:
    - Amazon Web Services (AWS)
    - Microsoft Azure
    - Google Cloud Platform (GCP)

    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Initialize API client and discovery API
    api_client = ApiClient()
    discovery_api = ProvidersApi(api_client)

    # List to track created resources
    resource_ids = []

    try:
        # Create AWS Cloud Discovery Job
        aws_discovery_job_body = {
            "name": "example_provider_aws",
            "provider_type": "Amazon Web Services",
            "account_preference": "single",
            "credential_preference": {
                "access_identifier_type": "role_arn",
                "credential_type": "dynamic"
            },
            "source_configs": [
                {
                    "credential_config": {
                        "access_identifier": "arn:aws:iam::123456789012:role/role-name"
                    }
                }
            ],
            "destination_types_enabled": [
                "IPAM/DHCP",
            ],
            "destinations": [
                {
                    "config": {},
                    "destination_type": "IPAM/DHCP"
                }
            ],
            "tags": {
                "site": "Site A"
            }
        }

        aws_discovery_response = create_discovery_job(
            discovery_api,
            aws_discovery_job_body
        )

        if aws_discovery_response:
            resource_ids.append((
                "aws_discovery_job",
                aws_discovery_response.result.id
            ))
            logging.info("AWS Cloud Discovery Job created successfully")

        # Create Azure Cloud Discovery Job
        azure_discovery_job_body = {
            "name": "example_provider_azure",
            "provider_type": "Microsoft Azure",
            "account_preference": "auto_discover_multiple",
            "credential_preference": {
                "access_identifier_type": "tenant_id",
                "credential_type": "dynamic"
            },
            "source_configs": [
                {
                    "credential_config": {
                        "access_identifier": "xyz98765-4321-abcd-efgh-ijklmnopqrst"
                    },
                    "restricted_to_accounts": [
                        "12345678-abcd-efgh-ijkl-901234567890"
                    ]
                }
            ],
            "destination_types_enabled": [
                "IPAM/DHCP",
                "ACCOUNTS"
            ],
            "destinations": [
                {
                    "config": {},
                    "destination_type": "ACCOUNTS"
                },
                {
                    "config": {
                        "view_id": "bloxone_dns_view.example.id"
                    },
                    "destination_type": "IPAM/DHCP"
                }
            ],
            "tags": {
                "site": "Site A"
            }
        }

        azure_discovery_response = create_discovery_job(
            discovery_api,
            azure_discovery_job_body
        )

        if azure_discovery_response:
            resource_ids.append((
                "azure_discovery_job",
                azure_discovery_response.result.id
            ))
            logging.info("Azure Cloud Discovery Job created successfully")

        # Create GCP Cloud Discovery Job
        gcp_discovery_job_body = {
            "name": "example_provider_gcp",
            "provider_type": "Google Cloud Platform",
            "account_preference": "single",
            "credential_preference": {
                "access_identifier_type": "project_id",
                "credential_type": "dynamic"
            },
            "source_configs": [
                {
                    "credential_config": {
                        "access_identifier": "my-bloxone-example-2024"
                    }
                }
            ],
            "tags": {
                "site": "Site A"
            }
        }

        gcp_discovery_response = create_discovery_job(
            discovery_api,
            gcp_discovery_job_body
        )

        if gcp_discovery_response:
            resource_ids.append((
                "gcp_discovery_job",
                gcp_discovery_response.result.id
            ))
            logging.info("GCP Cloud Discovery Job created successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        # Clean up created resources
        delete_discovery_job(discovery_api, resource_ids)
        logging.info("Cleanup done.")
        print("Done")


if __name__ == "__main__":
    sample_dns_records()
