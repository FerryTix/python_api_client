# TopUp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**_for** | **str** | UUID of the FaehrCard the TopUp is for. | [optional] 
**issued_at** | **datetime** |  | [optional] 
**issued_by** | **str** | The id of the vending machine that the topup has been purchased at. Is null if purchased online | [optional] 
**amount** | **int** |  | [optional] 
**paid** | **int** |  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**initial** | **bool** | Describes whether the top up was done when the card was issued | [optional] 
**signature** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

