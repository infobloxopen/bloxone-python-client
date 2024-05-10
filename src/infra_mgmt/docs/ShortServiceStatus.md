# ShortServiceStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message text for the Service. | [optional] 
**status** | **str** | Status of the Service (&#x60;started&#x60;, &#x60;starting&#x60;, &#x60;stopping&#x60;, &#x60;stopped&#x60;, &#x60;error&#x60;). | [optional] 
**updated_at** | **datetime** | Timestamp of the latest status update of Service. | [optional] 

## Example

```python
from infra_mgmt.models.short_service_status import ShortServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ShortServiceStatus from a JSON string
short_service_status_instance = ShortServiceStatus.from_json(json)
# print the JSON string representation of the object
print(ShortServiceStatus.to_json())

# convert the object into a dict
short_service_status_dict = short_service_status_instance.to_dict()
# create an instance of ShortServiceStatus from a dict
short_service_status_from_dict = ShortServiceStatus.from_dict(short_service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


