# ThreatFeedMultiResponse

The Threat Feed list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ThreatFeed]**](ThreatFeed.md) | The list of Threat Feed objects. | [optional] 

## Example

```python
from fw.models.threat_feed_multi_response import ThreatFeedMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatFeedMultiResponse from a JSON string
threat_feed_multi_response_instance = ThreatFeedMultiResponse.from_json(json)
# print the JSON string representation of the object
print(ThreatFeedMultiResponse.to_json())

# convert the object into a dict
threat_feed_multi_response_dict = threat_feed_multi_response_instance.to_dict()
# create an instance of ThreatFeedMultiResponse from a dict
threat_feed_multi_response_from_dict = ThreatFeedMultiResponse.from_dict(threat_feed_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


