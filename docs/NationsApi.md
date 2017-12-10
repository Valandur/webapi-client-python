# swagger_client.NationsApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nation**](NationsApi.md#get_nation) | **GET** /nations/nation/{id} | Detailed nation info
[**get_nations**](NationsApi.md#get_nations) | **GET** /nations/nation | Nations list


# **get_nation**
> NationsNationResponse get_nation(id)

Detailed nation info

Get detailed information about a nation.  > Required permission: nations.nation.one 

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
api_instance = swagger_client.NationsApi()
id = 'id_example' # str | The id of the nation to get detailed information about.

try: 
    # Detailed nation info
    api_response = api_instance.get_nation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NationsApi->get_nation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the nation to get detailed information about. | 

### Return type

[**NationsNationResponse**](NationsNationResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nations**
> NationsNationsResponse get_nations(details=details)

Nations list

Get a list of all the nations on the server.  > Required permission: nations.nation.list 

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
api_instance = swagger_client.NationsApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each nation. (optional)

try: 
    # Nations list
    api_response = api_instance.get_nations(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NationsApi->get_nations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each nation. | [optional] 

### Return type

[**NationsNationsResponse**](NationsNationsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

