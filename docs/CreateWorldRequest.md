# CreateWorldRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the world. | [optional] 
**seed** | **float** | The seed number. A random seed is generated if not provided. | [optional] 
**generator** | **str** | The id of the generator type to use. Check &#x60;/registry/org.spongepowered.api.world.GeneratorType&#x60;. | [optional] 
**game_mode** | **str** | The id of the game mode to use. Check &#x60;/registry/org.spongepowered.api.entity.living.player.gamemode.GameMode&#x60;. | [optional] 
**difficulty** | **str** | The id of the difficutly to use. Check &#x60;/registry/org.spongepowered.api.world.difficulty.Difficulty&#x60;. | [optional] 
**load_on_startup** | **bool** | True if the world is loaded when the server starts, false otherwise. | [optional] 
**keep_spawn_loaded** | **bool** | True to keep the spawn area of the world loaded, even if it is empty. | [optional] 
**allow_commands** | **bool** | True if executing commands is allowed in the world. | [optional] 
**uses_map_features** | **bool** | True to use map features of the generator (such as villages). | [optional] 
**dimension** | **str** | The dimension of the world to use. Check &#x60;/registry/org.spongepowered.api.world.DimensionType&#x60;. | [optional] 
**generate_bonus_chest** | **bool** | True to generate bonus chests, false otherwise. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


