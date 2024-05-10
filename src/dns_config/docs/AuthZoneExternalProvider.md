# AuthZoneExternalProvider

The external provider object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the external provider. | [optional] [readonly] 
**name** | **str** | The name of the external provider. | [optional] 
**type** | **str** | Defines the type of external provider. Allowed values:  * _bloxone_ddi_: host type is BloxOne DDI,  * _microsoft_azure_: host type is Microsoft Azure,  * _amazon_web_service_: host type is Amazon Web Services,  * _microsoft_active_directory_: host type is Microsoft Active Directory,  * _google_cloud_platform_: host type is Google Cloud Platform. | [optional] 

## Example

```python
from dns_config.models.auth_zone_external_provider import AuthZoneExternalProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthZoneExternalProvider from a JSON string
auth_zone_external_provider_instance = AuthZoneExternalProvider.from_json(json)
# print the JSON string representation of the object
print(AuthZoneExternalProvider.to_json())

# convert the object into a dict
auth_zone_external_provider_dict = auth_zone_external_provider_instance.to_dict()
# create an instance of AuthZoneExternalProvider from a dict
auth_zone_external_provider_from_dict = AuthZoneExternalProvider.from_dict(auth_zone_external_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


