# swagger_client.PlayerApi

All URIs are relative to *https://localhost/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_method**](PlayerApi.md#execute_method) | **POST** /player/{player}/method | Execute a method
[**get_player**](PlayerApi.md#get_player) | **GET** /player/{player} | Get a player
[**list_players**](PlayerApi.md#list_players) | **GET** /player | List players
[**modify_player**](PlayerApi.md#modify_player) | **PUT** /player/{player} | Modify a player


# **execute_method**
> ExecuteMethodResponse execute_method(player, body=body, details=details, accept=accept, pretty=pretty)

Execute a method

Provides direct access to the underlying player object and can execute any method on it.     **Required permissions:**    - **player.method**   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-WebAPI-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-WebAPI-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
player = 'player_example' # str | The uuid of the player
body = swagger_client.ExecuteMethodRequest() # ExecuteMethodRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Execute a method
    api_response = api_instance.execute_method(player, body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->execute_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | **str**| The uuid of the player | 
 **body** | [**ExecuteMethodRequest**](ExecuteMethodRequest.md)|  | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**ExecuteMethodResponse**](ExecuteMethodResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player**
> Player get_player(player, details=details, accept=accept, pretty=pretty)

Get a player

Get detailed information about a player.     **Required permissions:**    - **player.one**   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-WebAPI-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-WebAPI-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
player = 'player_example' # str | The uuid of the player
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Get a player
    api_response = api_instance.get_player(player, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | **str**| The uuid of the player | 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Player**](Player.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_players**
> list[Player] list_players(details=details, accept=accept, pretty=pretty)

List players

Get a list of all the players on the server.     **Required permissions:**    - **player.list**   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-WebAPI-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-WebAPI-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # List players
    api_response = api_instance.list_players(details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->list_players: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**list[Player]**](Player.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_player**
> Player modify_player(player, body=body, details=details, accept=accept, pretty=pretty)

Modify a player

Modify the properties of an existing player.     **Required permissions:**    - **player.modify**   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-WebAPI-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-WebAPI-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
player = 'player_example' # str | The uuid of the player
body = swagger_client.UpdatePlayerRequest() # UpdatePlayerRequest |  (optional)
details = true # bool | Add to include additional details, omit or false otherwise (optional)
accept = 'accept_example' # str | Override the 'Accept' request header (useful for debugging your requests) (optional)
pretty = true # bool | Add to make the Web-API pretty print the response (useful for debugging your requests) (optional)

try:
    # Modify a player
    api_response = api_instance.modify_player(player, body=body, details=details, accept=accept, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->modify_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | **str**| The uuid of the player | 
 **body** | [**UpdatePlayerRequest**](UpdatePlayerRequest.md)|  | [optional] 
 **details** | **bool**| Add to include additional details, omit or false otherwise | [optional] 
 **accept** | **str**| Override the &#39;Accept&#39; request header (useful for debugging your requests) | [optional] 
 **pretty** | **bool**| Add to make the Web-API pretty print the response (useful for debugging your requests) | [optional] 

### Return type

[**Player**](Player.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

