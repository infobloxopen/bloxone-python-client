# Bloxone Python Client

This repository provides a Python Client library for interacting with Infoblox BloxOne APIs. The library is generated using the [OpenAPI Generator](https://openapi-generator.tech) project.

The following Bloxone APIs are supported:

## Bloxone Cloud
- [Infrastructure Management](infra_mgmt/README.md)
- [Infrastructure Provision (HostActivation API)](infra_provision/README.md)
- [Anycast Configuration Manager](anycast/README.md)
- [Upgrade Policy](upgradePolicy/README.md)

## Bloxone Threat Defense
- [Threat Defense Cloud (FW API)](fw/README.md)
- [DNS Forwarding Proxy (DFP API)](dfp/README.md)
- [Redirect](redirect/README.md)

## Universal DDI
- [IP Address Management](ipam/README.md)
- [DNS Configuration](dns_config/README.md)
- [DNS Data](dns_data/README.md)
- [Keys](keys/README.md)
- [Cloud Discovery Providers](cloud_discovery/README.md)
- [IPAM Federation](ipam_federation/README.md)

## Installation

To install the Bloxone Python Client, use the following command:

```bash
pip install git+https://github.com/infobloxopen/bloxone-python-client
```

## Usage


To use the Bloxone Python Client, you need to import the client and create an instance of the client. For example:

```python
from bloxone_client import ApiClient

client = ApiClient()
```

Additionally , you can also add a custom config to the client. For example:

```python
from bloxone_client import Configuration, ApiClient

config = Configuration()

client = ApiClient(config)
```

Furthermore , you can import the specific API module and use the client to interact with the API. For example:

```python
from dns_config import ViewApi

view_api = ViewApi(client)
```

## Configuration

### Client Name

The client name is used to identify the client in the logs. By default, the client name is set to `bloxone-python-client`. You can change this by creating an instance of Configuration and setting the client name. For example:

```python
from bloxone_client import Configuration

config = Configuration(
    client_name = "my-client",
)
```

### Server URL

The default URL for the Cloud Services Portal is `https://csp.infoblox.com`. If you need to change this, you can create an instance of Configuration and set the URL. For example:

```python
from bloxone_client import Configuration

config = Configuration(
    csp_url = "https://csp.eu.infoblox.com",
)
```

You can also set the URL using the environment variable `BLOXONE_CSP_URL`

### Authorization

An API key is required to access BloxOne API. You can obtain an API key by following the instructions in the guide for [Configuring User API Keys](https://docs.infoblox.com/space/BloxOneCloud/35430405/Configuring+User+API+Keys).

To use an API key with BloxOne API, you can create a new instance of Configuration . For example:

```python
from bloxone_client import Configuration

config = Configuration(
    api_key = "API_KEY",
)
```

Alternatively, You can also set the API key using the environment variable `BLOXONE_API_KEY`

Note: The API key is a secret and should be handled securely. Hardcoding the API key in your code is not recommended.

### Default Tags

The BloxOne API supports tagging resources. You can set default tags for all resources created using the client. 

To set the Default Tags , you can create a new instance of Configuration to set the tags. For example:

```python
from bloxone_client import Configuration

config = Configuration(
    default_tags = {
        "tag1": "value1",
        "tag2": "value2",
    }
)
```

## Support 

For support and inquiries, contact Infoblox Support or refer to the official [BloxOne documentation](https://csp.infoblox.com/apidoc).