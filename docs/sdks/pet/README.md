# Pet
(*pet*)

## Overview

Everything about your Pets

Find out more
<http://swagger.io>
### Available Operations

* [update_pet](#update_pet) - Update an existing pet
* [add_pet](#add_pet) - Add a new pet to the store
* [find_pets_by_status](#find_pets_by_status) - Finds Pets by status
* [find_pets_by_tags](#find_pets_by_tags) - Finds Pets by tags
* [get_pet_by_id](#get_pet_by_id) - Find pet by ID
* [delete_pet](#delete_pet) - Deletes a pet
* [upload_file](#upload_file) - uploads an image

## update_pet

Update an existing pet by Id

### Example Usage

```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.pet.update_pet(request=components.Pet(
    name='doggie',
    photo_urls=[
        '<value>',
    ],
    id=10,
    category=components.Category(
        id=1,
        name='Dogs',
    ),
))

if res.pet is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [components.Pet](../../models/components/pet.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.UpdatePetResponse](../../models/operations/updatepetresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## add_pet

Add a new pet to the store

### Example Usage

```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.pet.add_pet(request=components.Pet(
    name='doggie',
    photo_urls=[
        '<value>',
    ],
    id=10,
    category=components.Category(
        id=1,
        name='Dogs',
    ),
))

if res.pet is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [components.Pet](../../models/components/pet.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.AddPetResponse](../../models/operations/addpetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## find_pets_by_status

Multiple status values can be provided with comma separated strings

### Example Usage

```python
import mailengine
from mailengine.models import operations

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.pet.find_pets_by_status(status=operations.Status.AVAILABLE)

if res.pets is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `status`                                                         | [Optional[operations.Status]](../../models/operations/status.md) | :heavy_minus_sign:                                               | Status values that need to be considered for filter              |


### Response

**[operations.FindPetsByStatusResponse](../../models/operations/findpetsbystatusresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## find_pets_by_tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.pet.find_pets_by_tags(tags=[
    '<value>',
])

if res.pets is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `tags`             | List[*str*]        | :heavy_minus_sign: | Tags to filter by  |


### Response

**[operations.FindPetsByTagsResponse](../../models/operations/findpetsbytagsresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get_pet_by_id

Returns a single pet

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.pet.get_pet_by_id(pet_id=504151)

if res.pet is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `pet_id`            | *int*               | :heavy_check_mark:  | ID of pet to return |


### Response

**[operations.GetPetByIDResponse](../../models/operations/getpetbyidresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## delete_pet

Deletes a pet

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.pet.delete_pet(pet_id=441876, api_key='<value>')

if res.pet is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `pet_id`           | *int*              | :heavy_check_mark: | Pet id to delete   |
| `api_key`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeletePetResponse](../../models/operations/deletepetresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## upload_file

uploads an image

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.pet.upload_file(pet_id=565380, additional_metadata='<value>', request_body='0x7cca7F47Dd'.encode())

if res.api_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `pet_id`              | *int*                 | :heavy_check_mark:    | ID of pet to update   |
| `additional_metadata` | *Optional[str]*       | :heavy_minus_sign:    | Additional Metadata   |
| `request_body`        | *Optional[bytes]*     | :heavy_minus_sign:    | N/A                   |


### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
