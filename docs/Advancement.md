# Advancement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the advancement | 
**name** | **str** | The name of the advancement | 
**title** | **str** | The title of the advancement | 
**announce_to_chat** | **bool** | True if the achieving of this advancement is announced in chat, false otherwise | [optional] 
**description** | **str** | The description of the advancement | [optional] 
**hidden** | **bool** | True if this is a hidden advancement | [optional] 
**parent** | [**Advancement**](Advancement.md) | The parent advancement, which must be unlocked prior to this advancement | [optional] 
**show_toast** | **bool** | True if achieving this advancement shows the player a toast message, false otherwise | [optional] 
**tree** | [**CatalogTypeAdvancementTree**](CatalogTypeAdvancementTree.md) | The advancement tree that this advancement belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


