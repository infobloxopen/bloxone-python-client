# TSIGKey

A __TSIGKey__ object (_keys/tsig_) represents a TSIG key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The TSIG key algorithm.  Valid values are: * _hmac_sha1_ * _hmac_sha224_ * _hmac_sha256_ * _hmac_sha384_ * _hmac_sha512_  Defaults to _hmac_sha256_. | [optional] 
**comment** | **str** | The description for the TSIG key. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The TSIG key name in the absolute domain name format. | 
**protocol_name** | **str** | The TSIG key name supplied during a create/update operation that is converted to canonical form in punycode. | [optional] [readonly] 
**secret** | **str** | The TSIG key secret as a Base64 encoded string. | 
**tags** | **object** | The tags for the TSIG key in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from keys.models.tsig_key import TSIGKey

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


