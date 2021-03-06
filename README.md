# swagger-client
This is the api for the FerryTix Passenger Ferry Ticketing System, that is both accessible to the vending machines and to other clients.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.faehr_card_uuid_balance_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faehr_card_uuid_balance_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.faehr_card_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faehr_card_uuid_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TopUp() # TopUp | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.faehr_card_uuid_topup_post(body, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faehr_card_uuid_topup_post: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.MachineConfiguration() # MachineConfiguration | 

try:
    api_response = api_instance.machines_default_config_patch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_default_config_patch: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.machines_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.machines_uuid_commands_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_uuid_commands_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.MachineCommand() # MachineCommand | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.machines_uuid_commands_post(body, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_uuid_commands_post: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.MachineConfiguration() # MachineConfiguration | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.machines_uuid_config_patch(body, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_uuid_config_patch: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.machines_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_uuid_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.machines_uuid_status_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_uuid_status_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.MachineStatus() # MachineStatus | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.machines_uuid_status_patch(body, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->machines_uuid_status_patch: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TicketSale() # TicketSale | 

try:
    api_instance.ticket_sales_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->ticket_sales_post: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_instance.ticket_sales_uuid_invalidate_return_delete(uuid)
except ApiException as e:
    print("Exception when calling DefaultApi->ticket_sales_uuid_invalidate_return_delete: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**faehr_card_uuid_balance_get**](docs/DefaultApi.md#faehr_card_uuid_balance_get) | **GET** /faehrCard/{uuid}/balance | 
*DefaultApi* | [**faehr_card_uuid_get**](docs/DefaultApi.md#faehr_card_uuid_get) | **GET** /faehrCard/{uuid} | 
*DefaultApi* | [**faehr_card_uuid_topup_post**](docs/DefaultApi.md#faehr_card_uuid_topup_post) | **POST** /faehrCard/{uuid}/topup | 
*DefaultApi* | [**machines_default_config_patch**](docs/DefaultApi.md#machines_default_config_patch) | **PATCH** /machines/defaultConfig | 
*DefaultApi* | [**machines_get**](docs/DefaultApi.md#machines_get) | **GET** /machines | 
*DefaultApi* | [**machines_uuid_commands_get**](docs/DefaultApi.md#machines_uuid_commands_get) | **GET** /machines/{uuid}/commands | 
*DefaultApi* | [**machines_uuid_commands_post**](docs/DefaultApi.md#machines_uuid_commands_post) | **POST** /machines/{uuid}/commands | 
*DefaultApi* | [**machines_uuid_config_patch**](docs/DefaultApi.md#machines_uuid_config_patch) | **PATCH** /machines/{uuid}/config | 
*DefaultApi* | [**machines_uuid_get**](docs/DefaultApi.md#machines_uuid_get) | **GET** /machines/{uuid} | 
*DefaultApi* | [**machines_uuid_status_get**](docs/DefaultApi.md#machines_uuid_status_get) | **GET** /machines/{uuid}/status | 
*DefaultApi* | [**machines_uuid_status_patch**](docs/DefaultApi.md#machines_uuid_status_patch) | **PATCH** /machines/{uuid}/status | 
*DefaultApi* | [**ticket_sales_post**](docs/DefaultApi.md#ticket_sales_post) | **POST** /ticketSales | 
*DefaultApi* | [**ticket_sales_uuid_invalidate_return_delete**](docs/DefaultApi.md#ticket_sales_uuid_invalidate_return_delete) | **DELETE** /ticketSales/{uuid}/invalidateReturn | 

## Documentation For Models

 - [BankTransferPayment](docs/BankTransferPayment.md)
 - [CashPayment](docs/CashPayment.md)
 - [ECCardPayment](docs/ECCardPayment.md)
 - [FaehrCard](docs/FaehrCard.md)
 - [FaehrCardPayment](docs/FaehrCardPayment.md)
 - [Fare](docs/Fare.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [MachineCommand](docs/MachineCommand.md)
 - [MachineConfiguration](docs/MachineConfiguration.md)
 - [MachineLocation](docs/MachineLocation.md)
 - [MachineStatus](docs/MachineStatus.md)
 - [MachineStatusTicketsSoldToday](docs/MachineStatusTicketsSoldToday.md)
 - [OneOfMachineCommand](docs/OneOfMachineCommand.md)
 - [OneOfPaymentMethod](docs/OneOfPaymentMethod.md)
 - [PayPalPayment](docs/PayPalPayment.md)
 - [Payment](docs/Payment.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [Position](docs/Position.md)
 - [RefillPaperRollCommand](docs/RefillPaperRollCommand.md)
 - [StaffMember](docs/StaffMember.md)
 - [StaffRole](docs/StaffRole.md)
 - [TicketClass](docs/TicketClass.md)
 - [TicketSale](docs/TicketSale.md)
 - [TopUp](docs/TopUp.md)
 - [VendingMachine](docs/VendingMachine.md)
 - [WaitingPassenger](docs/WaitingPassenger.md)

## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

hendrik.lankers.hl@googlemail.com
