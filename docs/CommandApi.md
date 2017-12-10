# swagger_client.CommandApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_command**](CommandApi.md#execute_command) | **POST** /cmd | Execute command
[**get_command**](CommandApi.md#get_command) | **GET** /cmd/{name} | Detailed command info
[**get_commands**](CommandApi.md#get_commands) | **GET** /cmd | Command list


# **execute_command**
> ExecuteCommandResponse execute_command(request)

Execute command

Execute a command on the server. (Almost the same as running it from the console). Pass a list of commands to execute them in succession, if only passing one command the array is not required.  > Required permission: cmd.run > Required permission: cmd.run.[command] 

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
api_instance = swagger_client.CommandApi()
request = [swagger_client.CommandRequest()] # list[CommandRequest] | The command and arguments sent to the server

try: 
    # Execute command
    api_response = api_instance.execute_command(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandApi->execute_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**list[CommandRequest]**](CommandRequest.md)| The command and arguments sent to the server | 

### Return type

[**ExecuteCommandResponse**](ExecuteCommandResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command**
> CommandResponse1 get_command(name)

Detailed command info

Get detailed information about a command.  > Required permission: cmd.one 

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
api_instance = swagger_client.CommandApi()
name = 'name_example' # str | The name (main alias) of the command

try: 
    # Detailed command info
    api_response = api_instance.get_command(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandApi->get_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name (main alias) of the command | 

### Return type

[**CommandResponse1**](CommandResponse1.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commands**
> CommandsResponse get_commands()

Command list

Gets a list of all the commands available on the server.  > Required permission: cmd.list 

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
api_instance = swagger_client.CommandApi()

try: 
    # Command list
    api_response = api_instance.get_commands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandApi->get_commands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommandsResponse**](CommandsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

