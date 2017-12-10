# swagger_client.ChunkApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chunk**](ChunkApi.md#get_chunk) | **GET** /world/{uuid}/chunk/{x}/{z} | Detailed chunk info
[**get_chunks**](ChunkApi.md#get_chunks) | **GET** /world/{uuid}/chunk | Loaded chunk list


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
api_instance = swagger_client.ChunkApi()
uuid = 'uuid_example' # str | The uuid of the world.
x = 56 # int | The x-coordinate of the chunk.
z = 56 # int | The z-coordinate of the chunk.

try: 
    # Detailed chunk info
    api_response = api_instance.get_chunk(uuid, x, z)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChunkApi->get_chunk: %s\n" % e)
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
api_instance = swagger_client.ChunkApi()
uuid = 'uuid_example' # str | The uuid of the world.

try: 
    # Loaded chunk list
    api_response = api_instance.get_chunks(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChunkApi->get_chunks: %s\n" % e)
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

