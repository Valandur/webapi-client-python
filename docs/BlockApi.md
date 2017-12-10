# swagger_client.BlockApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_block_operation**](BlockApi.md#cancel_block_operation) | **DELETE** /block/op/{uuid} | Cancel block operation
[**change_block_operation**](BlockApi.md#change_block_operation) | **PUT** /block/op/{uuid} | Modify block operation
[**get_block**](BlockApi.md#get_block) | **GET** /block/{world}/{x}/{y}/{z} | Get one block
[**get_block_operation**](BlockApi.md#get_block_operation) | **GET** /block/op/{uuid} | Block operation details
[**get_block_operations**](BlockApi.md#get_block_operations) | **GET** /block/op | List block operations
[**start_block_operation**](BlockApi.md#start_block_operation) | **POST** /block/op | Create block operation


# **cancel_block_operation**
> BlockOperationResponse cancel_block_operation(uuid)

Cancel block operation

Cancel a pending or running block operation. **THIS DOES NOT UNDO THE BLOCK CHANGES**  > Required permission: block.op.delete 

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
api_instance = swagger_client.BlockApi()
uuid = 'uuid_example' # str | The uuid of the block operation.

try: 
    # Cancel block operation
    api_response = api_instance.cancel_block_operation(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->cancel_block_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the block operation. | 

### Return type

[**BlockOperationResponse**](BlockOperationResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_block_operation**
> BlockOperationResponse change_block_operation(uuid, data)

Modify block operation

Modify an existing block operation to either pause or continue it.  > Required permission: block.op.change 

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
api_instance = swagger_client.BlockApi()
uuid = 'uuid_example' # str | The uuid of the block operation.
data = swagger_client.Data() # Data | The new data applied to the block operation.

try: 
    # Modify block operation
    api_response = api_instance.change_block_operation(uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->change_block_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the block operation. | 
 **data** | [**Data**](Data.md)| The new data applied to the block operation. | 

### Return type

[**BlockOperationResponse**](BlockOperationResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block**
> SingleBlock get_block(world, x, y, z)

Get one block

Gets information about one block in the world.  > Required permission: block.one 

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
api_instance = swagger_client.BlockApi()
world = 'world_example' # str | The uuid of the world the block is in.
x = 56 # int | The x-coordinate of the block.
y = 56 # int | The y-coordinate of the block.
z = 56 # int | The z-coordinate of the block.

try: 
    # Get one block
    api_response = api_instance.get_block(world, x, y, z)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->get_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world** | **str**| The uuid of the world the block is in. | 
 **x** | **int**| The x-coordinate of the block. | 
 **y** | **int**| The y-coordinate of the block. | 
 **z** | **int**| The z-coordinate of the block. | 

### Return type

[**SingleBlock**](SingleBlock.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_operation**
> BlockOperationResponse get_block_operation(uuid)

Block operation details

Gets details about a specific block operation  > Required permission: block.op.one 

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
api_instance = swagger_client.BlockApi()
uuid = 'uuid_example' # str | The uuid of the block operation.

try: 
    # Block operation details
    api_response = api_instance.get_block_operation(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->get_block_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the block operation. | 

### Return type

[**BlockOperationResponse**](BlockOperationResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_operations**
> BlockOperationsList get_block_operations()

List block operations

Returns a list of all the currently running block operations.  > Required permission: block.op.list 

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
api_instance = swagger_client.BlockApi()

try: 
    # List block operations
    api_response = api_instance.get_block_operations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->get_block_operations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockOperationsList**](BlockOperationsList.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_block_operation**
> BlockOperationResponse start_block_operation(request)

Create block operation

Start a request to get or change blocks on the server.  > Required permission: block.op.create 

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
api_instance = swagger_client.BlockApi()
request = [swagger_client.BlockOperationNew()] # list[BlockOperationNew] | The requested changes to blocks

try: 
    # Create block operation
    api_response = api_instance.start_block_operation(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->start_block_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**list[BlockOperationNew]**](BlockOperationNew.md)| The requested changes to blocks | 

### Return type

[**BlockOperationResponse**](BlockOperationResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

