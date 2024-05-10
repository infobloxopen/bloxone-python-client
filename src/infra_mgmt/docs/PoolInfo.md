# PoolInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_status** | **str** | Composite Status of the Pool that this resource belongs to (&#x60;online&#x60;, &#x60;degraded&#x60;, &#x60;error&#x60;, &#x60;unavailable&#x60;). | [optional] 
**pool_id** | **str** | The resource identifier. | [optional] 
**pool_name** | **str** | Name of the Pool that this resource belongs to. | [optional] 

## Example

```python
from infra_mgmt.models.pool_info import PoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PoolInfo from a JSON string
pool_info_instance = PoolInfo.from_json(json)
# print the JSON string representation of the object
print(PoolInfo.to_json())

# convert the object into a dict
pool_info_dict = pool_info_instance.to_dict()
# create an instance of PoolInfo from a dict
pool_info_from_dict = PoolInfo.from_dict(pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


