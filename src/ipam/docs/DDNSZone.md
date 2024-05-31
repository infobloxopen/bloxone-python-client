# DDNSZone

A __DDNSZone__ object (_dhcp/ddns_zone_) represents a DNS zone that can accept dynamic DNS updates from DHCP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Zone FQDN.  If _zone_ is defined, the _fqdn_ field must be empty. | [optional] 
**gss_tsig_enabled** | **bool** | _gss_tsig_enabled_ enables/disables GSS-TSIG signed dynamic updates.  Defaults to _false_. | [optional] 
**nameservers** | [**List[Nameserver]**](Nameserver.md) | The Nameservers in the zone.  Each nameserver IP should be unique across the list of nameservers. | [optional] 
**tsig_enabled** | **bool** | Indicates if TSIG key should be used for the update.  Defaults to _false_. | [optional] 
**tsig_key** | [**TSIGKey**](TSIGKey.md) | The TSIG key. Required if _tsig_enabled_ is _true_.  Defaults to empty. | [optional] 
**view** | **str** | The resource identifier. | [optional] 
**view_name** | **str** | The name of the view. | [optional] [readonly] 
**zone** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.ddns_zone import DDNSZone

# TODO update the JSON string below
json = "{}"
# create an instance of DDNSZone from a JSON string
ddns_zone_instance = DDNSZone.from_json(json)
# print the JSON string representation of the object
print(DDNSZone.to_json())

# convert the object into a dict
ddns_zone_dict = ddns_zone_instance.to_dict()
# create an instance of DDNSZone from a dict
ddns_zone_from_dict = DDNSZone.from_dict(ddns_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


