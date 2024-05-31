# GenerateTSIGResponse

The response format to generate the TSIG key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**GenerateTSIGResult**](GenerateTSIGResult.md) | The generated TSIG key. | [optional] 

## Example

```python
from keys.models.generate_tsig_response import GenerateTSIGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTSIGResponse from a JSON string
generate_tsig_response_instance = GenerateTSIGResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateTSIGResponse.to_json())

# convert the object into a dict
generate_tsig_response_dict = generate_tsig_response_instance.to_dict()
# create an instance of GenerateTSIGResponse from a dict
generate_tsig_response_from_dict = GenerateTSIGResponse.from_dict(generate_tsig_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


