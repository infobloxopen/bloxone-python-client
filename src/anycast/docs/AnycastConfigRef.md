# AnycastConfigRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast_config_name** | **str** |  | [optional] 
**routing_protocols** | **List[str]** | Routing protocols enabled for this anycast configuration, on a particular host. Valid protocol names are \&quot;BGP\&quot;, \&quot;OSPF\&quot;/\&quot;OSPFv2\&quot;, \&quot;OSPFv3\&quot;. | [optional] 

## Example

```python
from anycast.models.anycast_config_ref import AnycastConfigRef

# TODO update the JSON string below
json = "{}"
# create an instance of AnycastConfigRef from a JSON string
anycast_config_ref_instance = AnycastConfigRef.from_json(json)
# print the JSON string representation of the object
print(AnycastConfigRef.to_json())

# convert the object into a dict
anycast_config_ref_dict = anycast_config_ref_instance.to_dict()
# create an instance of AnycastConfigRef from a dict
anycast_config_ref_from_dict = AnycastConfigRef.from_dict(anycast_config_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


