# swagger_client.TileEntityApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_tile_entity_method**](TileEntityApi.md#execute_tile_entity_method) | **POST** /tile-entity/{worldUuid}/{x}/{y}/{z} | Execute tile entity methods
[**get_tile_entities**](TileEntityApi.md#get_tile_entities) | **GET** /tile-entity | Tile entities list
[**get_tile_entity**](TileEntityApi.md#get_tile_entity) | **GET** /tile-entity/{worldUuid}/{x}/{y}/{z} | Detailed tile entity info


# **execute_tile_entity_method**
> ExecuteTileEntityMethodResponse execute_tile_entity_method(world_uuid, x, y, z, request)

Execute tile entity methods

Provides direct access to the underlaying tile entity object and can execute any method on it.  > Required permission: tile-entity.method 

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
api_instance = swagger_client.TileEntityApi()
world_uuid = 'world_uuid_example' # str | The uuid of the world the tile entity is in.
x = 56 # int | The x-coordinate of the tile entity.
y = 56 # int | The y-coordinate of the tile entity.
z = 56 # int | The z-coordinate of the tile entity.
request = swagger_client.RawRequest() # RawRequest | Information about which method to execute.

try: 
    # Execute tile entity methods
    api_response = api_instance.execute_tile_entity_method(world_uuid, x, y, z, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TileEntityApi->execute_tile_entity_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_uuid** | **str**| The uuid of the world the tile entity is in. | 
 **x** | **int**| The x-coordinate of the tile entity. | 
 **y** | **int**| The y-coordinate of the tile entity. | 
 **z** | **int**| The z-coordinate of the tile entity. | 
 **request** | [**RawRequest**](RawRequest.md)| Information about which method to execute. | 

### Return type

[**ExecuteTileEntityMethodResponse**](ExecuteTileEntityMethodResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tile_entities**
> TileEntitiesResponse get_tile_entities(world=world, type=type, limit=limit)

Tile entities list

Get a list of all tile entities on the server (in all worlds, unless specified).  > Required permission: tile-entity.list 

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
api_instance = swagger_client.TileEntityApi()
world = 'world_example' # str | The uuid of the world to filter entities by. (optional)
type = 'type_example' # str | The TileEntityType id to filter the tile entities by. (optional)
limit = 'limit_example' # str | The maximum amount of tile entities to return. (optional)

try: 
    # Tile entities list
    api_response = api_instance.get_tile_entities(world=world, type=type, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TileEntityApi->get_tile_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world to filter entities by. | [optional] 
 **type** | **str**| The TileEntityType id to filter the tile entities by. | [optional] 
 **limit** | **str**| The maximum amount of tile entities to return. | [optional] 

### Return type

[**TileEntitiesResponse**](TileEntitiesResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tile_entity**
> TileEntityResponse get_tile_entity(world_uuid, x, y, z, fields=fields, methods=methods)

Detailed tile entity info

Get detailed information about a tile entity.  > Required permission: tile-entity.one 

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
api_instance = swagger_client.TileEntityApi()
world_uuid = 'world_uuid_example' # str | The uuid of the world the tile entity is in.
x = 56 # int | The x-coordinate of the tile entity.
y = 56 # int | The y-coordinate of the tile entity.
z = 56 # int | The z-coordinate of the tile entity.
fields = 'fields_example' # str | An optional list of additional fields to get. (optional)
methods = 'methods_example' # str | An optional list of additional methods to get. (optional)

try: 
    # Detailed tile entity info
    api_response = api_instance.get_tile_entity(world_uuid, x, y, z, fields=fields, methods=methods)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TileEntityApi->get_tile_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_uuid** | **str**| The uuid of the world the tile entity is in. | 
 **x** | **int**| The x-coordinate of the tile entity. | 
 **y** | **int**| The y-coordinate of the tile entity. | 
 **z** | **int**| The z-coordinate of the tile entity. | 
 **fields** | **str**| An optional list of additional fields to get. | [optional] 
 **methods** | **str**| An optional list of additional methods to get. | [optional] 

### Return type

[**TileEntityResponse**](TileEntityResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

