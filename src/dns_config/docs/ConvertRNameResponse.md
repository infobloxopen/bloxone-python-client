# ConvertRNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rname** | **str** | The SOA RNAME field converted from the provided email address. | [optional] 

## Example

```python
from dns_config.models.convert_r_name_response import ConvertRNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertRNameResponse from a JSON string
convert_r_name_response_instance = ConvertRNameResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertRNameResponse.to_json())

# convert the object into a dict
convert_r_name_response_dict = convert_r_name_response_instance.to_dict()
# create an instance of ConvertRNameResponse from a dict
convert_r_name_response_from_dict = ConvertRNameResponse.from_dict(convert_r_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


