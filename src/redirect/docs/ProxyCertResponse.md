# ProxyCertResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast_dns_certificate_url** | **str** | Infoblox anycast dns client certificate URL. | [optional] 
**certificate_url** | **str** | The certificate URL. | [optional] 

## Example

```python
from redirect.models.proxy_cert_response import ProxyCertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyCertResponse from a JSON string
proxy_cert_response_instance = ProxyCertResponse.from_json(json)
# print the JSON string representation of the object
print(ProxyCertResponse.to_json())

# convert the object into a dict
proxy_cert_response_dict = proxy_cert_response_instance.to_dict()
# create an instance of ProxyCertResponse from a dict
proxy_cert_response_from_dict = ProxyCertResponse.from_dict(proxy_cert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


