# DfpCreateOrUpdatePayload

DNS Forwarding Proxy object.  For remote office deployments or in cases where installing an endpoint agent is not desirable or possible, you can use the DNS forwarding proxy. It is a software that runs on bare-metal, VM infrastructures, or Infoblox NIOS appliances; and it embeds the client IPs in DNS queries before forwarding them to Infoblox Cloud. The communications are encrypted and client visibility is maintained. The proxy also provides DNS resolution to local DNS zones when you configure local resolvers. Once you set up a DNS forwarding proxy, it becomes the main DNS server for your remote site. It will also cache responses to speed resolution of future queries.  Note that DNS Forwarding Proxy cannot be created (all information regarding DFP is synchronized from hostapp service).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarding_policy** | **str** | The type of DNS resolver as Forwarding Policy. It can hold values as ib_cloud_first, external_first or external_only The default value is ib_cloud_first. If empty string is sent then ib_cloud_first will be considered. | [optional] 
**host** | [**List[DfpHost]**](DfpHost.md) | host information. For internal Use only. | [optional] 
**id** | **int** | The DNS Forwarding Proxy object identifier. | [optional] [readonly] 
**internal_domain_lists** | **List[int]** | The list of internal domain list ids associated with this DFP (or resolvers) | [optional] 
**name** | **str** | The name of the DNS Forwarding Proxy. | [optional] 
**pop_region_id** | **int** | Point of Presence (PoP) region | [optional] 
**resolvers_all** | [**List[Resolver]**](Resolver.md) | The DNS forwarding proxy additional resolvers used for fallback and local resolution. This field replaces resolvers and default_resolvers fields which are deprecated. Either deprecated fields or new field can be used, both can not be used at same time. | [optional] 
**service_id** | **str** | The DNS Forwarding Proxy Service ID object identifier. | [optional] 
**service_name** | **str** | The name of the DNS Forwarding Proxy Service. | [optional] 
**site_id** | **str** | The DNS Forwarding Proxy site identifier that is appended to DNS queries originating from this DNS Forwarding Proxy and subsequently used for policy lookup purposes. | [optional] 

## Example

```python
from dfp.models.dfp_create_or_update_payload import DfpCreateOrUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of DfpCreateOrUpdatePayload from a JSON string
dfp_create_or_update_payload_instance = DfpCreateOrUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(DfpCreateOrUpdatePayload.to_json())

# convert the object into a dict
dfp_create_or_update_payload_dict = dfp_create_or_update_payload_instance.to_dict()
# create an instance of DfpCreateOrUpdatePayload from a dict
dfp_create_or_update_payload_from_dict = DfpCreateOrUpdatePayload.from_dict(dfp_create_or_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


