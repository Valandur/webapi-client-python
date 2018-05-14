# swagger_client.EntityApi

All URIs are relative to *https://localhost/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity**](EntityApi.md#create_entity) | **POST** /entity | Spawn an entity
[**execute_method**](EntityApi.md#execute_method) | **POST** /entity/{entity}/method | Execute a method
[**get_entity**](EntityApi.md#get_entity) | **GET** /entity/{entity} | Get entity
[**list_entities**](EntityApi.md#list_entities) | **GET** /entity | List entities
[**modify_entity**](EntityApi.md#modify_entity) | **PUT** /entity/{entity} | Modify an entity
[**remove_entity**](EntityApi.md#remove_entity) | **DELETE** /entity/{entity} | Destroy an entity


# **create_entity**
> Entity create_entity(body=body, details=details, accept=accept, pretty=pretty)

Spawn an entity

Creates & Spawns a new entity with the specified properties.     **Required permissions:**    - **entity.create**   

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
api_instance = swagger_client.EntityApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateEntityRequest() # CreateEntityRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Spawn an entity
    api_response = api_instance.create_entity(body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntityRequest**](CreateEntityRequest.md)|  | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_method**
> ExecuteMethodResponse execute_method(entity, body=body, details=details, accept=accept, pretty=pretty)

Execute a method

Provides direct access to the underlaying entity object and can execute any method on it.     **Required permissions:**    - **entity.method**   

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
api_instance = swagger_client.EntityApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | The uuid of the entity
body = swagger_client.ExecuteMethodRequest() # ExecuteMethodRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Execute a method
    api_response = api_instance.execute_method(entity, body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->execute_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**str**](.md)| The uuid of the entity | 
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

# **get_entity**
> Entity get_entity(entity, details=details, accept=accept, pretty=pretty)

Get entity

Get detailed information about an entity.     **Required permissions:**    - **entity.one**   

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
api_instance = swagger_client.EntityApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | The uuid of the entity
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Get entity
    api_response = api_instance.get_entity(entity, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->get_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**str**](.md)| The uuid of the entity | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entities**
> list[Entity] list_entities(world=world, type=type, min=min, max=max, limit=limit, details=details, accept=accept, pretty=pretty)

List entities

Get a list of all entities on the server (in all worlds).     **Required permissions:**    - **entity.list**   

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
api_instance = swagger_client.EntityApi(swagger_client.ApiClient(configuration))
world = 'world_example' # str | The world to filter the entities by (optional)
type = 'type_example' # str | The type id of the entities to filter by (optional)
min = 'min_example' # str | The minimum coordinates at which the entity must be, min=x|y|z (optional)
max = 'max_example' # str | The maximum coordinates at which the entity must be, max=x|y|z (optional)
limit = 56 # int | The maximum amount of entities returned (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # List entities
    api_response = api_instance.list_entities(world=world, type=type, min=min, max=max, limit=limit, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->list_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The world to filter the entities by | [optional] 
 **type** | **str**| The type id of the entities to filter by | [optional] 
 **min** | **str**| The minimum coordinates at which the entity must be, min&#x3D;x|y|z | [optional] 
 **max** | **str**| The maximum coordinates at which the entity must be, max&#x3D;x|y|z | [optional] 
 **limit** | **int**| The maximum amount of entities returned | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**list[Entity]**](Entity.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_entity**
> Entity modify_entity(entity, body=body, details=details, accept=accept, pretty=pretty)

Modify an entity

Modify the properties of an existing entity.     **Required permissions:**    - **entity.modify**   

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
api_instance = swagger_client.EntityApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | The uuid of the entity
body = swagger_client.UpdateEntityRequest() # UpdateEntityRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Modify an entity
    api_response = api_instance.modify_entity(entity, body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->modify_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**str**](.md)| The uuid of the entity | 
 **body** | [**UpdateEntityRequest**](UpdateEntityRequest.md)|  | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity**
> Entity remove_entity(entity, details=details, accept=accept, pretty=pretty)

Destroy an entity

Destroys an entity.     **Required permissions:**    - **entity.delete**   

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
api_instance = swagger_client.EntityApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | The uuid of the entity
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Destroy an entity
    api_response = api_instance.remove_entity(entity, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->remove_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**str**](.md)| The uuid of the entity | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

