# Review method: follow the proof

Use for every authored-test review. Group cases sharing a proof chain; spend more
effort on high-impact or opaque behavior, not on mechanically filling a matrix.

## 1. Establish what would count as correct

Find an authoritative expectation: accepted requirement, public API contract,
domain invariant, independent worked example, or explicitly approved compatibility
behavior. Track which one supports an important expected value. Existing production
code and existing tests may share the same bug.

For characterization, explicitly say the goal is preserving observed behavior;
do not call that product correctness. Conflicting contracts need a decision. Do
not demand a new specification document for an unambiguous local contract.

Ask what regression a user, caller, operator, or downstream system would notice.
Operational guarantees, accessibility, privacy, and data integrity count as behavior.
Avoid reducing "business value" to a visible happy-path screen.

## 2. Trace setup through the real path

Read the full test and relevant hooks, factories, base classes, patches, aliases,
factories' defaults, fake implementations, and production callers.

1. Identify the real subject and public or appropriate internal contract boundary.
2. Trace the supplied state through guards and branches. Keep unrelated prerequisites
   valid so the intended condition, not an earlier error, decides the result.
3. Confirm the action reaches the subject: correct import/patch target, actual
   component/handler, correct feature configuration, correct request/user identity.
4. Find each observed value's producer. Does it flow from the production decision,
   or is the test merely reading a fixture, recorded mock return, or cached object?
5. Check when the assertion runs, including awaited tasks, callbacks, retries,
   transaction boundaries, eventual consistency, and process termination.

A static trace supports an inference about reachability. It does not mean the
branch or assertion has actually executed.

## 3. Challenge the oracle and observation

For each meaningful assertion ask: **could the claimed fault happen while this
assertion remains true?** Supply the smallest concrete witness.

Useful probes, only when related to the claim:

- Return an empty result, constant result, swapped identity, or default amount.
- Drop a required field, tenant filter, authorization check, write, or event.
- Return success while persisting nothing, persisting twice, or touching the wrong row.
- Reject before the intended rule because a fixture has an unrelated invalid field.
- Reuse a stale cached result, ignore a filter, or reorder equal-valued items.
- Acknowledge a retry without deduplication, recovery without success, or cancellation
  without stopping the side effect.

Describe these as **static counterexamples**, not executed mutations. A fault must
be plausible for this behavior and consistent with the test's setup; arbitrary
omnipotent broken code is not useful evidence. Passing for a harmless refactor is
desirable. A useful test need not detect every conceivable implementation mistake.

Expected values need independence appropriate to the claim. An imported production
limit is valid for a relational test around the *configured* limit; it is circular
when the claim is that the public limit is a fixed required value. A distinct
reference algorithm can be legitimate if independently justified; copying the same
branches, parser, or calculation repeats the same potential mistake.

## 4. Check the smallest meaningful scenario set

Inspect existing assertions, not just test names. Classify reviewed additions as:

| Action | Justification |
|---|---|
| KEEP | Useful distinct protection already expressed adequately. |
| STRENGTHEN | The case matters but setup/action/assertions miss its fault. |
| MERGE | Same contract, boundary, fault and lifecycle; combine without hiding failures. |
| DROP | No distinct relevant guarantee; cite surviving protection or why no project behavior is exercised. |
| REPORT GAP | A concrete consequential guarantee in the changed scope lacks protection; return it to the author/designer, without taking over case planning. |

Consider happy, alternative, rejection, and recovery paths without demanding one
per category. Use decision conditions, inclusive/exclusive boundaries, transitions,
and factor interactions when they explain a real fault. Parameterization is useful
for equivalent structure, not a reason to enumerate arbitrary values or hide cases.

Before dropping a test check whether it independently protects routing, serialization,
transaction semantics, native interaction, deployment/configuration, or a required
smoke contract. Overlap across layers is not automatically redundancy. A valid,
cheap test does not become blocking merely because another arrangement is shorter.

Only demand a missing case when it protects a relevant changed guarantee or a
material regression risk. Identify its source, setup, observation, and credible
fault. Deferred historical gaps outside scope are not automatic blockers for a
small test change. Do not use a perfect-coverage ideal to create endless rework.

## 5. Make the test maintainable and executable

Check repository layout and naming against discovery and local conventions.
A good name states condition/action and outcome, not `works` or a private method
sequence. Name-only ambiguity is normally optional unless it hides what is tested
or violates a required gate. Keep one coherent scenario per test; several assertions
about its result and forbidden side effects belong together. A recovery sequence
does not need to be split into unrelated tests that depend on each other.

Trace setup and teardown on failure paths. Each test must own the state it mutates
or explicitly use safe shared immutable state. Inspect unique IDs/ports/paths,
transaction scope, seeded randomness, locale/timezone, resource cleanup, and worker
isolation where relevant. Avoid test order dependence, global leaks, real credentials,
uncontrolled external services, and accidental user-data mutation.

Check that assertions are active: no unreturned promise, swallowed exception,
conditional bypass, empty loop, ineffective assertion helper, always-true boolean,
disabled assertions, permissive expected-failure marker, or snapshot auto-update.
Pin the important values and absence constraints; preserve tolerances where the
contract needs them. Validate a tolerance against domain precision rather than
replacing it with brittle bit-for-bit floating-point equality.

Prefer the cheapest environment containing the fault. Inspect avoidable startup,
full-stack fixtures for pure rules, heavy repeated seeding, redundant parameter
products, arbitrary sleeps, and polling without deadlines. Do not substitute a fake
for real persistence/native behavior when that behavior is the claim. Lack of a
timing measurement is not evidence a test is slow; report estimates as estimates.

## 6. Calibrate and close

Separate demonstrated flaws in the test from suspected production defects and
missing review information. Try to disprove your own finding by reading helpers
and related tests; a helper may already assert the missing guarantee.

Report only issues with a clear consequence and remedy. Cite the source location
and exact false-green, wrong-red, or maintenance mechanism. Keep optional style
improvements optional. State useful coverage retained and significant unreviewed
surfaces. Do not manufacture issues just because the requested critic is strict.

## Requirement authority and contradictions

Classify the oracle as accepted requirement/public contract, independently checked
example/property, approved characterization, or unresolved assumption. Current
implementation is evidence of behavior, not authority for correctness. Compare
requirements under the same trigger, actor, state and precedence rules before
calling them contradictory. Report incompatible outcomes and affected tests to
the requirement owner; do not resolve ambiguity by copying implementation.
Characterization can preserve explicitly approved behavior without proving it is
desired product behavior. A missing protection is a review finding, not permission
to take over scenario research or produce a replacement designer plan.

## Failure diagnostics

Inspect how failed assertions reach the runner. Reports should identify the test
and parameter case, with relevant expected and actual observations. Existing
runner diffs and case labels suffice; do not require custom messages everywhere.
Generic booleans or caught exceptions need context when they erase discrepancies.
Async errors must be awaited/joined or delivered through the runner's supported
mechanism. Teardown errors must not replace or swallow the primary assertion.
Bounded waits should expose what was awaited and the last relevant observed state,
using safe existing logs/artifacts where useful; never demand secret dumps.
Block demonstrated loss of useful diagnosis, not a formatting preference.
