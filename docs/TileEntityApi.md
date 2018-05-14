# swagger_client.TileEntityApi

All URIs are relative to *https://localhost/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_method**](TileEntityApi.md#execute_method) | **POST** /tile-entity/{world}/{x}/{y}/{z}/method | Execute a method
[**get_tile_entity**](TileEntityApi.md#get_tile_entity) | **GET** /tile-entity/{world}/{x}/{y}/{z} | Get tile entity
[**list_tile_entities**](TileEntityApi.md#list_tile_entities) | **GET** /tile-entity | List tile entities


# **execute_method**
> ExecuteMethodResponse execute_method(world, x, y, z, body=body, details=details, accept=accept, pretty=pretty)

Execute a method

Provides direct access to the underlaying tile entity object and can execute any method on it.     **Required permissions:**    - **tile-entity.method**   

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
api_instance = swagger_client.TileEntityApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The world the tile entity is in
x = 56 # int | The x-coordinate of the tile-entity
y = 56 # int | The x-coordinate of the tile-entity
z = 56 # int | The x-coordinate of the tile-entity
body = swagger_client.ExecuteMethodRequest() # ExecuteMethodRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Execute a method
    api_response = api_instance.execute_method(world, x, y, z, body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TileEntityApi->execute_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The world the tile entity is in | 
 **x** | **int**| The x-coordinate of the tile-entity | 
 **y** | **int**| The x-coordinate of the tile-entity | 
 **z** | **int**| The x-coordinate of the tile-entity | 
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

# **get_tile_entity**
> TileEntity get_tile_entity(world, x, y, z, details=details, accept=accept, pretty=pretty)

Get tile entity

Get detailed information about a tile entity.     **Required permissions:**    - **tile-entity.one**   

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
api_instance = swagger_client.TileEntityApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The world the tile entity is in
x = 56 # int | The x-coordinate of the tile-entity
y = 56 # int | The y-coordinate of the tile-entity
z = 56 # int | The z-coordinate of the tile-entity
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Get tile entity
    api_response = api_instance.get_tile_entity(world, x, y, z, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TileEntityApi->get_tile_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The world the tile entity is in | 
 **x** | **int**| The x-coordinate of the tile-entity | 
 **y** | **int**| The y-coordinate of the tile-entity | 
 **z** | **int**| The z-coordinate of the tile-entity | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**TileEntity**](TileEntity.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tile_entities**
> list[TileEntity] list_tile_entities(world=world, type=type, min=min, max=max, limit=limit, details=details, accept=accept, pretty=pretty)

List tile entities

Get a list of all tile entities on the server (in all worlds, unless specified).     **Required permissions:**    - **tile-entity.list**   

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
api_instance = swagger_client.TileEntityApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The world to filter tile entities by (optional)
type = 'type_example' # str | The type if of tile entities to filter by (optional)
min = 'min_example' # str | The minimum coordinates at which the tile entity must be, min=x|y|z (optional)
max = 'max_example' # str | The maximum coordinates at which the tile entity must be, max=x|y|z (optional)
limit = 56 # int | The maximum amount of tile entities returned (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # List tile entities
    api_response = api_instance.list_tile_entities(world=world, type=type, min=min, max=max, limit=limit, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TileEntityApi->list_tile_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The world to filter tile entities by | [optional] 
 **type** | **str**| The type if of tile entities to filter by | [optional] 
 **min** | **str**| The minimum coordinates at which the tile entity must be, min&#x3D;x|y|z | [optional] 
 **max** | **str**| The maximum coordinates at which the tile entity must be, max&#x3D;x|y|z | [optional] 
 **limit** | **int**| The maximum amount of tile entities returned | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**list[TileEntity]**](TileEntity.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

