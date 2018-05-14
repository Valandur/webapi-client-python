# swagger_client.MapApi

All URIs are relative to *https://localhost/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_map**](MapApi.md#get_map) | **GET** /map/{world}/{x}/{z} | Get a map tile


# **get_map**
> get_map(world, x, z, details=details, accept=accept, pretty=pretty)

Get a map tile

Returns an image representing the biomes of the blocks within the specified tile     **Required permissions:**    - **map.map**   

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
api_instance = swagger_client.MapApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The world to get the map tile from
x = 56 # int | The x-coordinate of the tile (is multiplied by the TILE_SIZE)
z = 56 # int | The z-coordinate of the tile (is multiplied by the TILE_SIZE)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Get a map tile
    api_instance.get_map(world, x, z, details=details, accept=accept, pretty=pretty)
except ApiException as e:
    print("Exception when calling MapApi->get_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The world to get the map tile from | 
 **x** | **int**| The x-coordinate of the tile (is multiplied by the TILE_SIZE) | 
 **z** | **int**| The z-coordinate of the tile (is multiplied by the TILE_SIZE) | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

