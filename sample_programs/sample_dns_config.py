import sys
sys.path.append("../src")

import dns_config.models as models
from dns_config.api import NewApiClient

def sample_dns_config():
    api_client = NewApiClient()

    try:
        view_response = api_client.view_api.create(
            body=models.AuthNSG(
                Comment="hello",
                name="hello"
            )
        )
        if view_response is not None :
            print("Auth NSG Created")
        else:
            raise Exception("Auth NSG not created")

        auth_zone_response = api_client.auth_zone_api.create(
            body=models.AuthZone(
                Comment="hello",
                name="hello",
                view = view_response.result.id,
            )
        )


        if auth_zone_response is not None :
            api_client.api.auth_zone_api.delete(view_response.result.id)
        if view_response is not None :
            api_client.api.view_api.delete(view_response.result.id)

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    sample_dns_config()