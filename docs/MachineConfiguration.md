# MachineConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_machine** | **str** | The machine id for which to apply these settings. May be left empty in a POST request if applicable for all machines. | [optional] 
**max_bicycles** | **int** |  | [optional] 
**max_bicycles_tolerance** | **int** | Tolerance fot the maximal amount of passengers carrying a bicycle in the waiting area. This will determine, to what extend the maximum may be exceeded in some situations. | [optional] 
**max_passengers** | **int** |  | [optional] 
**max_passengers_tolerance** | **int** | Tolerance fot the maximal amount of passengers in the waiting area. This will determine, to what extend the maximum may be exceeded in some situations. | [optional] 
**fares** | [**list[Fare]**](Fare.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

