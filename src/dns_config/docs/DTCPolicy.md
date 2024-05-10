# DTCPolicy

The __DTC Policy__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | __DTC Policy__ display name. | [optional] [readonly] 
**policy_id** | **str** | The resource identifier. | [optional] 

## Example

```python
from dns_config.models.dtc_policy import DTCPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DTCPolicy from a JSON string
dtc_policy_instance = DTCPolicy.from_json(json)
# print the JSON string representation of the object
print(DTCPolicy.to_json())

# convert the object into a dict
dtc_policy_dict = dtc_policy_instance.to_dict()
# create an instance of DTCPolicy from a dict
dtc_policy_from_dict = DTCPolicy.from_dict(dtc_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


