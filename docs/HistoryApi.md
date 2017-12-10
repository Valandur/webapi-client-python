# swagger_client.HistoryApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chat_history**](HistoryApi.md#get_chat_history) | **GET** /history/chat | Chat History
[**get_command_history**](HistoryApi.md#get_command_history) | **GET** /history/cmd | Command History


# **get_chat_history**
> ChatHistoryResponse get_chat_history()

Chat History

View a history of the server chat.  > Required permission: history.chat 

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
api_instance = swagger_client.HistoryApi()

try: 
    # Chat History
    api_response = api_instance.get_chat_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->get_chat_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ChatHistoryResponse**](ChatHistoryResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_history**
> CommandHistoryResponse get_command_history()

Command History

View a history of the server commands.  > Required permission: history.cmd 

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
api_instance = swagger_client.HistoryApi()

try: 
    # Command History
    api_response = api_instance.get_command_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->get_command_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommandHistoryResponse**](CommandHistoryResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

