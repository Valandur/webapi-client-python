# swagger_client.NucleusApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_jail**](NucleusApi.md#get_jail) | **GET** /nucleus/jail/{name} | Detailed jail info
[**get_jails**](NucleusApi.md#get_jails) | **GET** /nucleus/jail | Jail list
[**get_kit**](NucleusApi.md#get_kit) | **GET** /nucleus/kit/{name} | Detailed kit info
[**get_kits**](NucleusApi.md#get_kits) | **GET** /nucleus/kit | Kit list


# **get_jail**
> NucleusJailResponse get_jail(name)

Detailed jail info

Get detailed information about a jail.  > Required permission: nucleus.jail.one 

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
api_instance = swagger_client.NucleusApi()
name = 'name_example' # str | The name of the jail to get detailed information about.

try: 
    # Detailed jail info
    api_response = api_instance.get_jail(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_jail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the jail to get detailed information about. | 

### Return type

[**NucleusJailResponse**](NucleusJailResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jails**
> NucleusJailsResponse get_jails(details=details)

Jail list

Get a list of all the jails on the server.  > Required permission: nucleus.jail.list 

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
api_instance = swagger_client.NucleusApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each jail. (optional)

try: 
    # Jail list
    api_response = api_instance.get_jails(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_jails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each jail. | [optional] 

### Return type

[**NucleusJailsResponse**](NucleusJailsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kit**
> NucleusKitResponse get_kit(name)

Detailed kit info

Get detailed information about a kit.  > Required permission: nucleus.kit.one 

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
api_instance = swagger_client.NucleusApi()
name = 'name_example' # str | The name of the kit to get detailed information about.

try: 
    # Detailed kit info
    api_response = api_instance.get_kit(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the kit to get detailed information about. | 

### Return type

[**NucleusKitResponse**](NucleusKitResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kits**
> NucleusKitsResponse get_kits(details=details)

Kit list

Get a list of all the kits on the server.  > Required permission: nucleus.kit.list 

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
api_instance = swagger_client.NucleusApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each kit. (optional)

try: 
    # Kit list
    api_response = api_instance.get_kits(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NucleusApi->get_kits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each kit. | [optional] 

### Return type

[**NucleusKitsResponse**](NucleusKitsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

