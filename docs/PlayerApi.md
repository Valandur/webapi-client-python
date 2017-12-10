# swagger_client.PlayerApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_player**](PlayerApi.md#change_player) | **PUT** /player/{uuid} | Edit player
[**execute_player_method**](PlayerApi.md#execute_player_method) | **POST** /player/{uuid} | Execute player method
[**get_player**](PlayerApi.md#get_player) | **GET** /player/{uuid} | Detailed player info
[**get_players**](PlayerApi.md#get_players) | **GET** /player | Player list


# **change_player**
> PlayerResponse change_player(uuid, update_player_request)

Edit player

Update the properties of an existing player.  > Required permission: player.change 

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
api_instance = swagger_client.PlayerApi()
uuid = 'uuid_example' # str | The uuid of the player.
update_player_request = swagger_client.UpdatePlayerRequest() # UpdatePlayerRequest | The new properties of the player

try: 
    # Edit player
    api_response = api_instance.change_player(uuid, update_player_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->change_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the player. | 
 **update_player_request** | [**UpdatePlayerRequest**](UpdatePlayerRequest.md)| The new properties of the player | 

### Return type

[**PlayerResponse**](PlayerResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_player_method**
> ExecutePlayerMethodResponse execute_player_method(uuid, request)

Execute player method

Provides direct access to the underlaying player object and can execute any method on it.  > Required permission: player.method 

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
api_instance = swagger_client.PlayerApi()
uuid = 'uuid_example' # str | The uuid of the player.
request = swagger_client.RawRequest() # RawRequest | Information about which method to execute.

try: 
    # Execute player method
    api_response = api_instance.execute_player_method(uuid, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->execute_player_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the player. | 
 **request** | [**RawRequest**](RawRequest.md)| Information about which method to execute. | 

### Return type

[**ExecutePlayerMethodResponse**](ExecutePlayerMethodResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player**
> PlayerResponse get_player(uuid, fields=fields, methods=methods)

Detailed player info

Get detailed information about a player.  > Required permission: player.one 

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
api_instance = swagger_client.PlayerApi()
uuid = 'uuid_example' # str | The uuid of the player to get detailed information about.
fields = 'fields_example' # str | An optional list of additional fields to get. (optional)
methods = 'methods_example' # str | An optional list of additional methods to get. (optional)

try: 
    # Detailed player info
    api_response = api_instance.get_player(uuid, fields=fields, methods=methods)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the player to get detailed information about. | 
 **fields** | **str**| An optional list of additional fields to get. | [optional] 
 **methods** | **str**| An optional list of additional methods to get. | [optional] 

### Return type

[**PlayerResponse**](PlayerResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_players**
> PlayersList get_players()

Player list

Get a list of all the players on the server.  > Required permission: player.list 

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
api_instance = swagger_client.PlayerApi()

try: 
    # Player list
    api_response = api_instance.get_players()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_players: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlayersList**](PlayersList.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

