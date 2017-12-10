# MessageFull

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The unique UUID assigned to the message by the Web-API. | [optional] 
**id** | **str** | The id of the message. This will be sent back in the reply, so you can identify the request. | [optional] 
**target** | **str** | The UUID of the player this message is sent to. | [optional] 
**message** | **str** | The message sent to the player. Text formatting can be applied with ampersand formatting. | [optional] 
**once** | **bool** | True if the target can only select one response for this message (further responses are not sent to the webhook endpoint)  | [optional] 
**options** | [**list[MessageOption]**](MessageOption.md) | These are the options the player can choose from. The key is sent back to the server, the value is displayed to the player.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


