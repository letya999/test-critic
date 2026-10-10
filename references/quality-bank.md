# Quality bank: distinguish faults, not appearances

Consult relevant rows when challenging written tests. These examples are patterns,
not universal bans or mandatory test inventories. Findings require the actual
project's contract and code path.

## False confidence and minimal repairs

| Weak pattern | Fault it can miss | Smallest meaningful repair |
|---|---|---|
| `first.key == retry.key` | Both keys are missing. | Assert required presence/shape and stable identity across the retry. |
| Check status 200 only | Wrong payload, missing write, wrong account affected. | Assert the promised result/effect; status-only is fine for a status-only contract. |
| `all(row.allowed for row in rows)` | An empty result passes. | Establish a positive witness/cardinality when non-empty output is required. |
| Expected and actual use the same production helper | The shared calculation is wrong. | Use a checked example or independently justified relation. |
| Mock the function being tested | Only the mock's configured answer is observed. | Call the real subject; double an external seam if needed. |
| All identities or amounts equal | Swaps, wrong owners and wrong joins remain invisible. | Use different valid values that distinguish the fault. |
| Unauthorized request uses nonexistent resource | Not-found can satisfy a broad rejection assertion. | Seed an existing other-owner resource and check the required denial and no forbidden effect. |
| Check DB write with the same in-memory object | No durable write occurred. | Observe through a fresh read/context appropriate to the persistence claim. |
| Assert an event list has length one | Wrong type, recipient or payload. | Pin the meaningful event fields and relevant absence/uniqueness. |
| Test passes if any exception is thrown | Import/setup/unrelated validation error masks the target failure. | Narrow error type/code and assert the relevant state remains unchanged. |
| `assert_called()` for a commit claim | Dispatch succeeds but commit never happens. | Observe committed state at the right boundary; keep dispatch assertions for dispatch contracts. |
| Snapshot captures the entire response | Noise hides the important contract; approved snapshot can encode a bug. | Review a stable baseline and pin critical semantic fields separately where needed. |
| Generate the expected snapshot in the test | Current output becomes its own oracle. | Compare to an independently reviewed baseline. |
| Test name promises concurrency, calls sequentially | Race window is never opened. | Coordinate actual overlap and observe the final invariant. |
| Retry test asserts only call count | Wrong payload, extra charge, or unbounded retries. | Check the retry contract, bounded completion and relevant final/forbidden effects. |
| Recovery test checks error message disappears | Corrected operation is still blocked. | Perform the normal retry action and observe successful completion. |
| Skip/xfail/todo hides a required regression | Gate passes without checking the requirement. | Restore active protection or disclose the genuine unresolved prerequisite. |
| `if items: assert ...` | Empty output bypasses every assertion. | Assert the required precondition and outcome unconditionally. |
| Sleep "long enough" before asserting | Load-dependent result and extra latency. | Await a meaningful signal with a bounded deadline. |
| Single-row sorted/filter fixture | Ignoring sorting/filtering still passes. | Add distinct matching/nonmatching or out-of-order witnesses. |
| Assert no exception for a transformation | Constant/no-op output passes. | Assert the contractual transformation or invariant. |
| Broad partial match | Required values, cardinality, or forbidden data can be wrong. | Pin only the fields/absence/exactness that the contract requires. |

## Doubles: inspect responsibility, not ideology

Keep the decision under test real. A network stub feeding an actual parser, a fake
clock driving real expiry logic, or a mock gateway observing a dispatch contract
can be excellent. A fake repository can support service-rule tests but cannot prove
database isolation, uniqueness, collation, rollback, or durable commit.

Ask which guarantee crosses the substituted boundary and where that guarantee is
otherwise protected. Compare doubles with real signatures, serialization, errors,
and state semantics where relevant. Look for patches applied in the wrong module,
autouse/global mocks that erase the behavior, or recorded results bypassing parsing.
Recommend a contract/integration test only for a concrete gap; do not demand one
for every mock. Do not invent a fake framework to avoid a small existing fixture.

## Properties and generated cases

Check that the asserted property is domain-justified and can be false for a plausible
bad implementation. Examples of inadequate properties:

- Sorting is idempotent: the identity function also satisfies it. Check ordering
  and multiset preservation for the relevant domain, including duplicates.
- Decode(encode(x)) equals x: paired bugs can cancel out. Keep round-trip protection
  and add known vectors/interoperability checks when an external encoding is promised.
- Result is within `[0, limit]`: always returning zero satisfies it. Add a nonzero
  witness or a relation that expresses the actual behavior.
- Compare two calls to the same deterministic method: consistency alone is not
  correctness unless determinism is the contract being protected.

Inspect generator support, not just sample count: meaningful boundaries, invalid
inputs when needed, constrained combinations, nonempty data, duplicate IDs, states,
and transitions. Heavy filtering/assumptions may discard the interesting domain.
Ensure stateful preconditions allow the targeted sequence. Require replayable seeds
or counterexamples where the framework supports them; shrinking must preserve the
case's meaning. Do not require property testing when a few examples protect the risk.

## Granularity and necessity

A test earns its maintenance cost by a meaningful failure signal. Framework/library
behavior alone is usually outside scope, but project configuration, adapter behavior,
version compatibility and contract assumptions can justify such checks.

Merge same-layer duplicates only if fixtures, faults, and lifecycle really coincide.
Retain separate cases when they isolate distinct decisions or make failure diagnosis
clearer. Do not split a coherent outcome into many tests merely to achieve "one
assertion per test". Do not delete a required smoke check because it is shallow: its
claim may intentionally be only startup/readiness.

An improbable setup is a problem when unreachable at the selected boundary, not
when merely uncommon. Threat inputs at an untrusted boundary, crashed processes,
interrupted writes, and retries after lost acknowledgments may be realistic and
high-impact. Cite reachability and consequence before recommending deletion.

## Worked review: missing idempotency keys

Contract: every submission carries a nonempty idempotency key; retries of the same
operation reuse it; independent operations receive different keys.

```text
Weak:   send twice; assert first.headers[key] == second.headers[key]
Witness: remove key generation; both reads return absent; equality still passes.
Repair: assert a valid nonempty key, equality for the retry, and a distinct key
        for a separate operation if this claim is not already covered.
Limit:  outgoing headers prove the client contract, not server deduplication.
```

## Worked review: legitimate mock

Contract: the notification adapter dispatches a normalized recipient and body.
The test calls the real adapter and checks exact meaningful arguments to the
substituted vendor transport. This is a valid dispatch test. Do not require a live
vendor delivery or label it self-testing merely because it asserts a mock call.
If the claim instead promises delivery/acknowledgment handling, inspect that path
and its evidence separately.

## Worked review: negative control at the wrong guard

Contract: a suspended member cannot edit an existing owned document.
The test submits a nonexistent document ID and accepts any 4xx. It could pass even
if the suspension check were deleted. Use an existing owned document with all other
valid inputs; assert the suspension-specific rejection and unchanged document.
An active-member counterpart can establish the permitted path when not already
protected. Do not add a full role matrix without a relevant rule.

## Diagnostic and boundary traps

- A broad catch/log-and-return can turn assertion or background errors into green.
  Trace exception delivery rather than trusting that an error was printed.
- A failing teardown can hide the business discrepancy. Preserve primary failure
  and attach cleanup context through the runner's supported mechanism.
- An unlabelled parameterized boolean may conceal which domain case and actual
  result failed. Prefer direct value assertions and meaningful existing case IDs;
  a built-in diff already carrying that information needs no custom boilerplate.
- Internal-object fixtures can satisfy a fake while violating the wire schema.
  Inspect the boundary actually claimed, including serialization and nullability.
- Two locally correct outputs can violate a shared business invariant. Check the
  relevant combined observation, not an invented exhaustive lifecycle matrix.
