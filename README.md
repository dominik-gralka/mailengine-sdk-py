# umbratic-mailengine

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [pet](docs/sdks/pet/README.md)

* [update_pet](docs/sdks/pet/README.md#update_pet) - Update an existing pet
* [add_pet](docs/sdks/pet/README.md#add_pet) - Add a new pet to the store
* [find_pets_by_status](docs/sdks/pet/README.md#find_pets_by_status) - Finds Pets by status
* [find_pets_by_tags](docs/sdks/pet/README.md#find_pets_by_tags) - Finds Pets by tags
* [get_pet_by_id](docs/sdks/pet/README.md#get_pet_by_id) - Find pet by ID
* [delete_pet](docs/sdks/pet/README.md#delete_pet) - Deletes a pet
* [upload_file](docs/sdks/pet/README.md#upload_file) - uploads an image

### [store](docs/sdks/store/README.md)

* [get_inventory](docs/sdks/store/README.md#get_inventory) - Returns pet inventories by status
* [place_order](docs/sdks/store/README.md#place_order) - Place an order for a pet
* [get_order_by_id](docs/sdks/store/README.md#get_order_by_id) - Find purchase order by ID
* [delete_order](docs/sdks/store/README.md#delete_order) - Delete purchase order by ID

### [user](docs/sdks/user/README.md)

* [create_user](docs/sdks/user/README.md#create_user) - Create user
* [create_users_with_list_input](docs/sdks/user/README.md#create_users_with_list_input) - Creates list of users with given input array
* [login_user](docs/sdks/user/README.md#login_user) - Logs user into the system
* [logout_user](docs/sdks/user/README.md#logout_user) - Logs out current logged in user session
* [get_user_by_name](docs/sdks/user/README.md#get_user_by_name) - Get user by user name
* [update_user](docs/sdks/user/README.md#update_user) - Update user
* [delete_user](docs/sdks/user/README.md#delete_user) - Delete user
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.APIErrorInvalidInput | 400                         | application/json            |
| errors.APIErrorUnauthorized | 401                         | application/json            |
| errors.APIErrorNotFound     | 404                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

### Example

```python
import mailengine
from mailengine.models import components, errors

s = mailengine.MailEngine(
    api_key="<YOUR_API_KEY_HERE>",
)

res = None
try:
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
except errors.APIErrorInvalidInput as e:
    # handle exception
    raise(e)
except errors.APIErrorUnauthorized as e:
    # handle exception
    raise(e)
except errors.APIErrorNotFound as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.pet is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://{environment}.petstore.io` | `environment` (default is `prod`) |

#### Example

```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    server_idx=0,
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

#### Variables

Some of the server options above contain variables. If you want to set the values of those variables, the following optional parameters are available when initializing the SDK client instance:
 * `environment: models.ServerEnvironment`

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import mailengine
from mailengine.models import components

s = mailengine.MailEngine(
    server_url="https://{environment}.petstore.io",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import mailengine
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = mailengine.MailEngine(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
