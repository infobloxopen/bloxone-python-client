# ThreatFeed

The Threat Feed object.  BloxOne Cloud provides predefined threat intelligence feeds based on your subscription. The Plus subscription offers a few more feeds than the Standard subscription. The Advanced subscription offers a few more feeds than the Plus subscription. A threat feed subscription for RPZ updates offers protection against malicious hostnames.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_level** | **str** | The Confidence Level of the Feed. | [optional] [readonly] 
**description** | **str** | The brief description for the thread feed. | [optional] [readonly] 
**key** | **str** | The TSIG key of the threat feed. | [optional] [readonly] 
**name** | **str** | The name of the thread feed. | [optional] [readonly] 
**source** | [**ThreatFeedSource**](ThreatFeedSource.md) |  | [optional] 
**threat_level** | **str** | The Threat Level of the Feed. | [optional] [readonly] 

## Example

```python
from fw.models.threat_feed import ThreatFeed

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatFeed from a JSON string
threat_feed_instance = ThreatFeed.from_json(json)
# print the JSON string representation of the object
print(ThreatFeed.to_json())

# convert the object into a dict
threat_feed_dict = threat_feed_instance.to_dict()
# create an instance of ThreatFeed from a dict
threat_feed_from_dict = ThreatFeed.from_dict(threat_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


