# CPSubnet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**cidr** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**ip_space_name** | **str** |  | [optional] 
**ip_space_ref** | **str** | The resource identifier. | [optional] 
**name** | **str** |  | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** |  | [optional] 

## Example

```python
from ipam.models.cp_subnet import CPSubnet

# TODO update the JSON string below
json = "{}"
# create an instance of CPSubnet from a JSON string
cp_subnet_instance = CPSubnet.from_json(json)
# print the JSON string representation of the object
print(CPSubnet.to_json())

# convert the object into a dict
cp_subnet_dict = cp_subnet_instance.to_dict()
# create an instance of CPSubnet from a dict
cp_subnet_from_dict = CPSubnet.from_dict(cp_subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


