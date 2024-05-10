# ListLBDNResponse

The __LBDN__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[LBDN]**](LBDN.md) | List of __LBDN__ objects. | [optional] 

## Example

```python
from dns_config.models.list_lbdn_response import ListLBDNResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListLBDNResponse from a JSON string
list_lbdn_response_instance = ListLBDNResponse.from_json(json)
# print the JSON string representation of the object
print(ListLBDNResponse.to_json())

# convert the object into a dict
list_lbdn_response_dict = list_lbdn_response_instance.to_dict()
# create an instance of ListLBDNResponse from a dict
list_lbdn_response_from_dict = ListLBDNResponse.from_dict(list_lbdn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


