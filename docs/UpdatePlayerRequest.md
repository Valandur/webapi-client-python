# UpdatePlayerRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**world** | **str** | The UUID or name of the world that the player is moved to. | [optional] 
**position** | [**Vector3**](Vector3.md) |  | [optional] 
**velocity** | [**Vector3**](Vector3.md) |  | [optional] 
**rotation** | [**Vector3**](Vector3.md) |  | [optional] 
**scale** | [**Vector3**](Vector3.md) |  | [optional] 
**food_level** | **float** | The new food level of the player. | [optional] 
**exhaustion** | **float** | The new exhaustion level of the player. | [optional] 
**saturation** | **float** | The new saturation level of the player. | [optional] 
**total_experience** | **float** | The total amount of experience the player has. This implicitly also sets the level. | [optional] 
**level** | **float** | The current level of the player. This is also defined by the total amount of experience the player has. | [optional] 
**experience_since_level** | **float** | The amount of experience since the last level up that the player has collected. | [optional] 
**health** | **float** | The current amount of health the player has. | [optional] 
**max_health** | **float** | The total amount of health the player can have at maximum. | [optional] 
**damage** | [**DamageRequest1**](DamageRequest1.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


