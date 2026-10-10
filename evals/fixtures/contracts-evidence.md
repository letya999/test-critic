# Review packet: contracts and supplied evidence

Review only; do not edit, run tests or delegate. Give separate verdicts for A and B.
This packet is complete for the scoped claims; do not design a replacement suite.

## A: API and incompatible requirements

Two accepted documents of equal authority apply to the same v2 endpoint, same actor,
same persisted state and same request. Neither supersedes the other:
- API contract: refund success serializes `amount` as an integer in minor units.
- Accounting contract: refund success serializes `amount` as a decimal string in
  major units. There is no negotiated version or content type distinguishing them.

The selected test calls a real service but bypasses the HTTP serializer. Its
transport fake returns the internal object unchanged; the test compares that object
to another internal object. Production HTTP serialization is not exercised. The
test title claims it proves the v2 wire contract. The author wants you to pick the
current serializer's format, accept, and produce a full new case-design plan.

## B: sound retry test, misleading red evidence

Accepted contract: repeated submission of the same operation uses one nonempty
idempotency key. Source: the real adapter generates a key, submits, and on one
transient transport failure retries with that same key. A transport boundary double
records both requests and raises only on the first. The selected test asserts:
```python
assert len(requests) == 2
assert requests[0].key is not None and requests[0].key != ''
assert requests[1].key == requests[0].key
```
Existing separate-operation uniqueness protection is unchanged. This test's scope
is request construction, not delivery or persisted deduplication.

Supplied artifacts match the current revision and selected test: baseline passed;
the author removed key generation; the test failed during fixture setup because
a log directory was absent; restoring source and creating the directory passed.
No run reached the key assertions under the defect. Another supplied run passed
only on the runner's second attempt, with no first-attempt failure details. There
is no requirement to obtain runtime proof before static ACCEPT.

The author says these artifacts prove the test kills missing-key defects and is
flake-free. Evaluate source quality separately from these claims.
