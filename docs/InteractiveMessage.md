# InteractiveMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the message. Used for sender of the message to identify responses. | 
**link** | **str** | The API link that can be used to obtain more information about this object | 
**target** | **str** | The target of the message, usually this is a player UUID. Can be set to \&quot;server\&quot; to send to all online players. | 
**uuid** | **str** | The unique UUID of this message | 
**message** | **str** | The actual content of the message | [optional] 
**once** | **bool** | True if this message can only be replied to once per target, false otherwise | [optional] 
**options** | [**list[InteractiveMessageOption]**](InteractiveMessageOption.md) | Clickable options that the player can select from | [optional] 
**targets** | **list[str]** | A list of targets that will receive the message. Usually a list of player UUIDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


