# Evidence and gates

Use when reporting feasibility, interpreting execution artifacts, or handing back
to an implementation workflow. The critic remains static in every case below.

## Evidence vocabulary

| Evidence | What may be said | What it cannot establish |
|---|---|---|
| Source/config inspected | "The configured glob excludes this file." | That any command actually ran. |
| Static counterexample | "Both absent keys satisfy this equality." | That a mutant was executed or killed. |
| Supplied execution artifact | "This report records these selected cases at this revision." | Fresh execution, or applicability to changed files. |
| Supplied behavioral red/green | "The artifact shows this assertion failing/passing in these states." | Product correctness outside that oracle and scope. |
| Supplied targeted mutation evidence | "This fault caused this assertion failure on this snapshot." | Completeness, absence of bugs, or quality of every test. |

Prefer original output with command, working directory, code snapshot/revision,
selected test IDs, result counts, exit status, and failure location. An author's
sentence "all green" is a claim, not verified evidence. If relevant files changed,
mark artifacts stale for affected conclusions. Do not demand a permanent ledger
when a concise report and existing CI link suffice.

## Red is not one thing

| Situation | Static critic decision / next-step limit |
|---|---|
| New behavior, existing callable seam | Require assertions against the intended outcome and a plausible pre-change failure. ACCEPT permits the next configured red run. |
| New API does not exist yet | A contract-grounded test may be ACCEPTed for the next permitted step; identify the missing symbol. An import/type/link failure is structural red, not behavioral red. |
| Feature already implemented / test-only strengthening | Do not demand every useful test fail on current code. Look for an independently grounded oracle and concrete sensitivity gap. |
| Behavior-preserving refactor | Existing green behavior may be exactly correct; judge preservation and reachable regression faults. |
| Bug-finding regression fails against current behavior | If the requirement is sound, retain the regression and flag a likely product defect. Do not alter the expectation to match the bug. |
| Characterization | State that the test preserves current behavior, not that the behavior is normatively correct. |
| Environment, import, fixture, timeout, unrelated error | Do not count this as behavioral sensitivity; distinguish test defects from unavailable execution infrastructure. |

For a missing API, recommend only the next action allowed by the project's TDD
rules. A minimal declaration/skeleton may be permitted outside review; it is still
a code change and is not automatically authorized by ACCEPT. Do not secretly
implement the feature to get a more impressive red run. An ambiguous future API
contract is a real blocker, not license to invent functions or signatures.

## Interpreting fault probes performed elsewhere

Do not execute these steps here. When supplied evidence claims that a test detects
a fault, check that the later executor established:

1. The correct relevant baseline passes in the stated environment.
2. A small plausible fault changes the production behavior claimed by the test,
   not the test's own expected value or its assertion.
3. The intended test runs and fails at a meaningful observation for that fault.
4. The baseline is restored and the same relevant test passes again.

For bug-fix TDD, the original buggy version can supply the fault witness and the
fixed version the passing baseline; no artificial mutation is needed to repeat
that same evidence. Before implementation, only expected sensitivity is available.

A compile error, runner crash, or setup failure is not a behavioral kill. A timeout
can be relevant to a termination contract if its cause and bound are established;
otherwise it is ambiguous evidence. Preserve the tool's raw classification while
explaining this narrower interpretation. Equivalent/unreachable/out-of-contract
mutants need analysis, not an automatic new test. Do not enforce an arbitrary
mutation percentage or one executed mutant per test.

If future mutation work is authorized, hand it to the surrounding workflow with
isolation/restoration prerequisites. This skill never edits the working copy,
stashes a user's changes, or resets Git to manufacture a baseline.

## Feasible is different from verified

Check that referenced fixtures, helpers, APIs and data exist or are explicitly
defined as new contractual seams. Find runner inclusion, async integration,
required services and cleanup in source. An undeclared fixture is a test defect;
a declared PostgreSQL service unavailable on this machine is an execution gap.

Report "statically feasible, not executed" when appropriate. Missing local runtime
or CI output alone cannot block a pre-run review. Missing essential code/config
needed to determine what the test does can. If a project explicitly requires
execution before its final gate, ACCEPT here does not satisfy that final gate.

## Gate discipline

An unresolved must-fix test issue means REVISE. A final prose disclaimer does not
neutralize it. The author repairs the specific tests and returns for review; the
critic validates the new proof chain and checks shared-helper fallout.

Only new evidence can dismiss a finding as inapplicable. Record the finding, the
source that refutes it and what protection remains. Deadline pressure, a large
coverage number or previous reviewer approval is not new evidence. An authorized
user can explicitly waive this skill's advisory gate subject to higher-priority
rules; record WAIVED and the remaining risk, never relabel it ACCEPT.

The skill is an instruction, not an execution interceptor. Actual enforcement
requires the surrounding agent to honor it or existing repository tooling to
enforce the workflow. Do not claim that a Markdown verdict technically prevents
commands, commits, or deployments.

## Stability evidence and fault sensitivity

Use two read-only modes: pre-run source review, or review of source plus supplied
execution artifacts. In both, the critic performs no execution. Label supplied
observations separately from static predictions; identify the reviewed revision,
selected test, command/environment and failing assertion where available.

Check source for uncontrolled wall time, RNG/seed, locale/timezone, iteration and
test order, parallel workers, ports/files/accounts, persistent state, network and
eventual consistency. Check reset/cleanup and completion signals. Controlled clocks,
seeds and isolated resources are valid; do not ban them or invent repeated-run quotas.
Product retry semantics differ from runner retries. A green after retry can conceal
an intermittent first-attempt failure. Read first-attempt outcomes when supplied.
Bounded repetitions support only 'no flakes observed in this sample', never a
guarantee of no flakes. Without runs, report assessed risks and unverified stability.

For each important claim, name a plausible reachable fault, the exercised decision,
and the exact observation/assertion that should reject it. This is static sensitivity
reasoning. Supplied empirical proof needs a valid baseline, the intended selected
test failing at a meaningful assertion under the relevant defect, and a passing
restored baseline; keep input and oracle unchanged. An existing bug can provide the
fault witness. Setup/import errors, wrong assertions, timeout unrelated to the
contract, another selected test, or changing expectations do not prove sensitivity.
Do not require mutation tooling, a pre-implementation behavioral red for an absent
API, or execution during this review. Route evidence gaps to the permitted executor
only when empirical proof is an actual project gate.
