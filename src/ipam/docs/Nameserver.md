# Nameserver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_principal** | **str** | The Kerberos principal name. It uses the typical Kerberos notation: &lt;SERVICE-NAME&gt;/&lt;server-domain-name&gt;@&lt;REALM&gt;.  Defaults to empty. | [optional] 
**gss_tsig_fallback** | **bool** | The behavior when GSS-TSIG should be used (a matching external DNS server is configured) but no GSS-TSIG key is available. If configured to _false_ (the default) this DNS server is skipped, if configured to _true_ the DNS server is ignored and the DNS update is sent with the configured DHCP-DDNS protection e.g. TSIG key or without any protection when none was configured.  Defaults to _false_. | [optional] 
**kerberos_rekey_interval** | **int** | Time interval (in seconds) the keys for each configured external DNS server are checked for rekeying, i.e. a new key is created to replace the current usable one when its age is greater than the _kerberos_rekey_interval_ value.  Defaults to 120 seconds. | [optional] 
**kerberos_retry_interval** | **int** | Time interval (in seconds) to retry to create a key if any error occurred previously for any configured external DNS server.  Defaults to 30 seconds. | [optional] 
**kerberos_tkey_lifetime** | **int** | Lifetime (in seconds) of GSS-TSIG keys in the TKEY protocol.  Defaults to 160 seconds. | [optional] 
**kerberos_tkey_protocol** | **str** | Determines which protocol is used to establish the security context with the external DNS servers, TCP or UDP.  Defaults to _tcp_. | [optional] 
**nameserver** | **str** |  | [optional] 
**server_principal** | **str** | The Kerberos principal name of this DNS server that will receive updates.  Defaults to empty. | [optional] 

## Example

```python
from ipam.models.nameserver import Nameserver

# TODO update the JSON string below
json = "{}"
# create an instance of Nameserver from a JSON string
nameserver_instance = Nameserver.from_json(json)
# print the JSON string representation of the object
print(Nameserver.to_json())

# convert the object into a dict
nameserver_dict = nameserver_instance.to_dict()
# create an instance of Nameserver from a dict
nameserver_from_dict = Nameserver.from_dict(nameserver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


