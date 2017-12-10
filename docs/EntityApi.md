# swagger_client.EntityApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_entity**](EntityApi.md#change_entity) | **PUT** /entity/{uuid} | Edit entity
[**create_entity**](EntityApi.md#create_entity) | **POST** /entity | Create an entity
[**destroy_entity**](EntityApi.md#destroy_entity) | **DELETE** /entity/{uuid} | Destroy an entity
[**execute_entity_method**](EntityApi.md#execute_entity_method) | **POST** /entity/{uuid} | Execute entity method
[**get_entities**](EntityApi.md#get_entities) | **GET** /entity | Entities list
[**get_entity**](EntityApi.md#get_entity) | **GET** /entity/{uuid} | Detailed entity info


# **change_entity**
> EntityResponse change_entity(uuid, update_entity_request)

Edit entity

Update the properties of an existing entity.  > Required permission: entity.change 

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
api_instance = swagger_client.EntityApi()
uuid = 'uuid_example' # str | The uuid of the entity.
update_entity_request = swagger_client.UpdateEntityRequest() # UpdateEntityRequest | The new properties of the entity

try: 
    # Edit entity
    api_response = api_instance.change_entity(uuid, update_entity_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->change_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the entity. | 
 **update_entity_request** | [**UpdateEntityRequest**](UpdateEntityRequest.md)| The new properties of the entity | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> EntityResponse create_entity(create_entity_request)

Create an entity

Creates & Spawns a new entity with the specified properties.  > Required permission: entity.create 

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
api_instance = swagger_client.EntityApi()
create_entity_request = swagger_client.CreateEntityRequest() # CreateEntityRequest | 

try: 
    # Create an entity
    api_response = api_instance.create_entity(create_entity_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_entity_request** | [**CreateEntityRequest**](CreateEntityRequest.md)|  | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_entity**
> EntityResponse destroy_entity(uuid)

Destroy an entity

Destroys an entity.  > Required permission: entity.delete 

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
api_instance = swagger_client.EntityApi()
uuid = 'uuid_example' # str | The uuid of the entity.

try: 
    # Destroy an entity
    api_response = api_instance.destroy_entity(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->destroy_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the entity. | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_entity_method**
> EntityMethodResult execute_entity_method(uuid, request)

Execute entity method

Provides direct access to the underlaying entity object and can execute any method on it.  > Required permission: entity.method 

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
api_instance = swagger_client.EntityApi()
uuid = 'uuid_example' # str | The uuid of the entity.
request = swagger_client.RawRequest() # RawRequest | Information about which method to execute.

try: 
    # Execute entity method
    api_response = api_instance.execute_entity_method(uuid, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->execute_entity_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the entity. | 
 **request** | [**RawRequest**](RawRequest.md)| Information about which method to execute. | 

### Return type

[**EntityMethodResult**](EntityMethodResult.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities**
> EntitiesList get_entities(details=details)

Entities list

Get a list of all entities on the server (in all worlds).  > Required permission: entity.list 

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
api_instance = swagger_client.EntityApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each entity. (optional)

try: 
    # Entities list
    api_response = api_instance.get_entities(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->get_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each entity. | [optional] 

### Return type

[**EntitiesList**](EntitiesList.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> EntityResponse get_entity(uuid, fields=fields, methods=methods)

Detailed entity info

Get detailed information about an entity.  > Required permission: entity.one 

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
api_instance = swagger_client.EntityApi()
uuid = 'uuid_example' # str | The uuid of the entity to get detailed information about.
fields = 'fields_example' # str | An optional list of additional fields to get. (optional)
methods = 'methods_example' # str | An optional list of additional methods to get. (optional)

try: 
    # Detailed entity info
    api_response = api_instance.get_entity(uuid, fields=fields, methods=methods)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->get_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the entity to get detailed information about. | 
 **fields** | **str**| An optional list of additional fields to get. | [optional] 
 **methods** | **str**| An optional list of additional methods to get. | [optional] 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

