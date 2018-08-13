# swagger_client.ChunkApi

All URIs are relative to *https://localhost/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chunk_at**](ChunkApi.md#create_chunk_at) | **POST** /chunk/{world}/{x}/{z} | Load &amp; Generate a chunk
[**get_chunk_at**](ChunkApi.md#get_chunk_at) | **GET** /chunk/{world}/{x}/{z} | Get a chunk
[**list_chunks**](ChunkApi.md#list_chunks) | **GET** /chunk/{world} | List chunks


# **create_chunk_at**
> Chunk create_chunk_at(world, x, z, details=details, accept=accept, pretty=pretty)

Load & Generate a chunk

Forces a chunk to be loaded into memory, and created if it does not exist.     **Required permissions:**    - **chunk.create**   

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
api_instance = swagger_client.ChunkApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The uuid of the world in which to create the chunk
x = 56 # int | The x-coordinate of the chunk (in chunk coordinates)
z = 56 # int | The z-coordinate of the chunk (in chunk coordinates)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Load & Generate a chunk
    api_response = api_instance.create_chunk_at(world, x, z, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChunkApi->create_chunk_at: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world in which to create the chunk | 
 **x** | **int**| The x-coordinate of the chunk (in chunk coordinates) | 
 **z** | **int**| The z-coordinate of the chunk (in chunk coordinates) | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Chunk**](Chunk.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunk_at**
> Chunk get_chunk_at(world, x, z, details=details, accept=accept, pretty=pretty)

Get a chunk

Get detailed information about a chunk     **Required permissions:**    - **chunk.one**   

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
api_instance = swagger_client.ChunkApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The uuid of the world in which to get the chunk
x = 56 # int | The x-coordinate of the chunk (in chunk coordinates)
z = 56 # int | The z-coordinate of the chunk (in chunk coordinates)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Get a chunk
    api_response = api_instance.get_chunk_at(world, x, z, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChunkApi->get_chunk_at: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world in which to get the chunk | 
 **x** | **int**| The x-coordinate of the chunk (in chunk coordinates) | 
 **z** | **int**| The z-coordinate of the chunk (in chunk coordinates) | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Chunk**](Chunk.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_chunks**
> list[Chunk] list_chunks(world, details=details, accept=accept, pretty=pretty)

List chunks

Gets a list of all the loaded chunks for the specified world.     **Required permissions:**    - **chunk.list**   

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
api_instance = swagger_client.ChunkApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The uuid of the for which to get all chunks
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # List chunks
    api_response = api_instance.list_chunks(world, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChunkApi->list_chunks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the for which to get all chunks | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**list[Chunk]**](Chunk.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

