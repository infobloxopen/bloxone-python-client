# OnpremDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostid** | **str** |  | [optional] 
**ophid** | **str** |  | [optional] 

## Example

```python
from upgrade_policy.models.onprem_details import OnpremDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OnpremDetails from a JSON string
onprem_details_instance = OnpremDetails.from_json(json)
# print the JSON string representation of the object
print(OnpremDetails.to_json())

# convert the object into a dict
onprem_details_dict = onprem_details_instance.to_dict()
# create an instance of OnpremDetails from a dict
onprem_details_from_dict = OnpremDetails.from_dict(onprem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


