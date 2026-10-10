# Platform checks

Load only sections relevant to the test's claim. Adapt to the configured framework
and version; these are semantic checks, not a requirement to adopt specific tools.

## Backend, API, persistence, integrations

Trace real routing/middleware, identity, validation, business rules and storage.
A controller test with the service doubled proves mapping, not service behavior.
A direct service call does not prove authentication or route wiring.

- Use valid other prerequisites to isolate a rejection. Distinguish missing resource,
  forbidden owner, invalid input and dependency failure when the contract does.
- Assert meaningful payload/state, identities and cardinality. A list of only one
  tenant cannot demonstrate tenant isolation; include a valid contrasting tenant.
- For persistence, inspect transaction boundaries and fresh observations. Same-session
  caches and rollback fixtures can hide missing commit behavior; select the boundary
  that matches the actual claim rather than universally demanding a new connection.
- For rejected writes, inspect rollback/no partial updates and no forbidden events
  when required. An error response does not prove no side effect occurred.
- For pagination/filtering, use distinguishing records and validate absence of leaks,
  duplicates, or gaps within the promised contract. Do not assert sorting unless promised.
- For integrations, distinguish request construction, provider response handling,
  contract compatibility, and actual remote success. Test the selected boundary.

Use realistic synthetic domain data, not copied production data or real credentials.
Business timeouts and transport errors should be introduced at the appropriate seam.

## Web and component UI

Trace user action → browser/component behavior → request/state → visible outcome.
Inspect what the renderer/environment implements. A simulated DOM cannot establish
native layout, focus behavior, downloads, navigation or platform validation it does
not implement. A browser screenshot is not an assertion; a reviewed visual baseline
comparison can be one.

- Prefer normal interaction through accessible role/name/label or a stable explicit
  contract. Avoid implementation-detail selectors unless the project has a valid reason.
- Check awaited user actions, async rendering and retrying assertions. An unawaited
  promise can let the test finish before failure. Negative assertions need a relevant
  completion point when delayed effects are possible.
- Check recovery by correcting the input and actually resubmitting with a normal
  click/keyboard action. Dispatching `submit` directly or calling a handler can bypass
  native constraint validation and hide a still-blocked form.
- A low-level event is acceptable for an event-handler contract; do not blanket-ban
  `fireEvent` or mandate browser E2E for every component.
- Mock the external response when testing UI interpretation, not the component's
  own state transition. Confirm loading/error/empty/content states are distinguishable.
- Check keyboard/focus/accessible error behavior when it is part of the changed user
  path or an applicable accessibility requirement. Automated role checks alone do not
  certify all accessibility, and DOM assertions alone do not prove visual layout.
- Visual snapshots need intentional baselines and a controlled viewport/font/platform
  context. Broad masking must not hide the changed behavior; unexplained snapshot
  regeneration is not a fix. Semantic assertions can complement visual comparisons.

Read supplied UI evidence only. This critic does not launch a browser to execute
the tests or explore an application; return the precise observation needed by the
next authorized exploration/execution phase.

## Mobile and desktop

Choose the boundary that includes the changed behavior: pure model logic, UI toolkit,
OS integration, lifecycle, device or process. Headless widgets do not prove OS permission
prompts, notifications, filesystem dialogs, background execution or process restoration.

Inspect lifecycle and persistence claims: restarting a view is not a process restart;
reusing an in-memory store is not restoration from disk; rotating a simulator is not
proof of all device configurations. Use the project's actual target matrix and
capabilities. Name missing platform evidence without inventing mandatory devices.

For offline/reconnect, interruption and recovery, inspect the sequence and final
state: no lost edits, duplicate effects or stale UI when those are contractual.
Check sandboxed files, isolated app state, permissions setup and cleanup. Do not
accept mutation of a user's actual settings or files as a convenient fixture.

## CLI and filesystem

Inspect real parsing/dispatch at the claimed boundary. Calling a command function
directly does not prove installed entrypoint packaging or OS process exit behavior.
Do not demand subprocesses for pure formatting logic.

Check exit status, stdout/stderr split, promised machine-readable payload, encoding
or newline contract, and resulting files/state as relevant. A JSON parse alone cannot
prove the payload is correct. Diagnostic text on stdout can break machine consumers.

Use isolated temporary directories and HOME/config when needed. Check cleanup,
failure atomicity, overwrites and interrupted operations for changed file behavior.
Path quoting, spaces and platform differences need tests when plausible for the
supported contract, not an invented exhaustive platform matrix.

## Async, time, retries and concurrency

Read the runner's real execution model. Missing `await`, unjoined goroutines/threads,
unreturned promises and background assertions are potential false passes. A framework
may supply a join automatically; inspect it before accusing.

Use synchronization barriers/events or controlled scheduling to expose a relevant
race, not arbitrary sleeps or a claim inferred from repeated sequential calls.
Specify the invariant and observation point: exactly one durable effect, conservation
of total, ordered delivery, or allowed outcomes under the project's consistency model.

Fake clocks should advance the real scheduling seam; stubbing the decision itself
tests nothing. Check expiry boundaries using the documented precision and semantics.
Retries need bounded termination and meaningful final state. A no-call assertion
immediately after spawning work cannot establish absence of a later side effect.

Repeating a test or automatically retrying failures is not proof of determinism.
Distinguish a product retry contract from runner retries hiding a flaky test.

## Performance of the suite and performance as a contract

These are separate questions. A useful test should avoid needless suite cost; a
performance regression test must substantiate a performance requirement.

For suite cost, inspect expensive setup/teardown, avoidable full-stack startup,
unbounded waits, huge Cartesian parameter products and repeated identical fixtures.
Propose a cheaper level only if it preserves the fault boundary. Cite measured
timings when available; never fabricate a millisecond budget.

For a performance claim, identify a requirement/accepted budget and representative
workload: data size/distribution, concurrency, cold/warm caches, setup excluded or
included intentionally, completion criterion, relevant metric and environment.
One trivial input timed against an arbitrary threshold proves little. A query-count
or allocation bound may be a stable proxy for a specific scaling regression but
does not prove end-user latency or an SLO.

Check whether repetitions/warmup, percentile calculations and variance treatment
make sense for that metric. Do not demand a benchmark suite on every change, or
accept a single noisy wall-clock assertion as reliable evidence. A future executor
can measure; static review can identify design defects and unknowns only.

## Boundary representations and cross-operation invariants

When claiming an API contract, inspect the real wire representation and schema:
field names/types, required versus optional/null fields, IDs, serialization, error
shape and version as relevant. An internal ORM object or permissive fake can bypass
DTO validation and manufacture confidence. Use the actual boundary or a faithful
contract fixture; do not demand an external service for a local serializer claim.

Where the changed contract spans operations or components, check the consequential
invariant through observable outcomes: e.g. refund plus ledger balance, retry plus
single persisted charge, permission denial plus unchanged state. Separate locally
green checks can miss an inconsistent combined state. Require only reachable,
in-scope invariants; this is not permission to design a whole-system test program.
Use the diagnostics and stability checks in review-method and evidence-and-gates
for platform-specific async failures, resource sharing and timeout observations.
