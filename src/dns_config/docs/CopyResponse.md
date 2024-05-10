# CopyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the resource that was requested to be copied. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**job_id** | **str** | An Unique Id to identify copy operation. | [optional] 

## Example

```python
from dns_config.models.copy_response import CopyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CopyResponse from a JSON string
copy_response_instance = CopyResponse.from_json(json)
# print the JSON string representation of the object
print(CopyResponse.to_json())

# convert the object into a dict
copy_response_dict = copy_response_instance.to_dict()
# create an instance of CopyResponse from a dict
copy_response_from_dict = CopyResponse.from_dict(copy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


