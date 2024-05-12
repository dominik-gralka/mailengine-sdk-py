<!-- Start SDK Example Usage [usage] -->
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