# Service

Infrastructure Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[ServiceHostConfig]**](ServiceHostConfig.md) | List of Host-specific configurations of this Service. | [optional] [readonly] 
**created_at** | **datetime** | Timestamp of creation of Service. | [optional] [readonly] 
**description** | **str** | The description of the Service (optional). | [optional] 
**desired_state** | **str** | The desired state of the Service. Should either be &#x60;\&quot;start\&quot;&#x60; or &#x60;\&quot;stop\&quot;&#x60;. | [optional] 
**desired_version** | **str** | The desired version of the Service. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**interface_labels** | **List[str]** | List of interfaces on which this Service can operate. Note: The list can contain custom interface labels (Example: &#x60;[\&quot;WAN\&quot;,\&quot;LAN\&quot;,\&quot;label1\&quot;,\&quot;label2\&quot;]&#x60;) | [optional] 
**name** | **str** | The name of the Service (unique). | 
**pool_id** | **str** | The resource identifier. | 
**service_type** | **str** | The type of the Service deployed on the Host (&#x60;dns&#x60;, &#x60;cdc&#x60;, etc.). | 
**tags** | **object** | Tags associated with this Service. | [optional] 
**updated_at** | **datetime** | Timestamp of the latest update on Service. | [optional] [readonly] 

## Example

```python
from infra_mgmt.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


