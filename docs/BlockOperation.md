# BlockOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The error message, if any | 
**estimated_seconds_remaining** | **float** | The estimated amount of time remaining until this block operation is complete (in seconds) | 
**link** | **str** | The API link that can be used to obtain more information about this object | 
**max** | [**Vector3i**](Vector3i.md) | The maximum block belonging to this operation | 
**min** | [**Vector3i**](Vector3i.md) | The minimum block belonging to this operation | 
**progress** | **float** | The current progress of the block operation, from 0 (&#x3D;started) to 1 (&#x3D;finished) | 
**status** | **str** | The current status of the block operation | 
**type** | **str** | The type of block operation | 
**uuid** | **str** | The unique UUID identifying this block operation | 
**world** | [**World**](World.md) | The world in which this block operation is running | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


