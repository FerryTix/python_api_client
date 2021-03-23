# MachineStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vending** | **bool** |  | [optional] 
**battery_charge** | **float** |  | [optional] 
**estimated_receipt_paper_fill_level** | **float** |  | [optional] 
**receipt_paper_roll_length** | **int** |  | [optional] 
**cpu_temperature** | **float** |  | [optional] 
**tickets_sold_today** | [**MachineStatusTicketsSoldToday**](MachineStatusTicketsSoldToday.md) |  | [optional] 
**volume_of_sales_today** | **int** |  | [optional] 
**waiting** | [**list[WaitingPassenger]**](WaitingPassenger.md) |  | [optional] 
**sale_counter** | **int** | Current sale counter. Each vending machine has its own counter, that increases when a sale (TicketSale or TopUp) is completed. The sale counter can&#x27;t be changed from the outside. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

