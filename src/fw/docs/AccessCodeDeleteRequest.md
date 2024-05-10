# AccessCodeDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The Bypass Code identifier. | [optional] 

## Example

```python
from fw.models.access_code_delete_request import AccessCodeDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodeDeleteRequest from a JSON string
access_code_delete_request_instance = AccessCodeDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(AccessCodeDeleteRequest.to_json())

# convert the object into a dict
access_code_delete_request_dict = access_code_delete_request_instance.to_dict()
# create an instance of AccessCodeDeleteRequest from a dict
access_code_delete_request_from_dict = AccessCodeDeleteRequest.from_dict(access_code_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


