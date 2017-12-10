# ServerInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**motd** | **str** | The message of the day set on the server. | [optional] 
**players** | **float** | The amount of players currently playing on the server | [optional] 
**max_players** | **float** | The maximum amount of players allowed on the server | [optional] 
**uptime_ticks** | **float** | The number of ticks the server has been running | [optional] 
**tps** | **float** | The average ticks per second the server is running with. 20 is ideal. | [optional] 
**has_whitelist** | **bool** | True if the server has a whitelist, false otherwise. | [optional] 
**minecraft_version** | **str** | The minecraft version running on the server. | [optional] 
**game** | [**ServerInfoDetail**](ServerInfoDetail.md) |  | [optional] 
**api** | [**ServerInfoDetail**](ServerInfoDetail.md) |  | [optional] 
**implementation** | [**ServerInfoDetail**](ServerInfoDetail.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


