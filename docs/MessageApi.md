# swagger_client.MessageApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message**](MessageApi.md#get_message) | **GET** /message/{uuid} | Detailed message info
[**get_messages**](MessageApi.md#get_messages) | **GET** /message | Message list
[**send_message**](MessageApi.md#send_message) | **POST** /message | Send an interactive message


# **get_message**
> get_message(uuid)

Detailed message info

Get detailed information about a message.  > Required permission: message.one 

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
api_instance = swagger_client.MessageApi()
uuid = 'uuid_example' # str | The uuid of the message to get detailed information about.

try: 
    # Detailed message info
    api_instance.get_message(uuid)
except ApiException as e:
    print("Exception when calling MessageApi->get_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the message to get detailed information about. | 

### Return type

void (empty response body)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> MessagesResponse get_messages(details=details)

Message list

Get a list of all the messages that were sent through the message endpoint since the server started.  > Required permission: message.list 

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
api_instance = swagger_client.MessageApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each message. (optional)

try: 
    # Message list
    api_response = api_instance.get_messages(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each message. | [optional] 

### Return type

[**MessagesResponse**](MessagesResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> MessageResponse send_message(request)

Send an interactive message

Send an interactive message to a player. Make sure to have an event hook for \"custom_message\" to receive the response.  > Required permission: message.create 

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
api_instance = swagger_client.MessageApi()
request = swagger_client.MessageRequest() # MessageRequest | Details of the message sent to the player

try: 
    # Send an interactive message
    api_response = api_instance.send_message(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MessageRequest**](MessageRequest.md)| Details of the message sent to the player | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

