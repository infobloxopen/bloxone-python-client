# fw.SecurityPoliciesApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_security_policy**](SecurityPoliciesApi.md#create_security_policy) | **POST** /security_policies | Create Security Policy.
[**delete_security_policy**](SecurityPoliciesApi.md#delete_security_policy) | **DELETE** /security_policies | Delete Security Policies.
[**delete_single_security_policy**](SecurityPoliciesApi.md#delete_single_security_policy) | **DELETE** /security_policies/{id} | Delete Security Policy.
[**list_security_policies**](SecurityPoliciesApi.md#list_security_policies) | **GET** /security_policies | List Security Policies.
[**read_security_policy**](SecurityPoliciesApi.md#read_security_policy) | **GET** /security_policies/{id} | Read Security Policy.
[**update_security_policy**](SecurityPoliciesApi.md#update_security_policy) | **PUT** /security_policies/{id} | Update Security Policy.


# **create_security_policy**
> SecurityPolicyCreateResponse create_security_policy(body)

Create Security Policy.

Use this method to create a Security Policy object. If no rule list is specified, the newly created Security Policy object will create these rules as a copy of default Security Policy rules (\"Default Global Policy\"). If rule list is provided it must contain at least the complete list of policy rules, including the rules based on all feeds that the account is entitled to. If no network list is specified, networking scope for this policy is empty, thus no action can be performed by this policy. Note that you are not allowed to add DNS Forwarding Proxies and Roaming Device Groups that are already assigned to a Security Policy different from \"Default Global Policy\", to assign them to this Security Policy object you should remove them from other Security Policy first.  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and BloxOne Endpoint groups. BloxOne Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy.  Required: - name    

### Example


```python
import fw
from fw.models.security_policy import SecurityPolicy
from fw.models.security_policy_create_response import SecurityPolicyCreateResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.SecurityPoliciesApi(api_client)
    body = fw.SecurityPolicy() # SecurityPolicy | The Security Policy object.

    try:
        # Create Security Policy.
        api_response = api_instance.create_security_policy(body)
        print("The response of SecurityPoliciesApi->create_security_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPoliciesApi->create_security_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityPolicy**](SecurityPolicy.md)| The Security Policy object. | 

### Return type

[**SecurityPolicyCreateResponse**](SecurityPolicyCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;network_lists&#39; must containt existing Network Lists - &#39;dfps&#39; must contain existing DNS Forwarding Proxies - &#39;roaming_device_groups&#39; must contain existing endpoint devices - &#39;network_lists&#39; cannot contain Network Lists that are already assigned to another Security Policy - Network Lists for the Default Security Policy cannot be updated - &#39;dfps&#39; cannot contain DNS Forwarding Proxies that are already assigned to another Security Policy - DNS Forwarding Proxies for the Default Security Policy cannot be updated - &#39;roaming_device_groups&#39; cannot contain endpoint devices that are already assigned to another Security Policy - endpoint devices for the Default Security Policy cannot be updated - Threat Feed and TI rules must contain licensed threat feeds and TI lists - Threat Feed rules must be unique for the Security Policy |  -  |
**404** |  - Threat Feed and TI rules must contain existing threat feeds and TI lists - Custom Redirect rules must contain existing Custom Redirect - Custom List rules must contain existing Custom List |  -  |
**409** |  - &#39;name&#39; value must be unique among security policies belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_security_policy**
> delete_security_policy(body)

Delete Security Policies.

Use this method to delete Security Policy objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and BloxOne Endpoint groups. BloxOne Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy.  Required: - ids 

### Example


```python
import fw
from fw.models.security_policy_delete_request import SecurityPolicyDeleteRequest
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.SecurityPoliciesApi(api_client)
    body = fw.SecurityPolicyDeleteRequest() # SecurityPolicyDeleteRequest | 

    try:
        # Delete Security Policies.
        api_instance.delete_security_policy(body)
    except Exception as e:
        print("Exception when calling SecurityPoliciesApi->delete_security_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityPolicyDeleteRequest**](SecurityPolicyDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** |  - &#39;ids&#39; value must be non-empty - &#39;ids&#39; value must contain unique elements - &#39;ids&#39; value must contain values that are greater than or equal to zero - &#39;ids&#39; value must contain existing security policy identifiers - default security policy cannot be deleted |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_security_policy**
> delete_single_security_policy(id)

Delete Security Policy.

Use this method to delete Security Policy object by given Security Policy object id.  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and BloxOne Endpoint groups. BloxOne Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy.  

### Example


```python
import fw
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.SecurityPoliciesApi(api_client)
    id = 56 # int | The Security Policy object identifiers.

    try:
        # Delete Security Policy.
        api_instance.delete_single_security_policy(id)
    except Exception as e:
        print("Exception when calling SecurityPoliciesApi->delete_single_security_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Security Policy object identifiers. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** |  - &#39;id&#39; value must contain values that are greater than or equal to zero - &#39;id&#39; value must contain existing security policy identifier - default security policy cannot be deleted |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_security_policies**
> SecurityPolicyMultiResponse list_security_policies(filter=filter, fields=fields, include_access_codes=include_access_codes, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

List Security Policies.

Use this method to retrieve information on all Security Policy objects for the account.  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and BloxOne Endpoint groups. BloxOne Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy.  

### Example


```python
import fw
from fw.models.security_policy_multi_response import SecurityPolicyMultiResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.SecurityPoliciesApi(api_client)
    filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | id                 | int32  | !=, ==, >, <, <=, >=        | | name               | string | !=, ==, ~, !~, >, <, <=, >= | | description        | string | !=, ==, ~, !~, >, <, <=, >= | | is_default         | bool   | !=, ==                      |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Example: ``` ?_filter=\"((name=='sec_policy_a')or(name~'policy_b'))and(is_default!='true')\" ```  (optional)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    include_access_codes = True # bool |  (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    tfilter = 'tfilter_example' # str | Filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | Sorting by tags. (optional)

    try:
        # List Security Policies.
        api_response = api_instance.list_security_policies(filter=filter, fields=fields, include_access_codes=include_access_codes, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)
        print("The response of SecurityPoliciesApi->list_security_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPoliciesApi->list_security_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | id                 | int32  | !&#x3D;, &#x3D;&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;        | | name               | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | description        | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | is_default         | bool   | !&#x3D;, &#x3D;&#x3D;                      |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((name&#x3D;&#x3D;&#39;sec_policy_a&#39;)or(name~&#39;policy_b&#39;))and(is_default!&#x3D;&#39;true&#39;)\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **include_access_codes** | **bool**|  | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| Filtering by tags. | [optional] 
 **torder_by** | **str**| Sorting by tags. | [optional] 

### Return type

[**SecurityPolicyMultiResponse**](SecurityPolicyMultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_security_policy**
> SecurityPolicyReadResponse read_security_policy(id, fields=fields, name=name)

Read Security Policy.

Use this method to retrieve information on the specified Security Policy object.  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and BloxOne Endpoint groups. BloxOne Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy. 

### Example


```python
import fw
from fw.models.security_policy_read_response import SecurityPolicyReadResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.SecurityPoliciesApi(api_client)
    id = 56 # int | The Security Policy object identifier.
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    name = 'name_example' # str |  (optional)

    try:
        # Read Security Policy.
        api_response = api_instance.read_security_policy(id, fields=fields, name=name)
        print("The response of SecurityPoliciesApi->read_security_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPoliciesApi->read_security_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Security Policy object identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**SecurityPolicyReadResponse**](SecurityPolicyReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing security policy identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_security_policy**
> SecurityPolicyUpdateResponse update_security_policy(id, body)

Update Security Policy.

Use this method to update a specified Network List object. The policy data supplied with the update request must have the complete list of policy rules, including the rules based on all feeds that the account is entitled to. If no network list is specified, networking scope for this policy is empty, thus no action can be performed by this policy. Note that you are not allowed to add DNS Forwarding Proxies and Roaming Device Groups that are already assigned to a Security Policy different from \"Default Global Policy\", to assign them to this Security Policy object you should remove them from other Security Policy first.  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and BloxOne Endpoint groups. BloxOne Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy.  Required: - name - rules - dfps - network_lists - roaming_device_groups 

### Example


```python
import fw
from fw.models.security_policy import SecurityPolicy
from fw.models.security_policy_update_response import SecurityPolicyUpdateResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.SecurityPoliciesApi(api_client)
    id = 56 # int | The Security Policy object identifier.
    body = fw.SecurityPolicy() # SecurityPolicy | The Security Policy object.

    try:
        # Update Security Policy.
        api_response = api_instance.update_security_policy(id, body)
        print("The response of SecurityPoliciesApi->update_security_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPoliciesApi->update_security_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Security Policy object identifier. | 
 **body** | [**SecurityPolicy**](SecurityPolicy.md)| The Security Policy object. | 

### Return type

[**SecurityPolicyUpdateResponse**](SecurityPolicyUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;network_lists&#39; must containt existing Network Lists - &#39;dfps&#39; must contain existing DNS Forwarding Proxies - &#39;roaming_device_groups&#39; must contain existing endpoint devices - &#39;network_lists&#39; cannot contain Network Lists that are already assigned to another Security Policy - Network Lists for the Default Security Policy cannot be updated - &#39;dfps&#39; cannot contain DNS Forwarding Proxies that are already assigned to another Security Policy - DNS Forwarding Proxies for the Default Security Policy cannot be updated - &#39;roaming_device_groups&#39; cannot contain endpoint devices that are already assigned to another Security Policy - endpoint devices for the Default Security Policy cannot be updated - Threat Feed and TI rules must contain licensed threat feeds and TI lists - Threat Feed rules must be unique for the Security Policy |  -  |
**404** |  - &#39;id&#39; value must contain existing security policy identifier - Threat Feed and TI rules must contain existing threat feeds and TI lists - Custom Redirect rules must contain existing Custom Redirect - Custom List rules must contain existing Custom List |  -  |
**409** |  - &#39;name&#39; value must be unique among security policies belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

