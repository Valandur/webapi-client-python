# swagger_client.PluginApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plugin**](PluginApi.md#get_plugin) | **GET** /plugin/{id} | Detailed plugin info
[**get_plugins**](PluginApi.md#get_plugins) | **GET** /plugin | Plugin list


# **get_plugin**
> PluginResponse get_plugin(id)

Detailed plugin info

Gets detailed information about a plugin.  > Required permission: plugin.one 

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
api_instance = swagger_client.PluginApi()
id = 'id_example' # str | The id of the plugin to get detailed information about.

try: 
    # Detailed plugin info
    api_response = api_instance.get_plugin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApi->get_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the plugin to get detailed information about. | 

### Return type

[**PluginResponse**](PluginResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins**
> PluginsResponse get_plugins()

Plugin list

Get a list of all the plugins running on the server.  > Required permission: plugin.list 

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
api_instance = swagger_client.PluginApi()

try: 
    # Plugin list
    api_response = api_instance.get_plugins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApi->get_plugins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PluginsResponse**](PluginsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

