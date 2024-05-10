# DetailService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_state** | **str** | Composite State of this Service (&#x60;started&#x60;, &#x60;stopped&#x60;, &#x60;stopping&#x60;, &#x60;starting&#x60;, &#x60;error&#x60;). | [optional] 
**composite_status** | **str** | Composite Status of this Service (&#x60;online&#x60;, &#x60;stopped&#x60;, &#x60;degraded&#x60;, &#x60;error&#x60;). | [optional] 
**created_at** | **datetime** | Timestamp of creation of Service. | [optional] 
**current_version** | **str** | Current version of this Service. | [optional] 
**description** | **str** | The description of the Service. | [optional] 
**desired_state** | **str** | The desired state of the Service (&#x60;\&quot;start\&quot;&#x60; or &#x60;\&quot;stop\&quot;&#x60;). | [optional] 
**desired_version** | **str** | The desired version of the Service. | [optional] 
**hosts** | [**List[DetailServiceHost]**](DetailServiceHost.md) | List of Hosts on which this Service is deployed. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**interface_labels** | **List[str]** | List of interfaces on which this Service can operate. | [optional] 
**location** | [**DetailLocation**](DetailLocation.md) |  | [optional] 
**name** | **str** | The name of the Service. | [optional] 
**pool** | [**PoolInfo**](PoolInfo.md) |  | [optional] 
**service_type** | **str** | The type of the Service deployed on the Host (&#x60;dns&#x60;, &#x60;cdc&#x60;, etc.). | [optional] 
**tags** | **object** | Tags associated with this Service. | [optional] 
**updated_at** | **datetime** | Timestamp of the latest update on Service. | [optional] 

## Example

```python
from infra_mgmt.models.detail_service import DetailService

# TODO update the JSON string below
json = "{}"
# create an instance of DetailService from a JSON string
detail_service_instance = DetailService.from_json(json)
# print the JSON string representation of the object
print(DetailService.to_json())

# convert the object into a dict
detail_service_dict = detail_service_instance.to_dict()
# create an instance of DetailService from a dict
detail_service_from_dict = DetailService.from_dict(detail_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


