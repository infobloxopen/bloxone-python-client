# TSIGKey

Object representing TSIG key synced from Keys Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | TSIG key algorithm.  Possible values:  * _hmac_sha256_,  * _hmac_sha1_,  * _hmac_sha224_,  * _hmac_sha384_,  * _hmac_sha512_. | [optional] 
**comment** | **str** | Comment for TSIG key. | [optional] 
**key** | **str** | The resource identifier. | [optional] 
**name** | **str** | TSIG key name, FQDN. | [optional] 
**protocol_name** | **str** | TSIG key name in punycode. | [optional] [readonly] 
**secret** | **str** | TSIG key secret, base64 string. | [optional] 

## Example

```python
from dns_config.models.tsig_key import TSIGKey

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


