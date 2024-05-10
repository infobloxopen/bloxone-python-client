# BgpNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** |  | [optional] 
**asn_text** | **str** | Examples:     ASDOT        ASPLAIN     INTEGER     VALID/INVALID     0.1          1           1           Valid     1            1           1           Valid     65535        65535       65535       Valid     0.65535      65535       65535       Valid     1.0          65536       65536       Valid     1.1          65537       65537       Valid     1.65535      131071      131071      Valid     65535.0      4294901760  4294901760  Valid     65535.1      4294901761  4294901761  Valid     65535.65535  4294967295  4294967295  Valid      0.65536                              Invalid     65535.655536                         Invalid     65536.0                              Invalid     65536.65535                          Invalid                  4294967296              Invalid | [optional] 
**ip_address** | **str** | IPv4 address of the BGP neighbor | [optional] 
**max_hop_count** | **int** |  | [optional] 
**multihop** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from anycast.models.bgp_neighbor import BgpNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of BgpNeighbor from a JSON string
bgp_neighbor_instance = BgpNeighbor.from_json(json)
# print the JSON string representation of the object
print(BgpNeighbor.to_json())

# convert the object into a dict
bgp_neighbor_dict = bgp_neighbor_instance.to_dict()
# create an instance of BgpNeighbor from a dict
bgp_neighbor_from_dict = BgpNeighbor.from_dict(bgp_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


