# Destination

Destination information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**DestinationConfig**](DestinationConfig.md) | Destination configuration. Ex.: &#39;{  \&quot;dns\&quot;: {    \&quot;view_name\&quot;: \&quot;view 1\&quot;,    \&quot;view_id\&quot;: \&quot;dns/view/v1\&quot;,    \&quot;consolidated_zone_data_enabled\&quot;: false,    \&quot;sync_type\&quot;: \&quot;read_only/read_write\&quot;    \&quot;split_view_enabled\&quot;: false  },  \&quot;ipam\&quot;: {    \&quot;ip_space\&quot;: \&quot;\&quot;,  },  \&quot;account\&quot;: {},  }&#39;. | [optional] 
**created_at** | **datetime** | Timestamp when the object has been created. | [optional] [readonly] 
**deleted_at** | **datetime** | Timestamp when the object has been deleted. | [optional] [readonly] 
**destination_type** | **str** | Destination type: DNS / IPAM / ACCOUNT. | 
**id** | **str** | Auto-generated unique destination ID. Format BloxID. | [optional] [readonly] 
**updated_at** | **datetime** | Timestamp when the object has been updated. | [optional] [readonly] 

## Example

```python
from cloud_discovery.models.destination import Destination

# TODO update the JSON string below
json = "{}"
# create an instance of Destination from a JSON string
destination_instance = Destination.from_json(json)
# print the JSON string representation of the object
print(Destination.to_json())

# convert the object into a dict
destination_dict = destination_instance.to_dict()
# create an instance of Destination from a dict
destination_from_dict = Destination.from_dict(destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


