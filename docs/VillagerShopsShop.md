# VillagerShopsShop

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**CatalogTypeEntityType**](CatalogTypeEntityType.md) | The minecraft entity type string for this shops visual entity | 
**link** | **str** | The API link that can be used to obtain more information about this object | 
**entity_variant** | **str** | A very dynamic variant string for vanilla mobs, most variants as in the minecraft wiki should be supported | [optional] 
**location** | [**Location**](Location.md) | Where the shop is currently located | [optional] 
**name** | **str** | The escaped shop name | [optional] 
**owner** | **str** | If this shop is a player shop this conatins the UUID of this shops owner. Omitting this field or setting it to null will remove the player-shop association. | [optional] 
**rotation** | **float** | The mobs roations around their up-axis | [optional] 
**stock_container** | [**Location**](Location.md) | Location where a container should reside for stocking items. Omitting this field or setting it to null will remove the stock container. Having a player-shop without container is undefined behaviour! | [optional] 
**stock_items** | [**list[VillagerShopsStockItem]**](VillagerShopsStockItem.md) | Returns a list of all stock items currently listed. This property is read only. | [optional] 
**uid** | **str** | The unique shop identifier; this is not the mob uuid | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


