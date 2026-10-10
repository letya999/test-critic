# Review packet: notification adapter

Task: Review the changed test before its first run. Return a verdict with concrete
issues if any. Do not modify files or run code.

`specs/notification.md`: This adapter trims leading/trailing whitespace from a
recipient address and dispatches the unchanged body. It returns the transport's
receipt unchanged. It does not validate addresses, deliver messages itself, retry,
or normalize case. Provider errors are propagated and already covered by an
unchanged test. This change adds the whitespace regression only.

`src/notify.py`:

```python
def notify(recipient, body, transport):
    return transport.send(recipient.strip(), body)
```

`tests/test_notify.py` (standard unittest discovery):

```python
import unittest
from unittest.mock import Mock
from src.notify import notify

class NotificationTests(unittest.TestCase):
    def test_dispatch_trims_recipient_without_changing_body(self):
        transport = Mock()
        transport.send.return_value = {"receipt": "delivery-9"}
        result = notify("  user@example.test  ", "Hello,  reader!", transport)
        transport.send.assert_called_once_with("user@example.test", "Hello,  reader!")
        self.assertEqual(result, {"receipt": "delivery-9"})
```

CI uses standard unittest discovery under tests. There is no execution artifact yet.
No relevant project rule requires a live provider, a property framework, mutation
testing, or one assertion per test. Review is scoped to this new test.
