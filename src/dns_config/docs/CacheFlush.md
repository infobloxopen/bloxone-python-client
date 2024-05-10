# CacheFlush

The _dns/cache_flush_ API removes entries from the DNS cache on the on-prem host. The command will be forwarded to the on-prem host and executed asynchronously. The on-prem host must be available and running DNS for this to succeed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flush_subdomains** | **bool** | Optional. If _true_, all names below the given FQDN will also be removed from cache.  Defaults to _true_. | [optional] 
**fqdn** | **str** | Optional. The FQDN to remove.  Defaults to &#39;.&#39; | [optional] 
**ophid** | **str** | The host to alter. Either _ophid_ or _service_id_ should be provided. | [optional] 
**service_id** | **str** | Service Id. Either _ophid_ or _service_id_ should be provided. | [optional] 
**ttl** | **int** | Optional. The time in seconds the command is valid for. Command is executed on the onprem host only if it takes less than this time for the command to be transmitted to the host. Otherwise the onprem host discards this command.  Defaults to 120 (2 min). | [optional] 
**view_name** | **str** | Optional, If provided, flushes the server&#39;s cache for a view. | [optional] 

## Example

```python
from dns_config.models.cache_flush import CacheFlush

# TODO update the JSON string below
json = "{}"
# create an instance of CacheFlush from a JSON string
cache_flush_instance = CacheFlush.from_json(json)
# print the JSON string representation of the object
print(CacheFlush.to_json())

# convert the object into a dict
cache_flush_dict = cache_flush_instance.to_dict()
# create an instance of CacheFlush from a dict
cache_flush_from_dict = CacheFlush.from_dict(cache_flush_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


