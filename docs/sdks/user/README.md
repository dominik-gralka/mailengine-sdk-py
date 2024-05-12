# User
(*user*)

## Overview

Operations about user

### Available Operations

* [create_user](#create_user) - Create user
* [create_users_with_list_input](#create_users_with_list_input) - Creates list of users with given input array
* [login_user](#login_user) - Logs user into the system
* [logout_user](#logout_user) - Logs out current logged in user session
* [get_user_by_name](#get_user_by_name) - Get user by user name
* [update_user](#update_user) - Update user
* [delete_user](#delete_user) - Delete user

## create_user

This can only be done by the logged in user.

### Example Usage

```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.user.create_user(request=components.User(
    id=10,
    username='theUser',
    first_name='John',
    last_name='James',
    email='john@email.com',
    password='12345',
    phone='12345',
    user_status=1,
))

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [components.User](../../models/components/user.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_users_with_list_input

Creates list of users with given input array

### Example Usage

```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.user.create_users_with_list_input(request=[
    components.User(
        id=10,
        username='theUser',
        first_name='John',
        last_name='James',
        email='john@email.com',
        password='12345',
        phone='12345',
        user_status=1,
    ),
])

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [List[components.User]](../../models/.md)  | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUsersWithListInputResponse](../../models/operations/createuserswithlistinputresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## login_user

Logs user into the system

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.user.login_user(username='<value>', password='<value>')

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `username`                           | *Optional[str]*                      | :heavy_minus_sign:                   | The user name for login              |
| `password`                           | *Optional[str]*                      | :heavy_minus_sign:                   | The password for login in clear text |


### Response

**[operations.LoginUserResponse](../../models/operations/loginuserresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## logout_user

Logs out current logged in user session

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.user.logout_user()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.LogoutUserResponse](../../models/operations/logoutuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_user_by_name

Get user by user name

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.user.get_user_by_name(username='<value>')

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `username`                                                 | *str*                                                      | :heavy_check_mark:                                         | The name that needs to be fetched. Use user1 for testing.  |


### Response

**[operations.GetUserByNameResponse](../../models/operations/getuserbynameresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## update_user

This can only be done by the logged in user.

### Example Usage

```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.user.update_user(username='<value>', user=components.User(
    id=10,
    username='theUser',
    first_name='John',
    last_name='James',
    email='john@email.com',
    password='12345',
    phone='12345',
    user_status=1,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `username`                                                   | *str*                                                        | :heavy_check_mark:                                           | name that needs to be updated                                |
| `user`                                                       | [Optional[components.User]](../../models/components/user.md) | :heavy_minus_sign:                                           | Update an existent user in the store                         |


### Response

**[operations.UpdateUserResponse](../../models/operations/updateuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_user

This can only be done by the logged in user.

### Example Usage

```python
import mailengine

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.user.delete_user(username='<value>')

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `username`                        | *str*                             | :heavy_check_mark:                | The name that needs to be deleted |


### Response

**[operations.DeleteUserResponse](../../models/operations/deleteuserresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |
