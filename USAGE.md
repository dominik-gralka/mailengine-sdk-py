<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->