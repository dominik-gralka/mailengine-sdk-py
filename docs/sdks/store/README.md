# Store
(*store*)

## Overview

Access to Petstore orders

Find out more about our store
<http://swagger.io>
### Available Operations

* [get_inventory](#get_inventory) - Returns pet inventories by status
* [place_order](#place_order) - Place an order for a pet
* [get_order_by_id](#get_order_by_id) - Find purchase order by ID
* [delete_order](#delete_order) - Delete purchase order by ID

## get_inventory

Returns a map of status codes to quantities

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.store.get_inventory()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetInventoryResponse](../../models/operations/getinventoryresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## place_order

Place a new order in the store

### Example Usage

```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.store.place_order(request=components.Order(
    id=10,
    pet_id=198772,
    quantity=7,
    status=components.OrderStatus.APPROVED,
))

if res.order is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [components.Order](../../models/components/order.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.PlaceOrderResponse](../../models/operations/placeorderresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_order_by_id

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.store.get_order_by_id(order_id=614993)

if res.order is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `order_id`                           | *int*                                | :heavy_check_mark:                   | ID of order that needs to be fetched |


### Response

**[operations.GetOrderByIDResponse](../../models/operations/getorderbyidresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## delete_order

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.store.delete_order(order_id=127902)

if res.order is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `order_id`                               | *int*                                    | :heavy_check_mark:                       | ID of the order that needs to be deleted |


### Response

**[operations.DeleteOrderResponse](../../models/operations/deleteorderresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |
