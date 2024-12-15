# SubAccountV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 

## Example

```python
from cloud_discovery.models.sub_account_v2 import SubAccountV2

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountV2 from a JSON string
sub_account_v2_instance = SubAccountV2.from_json(json)
# print the JSON string representation of the object
print(SubAccountV2.to_json())

# convert the object into a dict
sub_account_v2_dict = sub_account_v2_instance.to_dict()
# create an instance of SubAccountV2 from a dict
sub_account_v2_from_dict = SubAccountV2.from_dict(sub_account_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


