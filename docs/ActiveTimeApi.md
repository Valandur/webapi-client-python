# swagger_client.ActiveTimeApi

All URIs are relative to *https://localhost/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_report**](ActiveTimeApi.md#get_server_report) | **GET** /active-time | Server report
[**get_user_report**](ActiveTimeApi.md#get_user_report) | **GET** /active-time/user/{uuid} | User report


# **get_server_report**
> ServerReport get_server_report(details=details, accept=accept, pretty=pretty)

Server report

Generates a report for the whole server from week ago until now     **Required permissions:**    - **active-time.report.server**   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-WebAPI-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-WebAPI-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActiveTimeApi(swagger_client.ApiClient(configuration))
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Server report
    api_response = api_instance.get_server_report(details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveTimeApi->get_server_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**ServerReport**](ServerReport.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_report**
> UserReport get_user_report(uuid, details=details, accept=accept, pretty=pretty)

User report

Generates a report for a specific user from a week ago until now     **Required permissions:**    - **active-time.report.user**   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-WebAPI-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-WebAPI-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActiveTimeApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # User report
    api_response = api_instance.get_user_report(uuid, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveTimeApi->get_user_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**UserReport**](UserReport.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

