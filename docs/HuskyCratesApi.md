# swagger_client.HuskyCratesApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_crate**](HuskyCratesApi.md#get_crate) | **GET** /husky/crate/{id} | Detailed crate info
[**get_crates**](HuskyCratesApi.md#get_crates) | **GET** /husky/crate | Crate list


# **get_crate**
> HuskyCrateResponse get_crate(id)

Detailed crate info

Get detailed information about a crate.  > Required permission: husky.crate.one 

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
api_instance = swagger_client.HuskyCratesApi()
id = 'id_example' # str | The id of the crate to get detailed information about.

try: 
    # Detailed crate info
    api_response = api_instance.get_crate(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HuskyCratesApi->get_crate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the crate to get detailed information about. | 

### Return type

[**HuskyCrateResponse**](HuskyCrateResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crates**
> HuskyCratesResponse get_crates(details=details)

Crate list

Get a list of all the crates on the server.  > Required permission: husky.crate.list 

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
api_instance = swagger_client.HuskyCratesApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each crate. (optional)

try: 
    # Crate list
    api_response = api_instance.get_crates(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HuskyCratesApi->get_crates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each crate. | [optional] 

### Return type

[**HuskyCratesResponse**](HuskyCratesResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

