# CategoryFilter

The Category Filter object.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | The list of content category names that falls into this category filter. | [optional] 
**created_time** | **datetime** | The time when this Category Filter object was created. | [optional] [readonly] 
**description** | **str** | The brief description for the category filter. | [optional] 
**id** | **int** | The Category Filter object identifier. | [optional] [readonly] 
**name** | **str** | The name of the category filter. | [optional] 
**policies** | **List[str]** | The list of security policy names with which the category filter is associated. | [optional] [readonly] 
**tags** | **object** | Enables tag support for resource where tags attribute contains user-defined key value pairs | [optional] 
**updated_time** | **datetime** | The time when this Category Filter object was last updated. | [optional] [readonly] 

## Example

```python
from fw.models.category_filter import CategoryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryFilter from a JSON string
category_filter_instance = CategoryFilter.from_json(json)
# print the JSON string representation of the object
print(CategoryFilter.to_json())

# convert the object into a dict
category_filter_dict = category_filter_instance.to_dict()
# create an instance of CategoryFilter from a dict
category_filter_from_dict = CategoryFilter.from_dict(category_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


