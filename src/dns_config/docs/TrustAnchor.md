# TrustAnchor

DNSSEC trust anchor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **int** |  | 
**protocol_zone** | **str** | Zone FQDN in punycode. | [optional] [readonly] 
**public_key** | **str** | DNSSEC key data. Non-empty, valid base64 string. | 
**sep** | **bool** | Optional. Secure Entry Point flag.  Defaults to _true_. | [optional] 
**zone** | **str** | Zone FQDN. | 

## Example

```python
from dns_config.models.trust_anchor import TrustAnchor

# TODO update the JSON string below
json = "{}"
# create an instance of TrustAnchor from a JSON string
trust_anchor_instance = TrustAnchor.from_json(json)
# print the JSON string representation of the object
print(TrustAnchor.to_json())

# convert the object into a dict
trust_anchor_dict = trust_anchor_instance.to_dict()
# create an instance of TrustAnchor from a dict
trust_anchor_from_dict = TrustAnchor.from_dict(trust_anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


