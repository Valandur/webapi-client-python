# Chunk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | The API link that can be used to obtain more information about this object | 
**loaded** | **bool** | True if this chunk is currently loaded, false otherwise | 
**position** | [**Vector3i**](Vector3i.md) | The position of this chunk (in chunk coordinates) | 
**uuid** | **str** | The unique id of this chunk | 
**block_max** | [**Vector3i**](Vector3i.md) | The bock with the largest coordinates that is still part of this chunk | [optional] 
**block_min** | [**Vector3i**](Vector3i.md) | The bock with the smallest coordinates that is still part of this chunk | [optional] 
**inhabited_time** | **int** | The total amount of time (in server ticks) this chunk has been inhabited by players. | [optional] 
**regional_difficulty_factor** | **float** | The increase in difficulty due to the presence of players in the chunk | [optional] 
**regional_difficulty_percentage** | **float** | The increase in difficulty due to the presence of players in the chunk as a percentage | [optional] 
**world** | [**World**](World.md) | The world the chunk is in | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


