# ContentCategory

The Content Category object.  The Content Category object represents a specific internet content and used to configure category filters. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. BloxOne Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many categories and sub-categories as you need.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_code** | **int** | The category code. | [optional] 
**category_name** | **str** | The name of the category. | [optional] 
**functional_group** | **str** | The functional group name of the category. | [optional] 

## Example

```python
from fw.models.content_category import ContentCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ContentCategory from a JSON string
content_category_instance = ContentCategory.from_json(json)
# print the JSON string representation of the object
print(ContentCategory.to_json())

# convert the object into a dict
content_category_dict = content_category_instance.to_dict()
# create an instance of ContentCategory from a dict
content_category_from_dict = ContentCategory.from_dict(content_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


