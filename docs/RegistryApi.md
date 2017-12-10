# swagger_client.RegistryApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_values**](RegistryApi.md#get_catalog_values) | **GET** /registry/{className} | List catalog values


# **get_catalog_values**
> CatalogTypesResponse get_catalog_values(class_name)

List catalog values

Lists all the catalog values of a specified CatalogType.  > Required permission: registry.one 

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
api_instance = swagger_client.RegistryApi()
class_name = 'class_name_example' # str | The fully qualified class name of the CatalogType to get.

try: 
    # List catalog values
    api_response = api_instance.get_catalog_values(class_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_catalog_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_name** | **str**| The fully qualified class name of the CatalogType to get. | 

### Return type

[**CatalogTypesResponse**](CatalogTypesResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

