# InternalSecondary

BloxOne DDI host acting as DNS secondary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The resource identifier. | 

## Example

```python
from dns_config.models.internal_secondary import InternalSecondary

# TODO update the JSON string below
json = "{}"
# create an instance of InternalSecondary from a JSON string
internal_secondary_instance = InternalSecondary.from_json(json)
# print the JSON string representation of the object
print(InternalSecondary.to_json())

# convert the object into a dict
internal_secondary_dict = internal_secondary_instance.to_dict()
# create an instance of InternalSecondary from a dict
internal_secondary_from_dict = InternalSecondary.from_dict(internal_secondary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


