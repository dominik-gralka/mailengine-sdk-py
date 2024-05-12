# MailEngine SDK


## Overview

MailEngine SDK for Python: A service to send emails quick and easy

### Available Operations

* [send_email](#send_email) - Send an email

## send_email

Endpoint to send an email

### Example Usage

```python
import mailengine
from mailengine.models import operations

s = mailengine.MailEngine(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.send_email(request=operations.SendEmailRequestBody(
    recipient_email='john.doe@example.com',
    recipient_name='John Doe',
    sender_email='noreply@example.com',
    sender_name='No Reply',
    email_subject='Important Information',
    email_content='This is a test email content.',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.SendEmailRequestBody](../../models/operations/sendemailrequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.SendEmailResponse](../../models/operations/sendemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
