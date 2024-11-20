import sys

import dns_config

sys.path.append("../src")

import dns_config.models as models
from dns_config.api import NewApiClient

def sample_dns_config():
    api_client = NewApiClient()

    try:
        # Create a DNS view
        view_response = api_client.view_api.create(
            body=models.View(
                name="view-example",
                comment="View object created through python client"
            )
        )
        if view_response is not None:
            print("view response Created")
        else:
            raise Exception("view response not created")

        # Create an authentication zone
        auth_zone_response = api_client.auth_zone_api.create(
            body=models.AuthZone(
                view=view_response.result.id,
                fqdn="domain.com.",
                primary_type="cloud",
                comment="Auth zone object created through python client"
            )
        )

        if auth_zone_response is not None:
            print("auth zone Created")
        else:
            raise Exception("auth_zone_response not created")

        # Create a DNS delegation
        delegation_response = api_client.delegation_api.create(
            body=models.Delegation(
                fqdn="del.domain.com.",
                delegation_servers=[models.DelegationServer(
                    address="12.0.0.0",
                    fqdn="ns1.com.",
                )],
                view=view_response.result.id,
                comment="Delegation zone created through Terraform",
                disabled=True,

            )
        )

        if delegation_response is not None:
            print("DNS delegation created")
        else:
            raise Exception("DNS delegation not created")

        # Create a Auth_NSG
        auth_nsg_response = api_client.auth_nsg_api.create(
            body=models.AuthNSG(
                name="example_dns_auth_nsg",
                comment="Auth NSG object created through python client"
            ),
        )
        if auth_nsg_response is not None:
            print("Auth NSG created")
        else:
            raise Exception("Auth NSG not created")

        # Create a forward Zone
        forward_zone_response = api_client.forward_zone_api.create(
            body=models.ForwardZone(
                fqdn="forward_zone.com.",
                view=view_response.result.id,
                comment="Forward zone object created through python client"
            )
        )
        if forward_zone_response is not None:
            print("Forward Zone created")
        else:
            raise Exception("Forward Zone not created")

        # Create a forward Zone NSG
        forward_nsg_response = api_client.forward_nsg_api.create(
            body=models.ForwardNSG(
                name="example_dns_forward_nsg",
                external_forwarders=[
                    models.Forwarder(
                        address="12.10.2.1",
                        fqdn="ext.primary.com.",
                    )
                ],
                comment="Forward NSG object created through python client",
            )
        )
        if forward_nsg_response is not None:
            print("Forward NSG Zone created")
        else:
            raise Exception("Forward NSG Zone not created")

        # Create  ACL object
        acl_response = api_client.acl_api.create(
            body=models.ACL(
                name="example_dns_acl",
                comment="ACL object created through python client"
            )
        )
        if acl_response is not None:
            print("ACL created")
        else:
            raise Exception("ACL not created")

        # Create dns server
        dns_server_response = api_client.server_api.create(
            body=models.Server(
                name="my-dns-server"
            )
        )
        if dns_server_response is None:
            print("DNS Server created successfully")
        else:
            print("DNS Server creation failed")

        # Delete the resources (cleanup)
        if dns_server_response is not None:
            api_client.server_api.delete(dns_server_response.result.id)
        if forward_nsg_response is not None:
            api_client.forward_nsg_api.delete(forward_nsg_response.result.id)
        if forward_zone_response is not None:
            api_client.forward_zone_api.delete(forward_zone_response.result.id)
        if auth_nsg_response is not None:
            api_client.auth_nsg_api.delete(auth_nsg_response.result.id)
        if delegation_response is not None:
            api_client.delegation_api.delete(delegation_response.result.id)
        if auth_zone_response is not None:
            api_client.auth_zone_api.delete(auth_zone_response.result.id)
        if view_response is not None:
            api_client.view_api.delete(view_response.result.id)

        print("Done")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
   sample_dns_config()
