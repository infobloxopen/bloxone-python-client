# UtilizationThreshold

A __UtilizationThreshold__ object represents IP address utilization threshold settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the utilization threshold for IP addresses is enabled or not. | 
**high** | **int** | The high threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test. | 
**low** | **int** | The low threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test. | 

## Example

```python
from ipam.models.utilization_threshold import UtilizationThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of UtilizationThreshold from a JSON string
utilization_threshold_instance = UtilizationThreshold.from_json(json)
# print the JSON string representation of the object
print(UtilizationThreshold.to_json())

# convert the object into a dict
utilization_threshold_dict = utilization_threshold_instance.to_dict()
# create an instance of UtilizationThreshold from a dict
utilization_threshold_from_dict = UtilizationThreshold.from_dict(utilization_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


