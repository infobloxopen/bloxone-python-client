# TSIGKey

A __TSIGKey__ object represents a TSIG key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | TSIG key algorithm.  Valid values are:  * _hmac_sha256_  * _hmac_sha1_  * _hmac_sha224_  * _hmac_sha384_  * _hmac_sha512_ | [optional] 
**comment** | **str** | The description for the TSIG key. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**key** | **str** | The resource identifier. | 
**name** | **str** | The TSIG key name, FQDN. | [optional] 
**protocol_name** | **str** | The TSIG key name in punycode. | [optional] [readonly] 
**secret** | **str** | The TSIG key secret, base64 string. | [optional] 

## Example

```python
from ipam.models.tsig_key import TSIGKey

# TODO update the JSON string below
json = "{}"
# create an instance of TSIGKey from a JSON string
tsig_key_instance = TSIGKey.from_json(json)
# print the JSON string representation of the object
print(TSIGKey.to_json())

# convert the object into a dict
tsig_key_dict = tsig_key_instance.to_dict()
# create an instance of TSIGKey from a dict
tsig_key_from_dict = TSIGKey.from_dict(tsig_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


