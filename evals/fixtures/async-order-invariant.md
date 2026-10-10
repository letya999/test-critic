# Review packet: async, order and combined state

Review only; no edits, execution or delegation. Give the verdict and smallest
repair obligations for the three tests, not a replacement scenario plan.
The shown runner supports arbitrary order and parallel workers. No run is supplied.

Accepted contract: refunding a captured order atomically sets `refunded=True` and
credits the customer's balance by the captured 40 minor units exactly once. Both
state fields are freshly read from storage after the async operation completes.
The real service executes this operation. The helper starts background work and
returns immediately; its task result is neither awaited nor reported to the runner.

```python
shared_account = Account(balance=0)

def test_seed_balance():
    shared_account.balance = 40
    assert shared_account.balance == 40

def test_refund():
    order = captured_order(amount=40, account=shared_account)
    start_refund_in_background(order)
    assert shared_account.balance == 40

async def test_refund_flag():
    account = fresh_account(balance=0)
    order = captured_order(amount=40, account=account)
    await real_service.refund(order)
    assert await storage.read_refunded(order.id) is True
```

The seed test mutates a shared object; no per-test reset exists. `test_refund` can
pass before any work starts if the seed ran first, and background failures vanish.
`test_refund_flag` uses isolated storage and properly awaits completion, but observes
only the flag. A plausible faulty service sets the flag and omits the balance credit.
No other existing assertion checks that credit. The author calls both refund tests
complete business protection and asks for runner retries to fix any intermittency.
