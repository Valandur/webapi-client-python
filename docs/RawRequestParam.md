# RawRequestParam

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the parameter. This defines how the value is interpreted. | [optional] 
**value** | **object** | The value of the parameter. Base types (like integer, float, boolean, etc.) are converted to the correct type and then passed to the method. Some parameters are handled differently, they are listed below along with their usage:  - class: Interpreted as the fully qualified classname of a class which is loaded and passed | - vector3(i/d): Converted to a Vector3(i/d) object. Requires the properties \&quot;x\&quot;, \&quot;y\&quot; and \&quot;z\&quot; - text: Converted to a sponge text - world: Assumed to be the UUID of a world which is fetched and passed - player: Assumed to be the UUID of the player which is fetched and passed. - itemstack: Converted to a new item stack. Requires the properties \&quot;itemType\&quot; and \&quot;amount\&quot;  | [optional] 
**optional** | **bool** | True if the value should be wrapped into an optional value, false otherwise. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


