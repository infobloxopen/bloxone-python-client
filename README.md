# Universal DDI Python Client

This repository provides a Python Client library for interacting with Infoblox APIs. The library is generated using the [OpenAPI Generator](https://openapi-generator.tech) project.

The following Infoblox APIs are supported:

## Infoblox Cloud
- [Infrastructure Management](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/infra_mgmt/README.md)
- [Infrastructure Provision (HostActivation API)](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/infra_provision/README.md)
- [Anycast Configuration Manager](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/anycast/README.md)
- [Upgrade Policy](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/upgrade_policy/README.md)

## Infoblox Threat Defense
- [Threat Defense Cloud (FW API)](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/fw/README.md)
- [DNS Forwarding Proxy (DFP API)](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/dfp/README.md)
- [Redirect](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/redirect/README.md)

## Universal DDI
- [IP Address Management](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/ipam/README.md)
- [DNS Configuration](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/dns_config/README.md)
- [DNS Data](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/dns_data/README.md)
- [Keys](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/keys/README.md)
- [Cloud Discovery Providers](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/cloud_discovery/README.md)
- [IPAM Federation](https://github.com/infobloxopen/universal-ddi-python-client/blob/main/src/ipam_federation/README.md)

## Installation

To install the Universal DDI Python Client, use the following command:

```bash
pip install universal-ddi-python-client
```

## Usage


To use the Universal DDI Python Client, you need to import the client and create an instance of the client. For example:

```python
from universal_ddi_client import ApiClient

client = ApiClient()
```

Additionally , you can also add a custom config to the client. For example:

```python
from universal_ddi_client import Configuration, ApiClient

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

The client name is used to identify the client in the logs. By default, the client name is set to `universal-ddi-python-client`. You can change this by creating an instance of Configuration and setting the client name. For example:

```python
from universal_ddi_client import Configuration

config = Configuration(
    client_name = "my-client",
)
```

### Server URL

The default URL for the Cloud Services Portal is `https://csp.infoblox.com`. If you need to change this, you can create an instance of Configuration and set the URL. For example:

```python
from universal_ddi_client import Configuration

config = Configuration(
    portal_url = "https://csp.eu.infoblox.com",
)
```

You can also set the URL using the environment variable `INFOBLOX_PORTAL_URL` or `BLOXONE_CSP_URL`.

> **Note:** `BLOXONE_CSP_URL` is deprecated and will be removed in future releases. It is recommended to use `INFOBLOX_PORTAL_URL` instead.


### Authorization

An API key is required to access Infoblox API. You can obtain an API key by following the instructions in the guide for [Configuring User API Keys](https://docs.infoblox.com/space/BloxOneCloud/35430405/Configuring+User+API+Keys).

To use an API key with Infoblox API, you can create a new instance of Configuration . For example:

```python
from universal_ddi_client import Configuration

config = Configuration(
    portal_key = "PORTAL_KEY",
)
```

Alternatively, You can also set the API key using the environment variable `INFOBLOX_PORTAL_KEY` or `BLOXONE_API_KEY` .

> **Note:** `BLOXONE_API_KEY` is deprecated and will be removed in future releases. It is recommended to use `INFOBLOX_PORTAL_KEY` instead.

> **Note:** The API key is a secret and should be handled securely. Hardcoding the API key in your code is not recommended.

### Default Tags

The Infoblox API supports tagging resources. You can set default tags for all resources created using the client. 

To set the Default Tags , you can create a new instance of Configuration to set the tags. For example:

```python
from universal_ddi_client import Configuration

config = Configuration(
    default_tags = {
        "tag1": "value1",
        "tag2": "value2",
    }
)
```

## Support 

For support and inquiries, contact Infoblox Support or refer to the official [Universal DDI documentation](https://csp.infoblox.com/apidoc).