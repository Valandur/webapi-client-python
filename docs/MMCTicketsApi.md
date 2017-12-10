# swagger_client.MMCTicketsApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_ticket**](MMCTicketsApi.md#change_ticket) | **PUT** /mmctickets/ticket/{id} | Edit ticket
[**get_ticket**](MMCTicketsApi.md#get_ticket) | **GET** /mmctickets/ticket/{id} | Detailed ticket info
[**get_tickets**](MMCTicketsApi.md#get_tickets) | **GET** /mmctickets/ticket | Ticket list


# **change_ticket**
> MMCTicketsTicketResponse change_ticket(id, update_ticket_request)

Edit ticket

Update the properties of an existing ticket.  > Required permission: mmctickets.ticket.change 

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
api_instance = swagger_client.MMCTicketsApi()
id = 'id_example' # str | The id of the ticket.
update_ticket_request = swagger_client.MMCUpdateTicketRequest() # MMCUpdateTicketRequest | The new properties of the ticket

try: 
    # Edit ticket
    api_response = api_instance.change_ticket(id, update_ticket_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MMCTicketsApi->change_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the ticket. | 
 **update_ticket_request** | [**MMCUpdateTicketRequest**](MMCUpdateTicketRequest.md)| The new properties of the ticket | 

### Return type

[**MMCTicketsTicketResponse**](MMCTicketsTicketResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket**
> MMCTicketsTicketResponse get_ticket(id)

Detailed ticket info

Get detailed information about a ticket.  > Required permission: mmctickets.ticket.one 

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
api_instance = swagger_client.MMCTicketsApi()
id = 'id_example' # str | The id of the ticket to get detailed information about.

try: 
    # Detailed ticket info
    api_response = api_instance.get_ticket(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MMCTicketsApi->get_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the ticket to get detailed information about. | 

### Return type

[**MMCTicketsTicketResponse**](MMCTicketsTicketResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets**
> MMCTicketsTicketsResponse get_tickets(details=details)

Ticket list

Get a list of all the tickets on the server.  > Required permission: mmtickets.ticket.list 

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
api_instance = swagger_client.MMCTicketsApi()
details = 'details_example' # str | Pass this parameter to receive the full details for each ticket. (optional)

try: 
    # Ticket list
    api_response = api_instance.get_tickets(details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MMCTicketsApi->get_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **str**| Pass this parameter to receive the full details for each ticket. | [optional] 

### Return type

[**MMCTicketsTicketsResponse**](MMCTicketsTicketsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

