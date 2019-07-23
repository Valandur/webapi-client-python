# RedProtectRegion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of this region | 
**link** | **str** | The API link that can be used to obtain more information about this object | 
**max** | [**Vector3d**](Vector3d.md) | The maximum coordinates that define the region | 
**min** | [**Vector3d**](Vector3d.md) | The minimum coordinates that define the region | 
**name** | **str** | The name of this region | 
**world** | [**World**](World.md) | The world this region is located in | 
**admins** | [**list[Player]**](Player.md) | A list of players that are admins of this region | [optional] 
**can_delete** | **bool** | True if this region can be deleted, false otherwise | [optional] 
**_date** | **str** | The date this region was created? | [optional] 
**flags** | **dict(str, object)** | A map of flags applicable to this region | [optional] 
**leaders** | [**list[Player]**](Player.md) | A list of players that are leaders of this region | [optional] 
**members** | [**list[Player]**](Player.md) | A list of players that are members of this region | [optional] 
**priority** | **int** | The priority of this region compared to other regions | [optional] 
**tp_point** | [**Location**](Location.md) | The teleport point for this region | [optional] 
**welcome_message** | **str** | The welcome message displayed to a player when they enter this region | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


