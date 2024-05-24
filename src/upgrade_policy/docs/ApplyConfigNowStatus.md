# ApplyConfigNowStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostid** | **str** |  | [optional] 
**ophid** | **str** |  | [optional] 
**status_code** | [**StatusCode**](StatusCode.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.apply_config_now_status import ApplyConfigNowStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyConfigNowStatus from a JSON string
apply_config_now_status_instance = ApplyConfigNowStatus.from_json(json)
# print the JSON string representation of the object
print(ApplyConfigNowStatus.to_json())

# convert the object into a dict
apply_config_now_status_dict = apply_config_now_status_instance.to_dict()
# create an instance of ApplyConfigNowStatus from a dict
apply_config_now_status_from_dict = ApplyConfigNowStatus.from_dict(apply_config_now_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


