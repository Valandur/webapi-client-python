# MobSpawnerData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_nearby_entities** | **int** | The maximum number of nearby entities for another mob to spawn | 
**maximum_spawn_delay** | **int** | The maximum delay between two consecutive spawns | 
**minimum_spawn_delay** | **int** | The minimum delay between two consecutive spawns | 
**next_entity_to_spawn** | [**EntityArchtype**](EntityArchtype.md) | The next entity type that will be spawned by this spawner | 
**possible_entities_to_spawn** | [**list[TableEntryEntityArchetype]**](TableEntryEntityArchetype.md) | A weighted table of probability for each entity type to spawn | 
**remaining_delay** | **int** | The remaining time until the next spawn attempt | 
**required_player_range** | **int** | The block range within there must be a player to trigger the spawn | 
**spawn_count** | **int** | The amount of entities that will spawn in one attempt | 
**spawn_range** | **int** | The range from the spawner within which the entities will spawn | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


