# BlockOperationNew

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action to perform. &#x60;GET&#x60; to fetch world blocks, &#x60;UPDATE&#x60; to change world blocks. | 
**world** | **str** | The UUID of the world that the block update is applied to.  Either the property &#x60;block&#x60; or &#x60;blocks&#x60; has to be set.  If the property &#x60;block&#x60; is set then all the blocks within the area defined by &#x60;min&#x60; and &#x60;max&#x60; are changed to the specified block.  If the property &#x60;blocks&#x60; is set then it defines nested arrays of the blocks within the area defined by &#x60;min&#x60; and &#x60;max&#x60;. The arrays should contain the blocks such that a block located at [min.X + x, min.Y + y, min.Z + z] can be accessed by &#x60;blocks[x][y][z]&#x60;, where &#x60;min&#x60; is the vecotor defined by the &#x60;min&#x60; property.  | 
**min** | [**Vector3**](Vector3.md) |  | 
**max** | [**Vector3**](Vector3.md) |  | 
**block** | [**BlockFull**](BlockFull.md) |  | [optional] 
**blocks** | **list[list[list[BlockFull]]]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


