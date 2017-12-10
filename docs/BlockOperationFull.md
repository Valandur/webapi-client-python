# BlockOperationFull

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The UUID of the block update operation. | [optional] 
**type** | **str** | The type of action that is being performed by this operation. | [optional] 
**status** | **str** | The current status of the operation, one of: INIT, RUNNING, PAUSED, DONE, ERRORED.  | [optional] 
**progress** | **float** | The update progress of this operation, from 0 (nothing done) to 1 (completely done). | [optional] 
**est_time_remaining** | **float** | The estimated amount of seconds remaining before this operation is completed. | [optional] 
**link** | **str** | The Web-API url to access for details about this operation. | [optional] 
**min** | [**Vector3**](Vector3.md) |  | [optional] 
**max** | [**Vector3**](Vector3.md) |  | [optional] 
**blocks** | **list[list[list[BlockFull]]]** | This array is only present if this is a BlockGetOperation. Contains the blocks that have already been scanned. All other values (blocks yet to be scanned) are set to null.  | [optional] 
**error** | **str** | Any error that occured during execution. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


