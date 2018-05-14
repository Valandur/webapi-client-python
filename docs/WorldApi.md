# swagger_client.WorldApi

All URIs are relative to *https://localhost/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_world**](WorldApi.md#create_world) | **POST** /world | Create a world
[**delete_world**](WorldApi.md#delete_world) | **DELETE** /world/{world} | Delete a world
[**execute_method**](WorldApi.md#execute_method) | **POST** /world/{world}/method | Execute a method
[**get_world**](WorldApi.md#get_world) | **GET** /world/{world} | Get a world
[**list_worlds**](WorldApi.md#list_worlds) | **GET** /world | List worlds
[**modify_world**](WorldApi.md#modify_world) | **PUT** /world/{world} | Modify a world


# **create_world**
> WorldFull create_world(body=body, details=details, accept=accept, pretty=pretty)

Create a world

Creates a new world with the specified settings. This does not yet load the world.     **Required permissions:**    - **world.create**   

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
api_instance = swagger_client.WorldApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWorldRequest() # CreateWorldRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Create a world
    api_response = api_instance.create_world(body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->create_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorldRequest**](CreateWorldRequest.md)|  | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**WorldFull**](WorldFull.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_world**
> WorldFull delete_world(world, details=details, accept=accept, pretty=pretty)

Delete a world

Deletes an existing world. **The world must be unloaded before deleting it**     **Required permissions:**    - **world.delete**   

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
api_instance = swagger_client.WorldApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The uuid of the world to delete
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Delete a world
    api_response = api_instance.delete_world(world, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->delete_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world to delete | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**WorldFull**](WorldFull.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_method**
> ExecuteMethodResponse execute_method(world, body=body, details=details, accept=accept, pretty=pretty)

Execute a method

Provides direct access to the underlaying world object and can execute any method on it.     **Required permissions:**    - **world.method**   

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
api_instance = swagger_client.WorldApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The uuid of the world on which to execute the method
body = swagger_client.ExecuteMethodRequest() # ExecuteMethodRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Execute a method
    api_response = api_instance.execute_method(world, body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->execute_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world on which to execute the method | 
 **body** | [**ExecuteMethodRequest**](ExecuteMethodRequest.md)|  | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**ExecuteMethodResponse**](ExecuteMethodResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world**
> WorldFull get_world(world, details=details, accept=accept, pretty=pretty)

Get a world

Get detailed information about a world.     **Required permissions:**    - **world.one**   

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
api_instance = swagger_client.WorldApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The uuid of the world for which to get details
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Get a world
    api_response = api_instance.get_world(world, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->get_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world for which to get details | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**WorldFull**](WorldFull.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_worlds**
> list[WorldFull] list_worlds(details=details, accept=accept, pretty=pretty)

List worlds

Get a list of all the worlds on the server.     **Required permissions:**    - **world.list**   

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
api_instance = swagger_client.WorldApi(swagger_client.ApiClient(configuration))
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # List worlds
    api_response = api_instance.list_worlds(details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->list_worlds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**list[WorldFull]**](WorldFull.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_world**
> WorldFull modify_world(world, body=body, details=details, accept=accept, pretty=pretty)

Modify a world

Modify the properties of an existing world.     **Required permissions:**    - **world.modify**   

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
api_instance = swagger_client.WorldApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The uuid of the world which to update
body = swagger_client.UpdateWorldRequest() # UpdateWorldRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Modify a world
    api_response = api_instance.modify_world(world, body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->modify_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world which to update | 
 **body** | [**UpdateWorldRequest**](UpdateWorldRequest.md)|  | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**WorldFull**](WorldFull.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

