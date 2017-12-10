# NationsZone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The unique uuid of this zone. | [optional] 
**name** | **str** | The name of the zone. | [optional] 
**rect** | [**NationsRect**](NationsRect.md) |  | [optional] 
**owner** | [**Player**](Player.md) |  | [optional] 
**co_owners** | [**list[Player]**](Player.md) | The list of co-owners of this zone. | [optional] 
**flags** | **object** | A map of boolean flags. | [optional] 
**for_sale** | **bool** | True if this zone is for sale, false otherwise. | [optional] 
**price** | **str** | The price of this zone. **This is a string because this number might be too large to hold in a regular number object.** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


