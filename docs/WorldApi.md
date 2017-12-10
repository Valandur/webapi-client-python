# swagger_client.WorldApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_world**](WorldApi.md#change_world) | **PUT** /world/{uuid} | Edit world
[**create_world**](WorldApi.md#create_world) | **POST** /world | Create a world
[**delete_world**](WorldApi.md#delete_world) | **DELETE** /world/{uuid} | Delete a world
[**execute_world_method**](WorldApi.md#execute_world_method) | **POST** /world/{uuid} | Execute world methods
[**get_chunk**](WorldApi.md#get_chunk) | **GET** /world/{uuid}/chunk/{x}/{z} | Detailed chunk info
[**get_chunks**](WorldApi.md#get_chunks) | **GET** /world/{uuid}/chunk | Loaded chunk list
[**get_world**](WorldApi.md#get_world) | **GET** /world/{uuid} | Detailed world info
[**get_worlds**](WorldApi.md#get_worlds) | **GET** /world | World list


# **change_world**
> WorldResponse change_world(uuid, update_world_request)

Edit world

Update the properties of an existing world.  > Required permission: world.change 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
uuid = 'uuid_example' # str | The uuid of the world.
update_world_request = swagger_client.UpdateWorldRequest() # UpdateWorldRequest | The new properties of the world

try: 
    # Edit world
    api_response = api_instance.change_world(uuid, update_world_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->change_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the world. | 
 **update_world_request** | [**UpdateWorldRequest**](UpdateWorldRequest.md)| The new properties of the world | 

### Return type

[**WorldResponse**](WorldResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_world**
> WorldResponse create_world(create_world_request)

Create a world

Creates a new world with the specified settings. This does not yet load the world.  > Required permission: world.create 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
create_world_request = swagger_client.CreateWorldRequest() # CreateWorldRequest | 

try: 
    # Create a world
    api_response = api_instance.create_world(create_world_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->create_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_request** | [**CreateWorldRequest**](CreateWorldRequest.md)|  | 

### Return type

[**WorldResponse**](WorldResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_world**
> WorldResponse delete_world(uuid)

Delete a world

Deletes an existing world. **The world must be unloaded before deleting it**  > Required permission: world.delete 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
uuid = 'uuid_example' # str | The uuid of the world.

try: 
    # Delete a world
    api_response = api_instance.delete_world(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->delete_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the world. | 

### Return type

[**WorldResponse**](WorldResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_world_method**
> ExecuteWorldMethodResponse execute_world_method(uuid, request)

Execute world methods

Provides direct access to the underlaying world object and can execute any method on it.  > Required permission: world.method 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
uuid = 'uuid_example' # str | The uuid of the world.
request = swagger_client.RawRequest() # RawRequest | Information about which method to execute.

try: 
    # Execute world methods
    api_response = api_instance.execute_world_method(uuid, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->execute_world_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the world. | 
 **request** | [**RawRequest**](RawRequest.md)| Information about which method to execute. | 

### Return type

[**ExecuteWorldMethodResponse**](ExecuteWorldMethodResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunk**
> ChunkResponse get_chunk(uuid, x, z)

Detailed chunk info

Get detailed information about a chunk  > Required permission: world.chunk.one 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
uuid = 'uuid_example' # str | The uuid of the world.
x = 56 # int | The x-coordinate of the chunk.
z = 56 # int | The z-coordinate of the chunk.

try: 
    # Detailed chunk info
    api_response = api_instance.get_chunk(uuid, x, z)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->get_chunk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the world. | 
 **x** | **int**| The x-coordinate of the chunk. | 
 **z** | **int**| The z-coordinate of the chunk. | 

### Return type

[**ChunkResponse**](ChunkResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunks**
> ChunksResponse get_chunks(uuid)

Loaded chunk list

Gets a list of all the loaded chunks for the specified world.  > Required permission: world.chunk.list 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
uuid = 'uuid_example' # str | The uuid of the world.

try: 
    # Loaded chunk list
    api_response = api_instance.get_chunks(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->get_chunks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the world. | 

### Return type

[**ChunksResponse**](ChunksResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world**
> WorldResponse get_world(uuid, fields=fields, methods=methods)

Detailed world info

Get detailed information about a world.  > Required permission: world.one 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
uuid = 'uuid_example' # str | The uuid of the world to get detailed information about.
fields = 'fields_example' # str | An optional list of additional fields to get. (optional)
methods = 'methods_example' # str | An optional list of additional methods to get. (optional)

try: 
    # Detailed world info
    api_response = api_instance.get_world(uuid, fields=fields, methods=methods)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->get_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the world to get detailed information about. | 
 **fields** | **str**| An optional list of additional fields to get. | [optional] 
 **methods** | **str**| An optional list of additional methods to get. | [optional] 

### Return type

[**WorldResponse**](WorldResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worlds**
> WorldsResponse get_worlds(details=details)

World list

Get a list of all the worlds on the server.  > Required permission: world.list 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WorldApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each world. (optional)

try: 
    # World list
    api_response = api_instance.get_worlds(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldApi->get_worlds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each world. | [optional] 

### Return type

[**WorldsResponse**](WorldsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

