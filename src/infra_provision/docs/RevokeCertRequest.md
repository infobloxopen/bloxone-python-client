# RevokeCertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_serial** | **str** |  | [optional] 
**ophid** | **str** | On-prem host ID which can be obtained either from on-prem or BloxOne UI portal(Manage &gt; Infrastructure &gt; Hosts &gt; Select the onprem &gt; click on 3 dots on top right side &gt; General Information &gt; Ophid) . | [optional] 
**revoke_reason** | **str** |  | [optional] 

## Example

```python
from infra_provision.models.revoke_cert_request import RevokeCertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeCertRequest from a JSON string
revoke_cert_request_instance = RevokeCertRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeCertRequest.to_json())

# convert the object into a dict
revoke_cert_request_dict = revoke_cert_request_instance.to_dict()
# create an instance of RevokeCertRequest from a dict
revoke_cert_request_from_dict = RevokeCertRequest.from_dict(revoke_cert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


