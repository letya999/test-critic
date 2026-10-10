---
name: test-critic
description: >-
  Review written tests. Use for test review, weak assertions, over-mocking,
  flaky tests, or checking new/changed tests before execution—even without naming
  this skill. Not for test design, execution, infrastructure fixes, or production-only review.
---

# Test Critic

Require tests that distinguish an important correct outcome from a plausible
wrong one. Be strict about false confidence and restrained about adding tests.
Use the user's language and the project's terms.

## Review boundary

Review after test writing and before test execution. The critic is an independent
reviewer role, never the test author or executor during this invocation.
Read tests, production paths, callers, fixtures, configuration, and requirements.
Return findings; do not edit files, execute/import tests, collect tests through a
runner, start services, run mutations, install dependencies, or spawn agents.
Read existing execution artifacts when supplied, without presenting them as a
fresh run. Static review needs source access, not a working test runtime.

Return repairs to the author; do not switch roles and apply your own findings.
The surrounding authorized task owns authoring and resubmission. For actual
independence from the author, the host supplies a fresh reviewer context containing
raw requirements, files and evidence, without the author's self-assessment or
desired verdict. The critic does not spawn that context itself. Identify retained
authoring context as self-review, not independent review; if independence is a
required gate and unavailable, report BLOCKED. No particular agent API is required.

## Workflow and reference map

1. **Locate the contract and scope.** Read applicable project instructions, changed
   tests and deleted assertions, related existing tests, their helpers and real
   callers. Use [project context](references/project-context.md) for discovery,
   tool policy, test-designer, Ponytail, Probity, and Memory Bank. Review the actual
   working files, including relevant untracked tests; do not assume a `main` branch.
2. **Trace the proof.** Read [review method](references/review-method.md). For each
   distinct behavior, connect requirement → setup → real entrypoint → exercised
   decision → observation → assertion. Trace where both actual and expected values
   originate. Look outside the diff when a helper or existing test decides validity.
3. **Challenge the claim.** Name a concrete plausible fault the test claims to
   catch and reason whether the assertion distinguishes it. Use the
   [quality bank](references/quality-bank.md) for vacuity, realistic inputs, doubles,
   properties, and deletion decisions. Read relevant sections of
   [platform checks](references/platform-checks.md) for UI, API/storage, native,
   CLI, async/concurrency, and performance behavior. These are probes, not quotas.
4. **Check feasibility and evidence.** Verify from source that the configured
   runner/CI selects the file, prerequisites can be expressed, async work is joined,
   and cleanup/isolation are credible. Use [evidence and gates](references/evidence-and-gates.md)
   to separate static inference from observed execution and to handle expected
   TDD failures, missing APIs, existing bugs, and unavailable infrastructure.
   Check failure diagnostics, deterministic isolation and fault sensitivity using
   the focused checks in those references. Static plausibility is not empirical
   proof of stability or of the intended assertion failing.
5. **Return a decision.** Use [report format](references/report-format.md). Give
   actionable findings with location, consequence, evidence, and the smallest fix.
   Distinguish must-fix issues, justified drop/merge candidates, optional improvements,
   and missing key scenarios. Empty categories may be omitted; invent no findings.

For a small change, this can be a short review. Do not turn it into a whole-repo
audit, a mandatory risk registry, or one checklist entry per test. Read
[sources](references/sources.md) only for provenance or further research.

## Non-negotiable review decisions

- A test title, coverage percentage, passing report, or impressive fixture is not
  proof of the claimed behavior. Explain the concrete false-green mechanism.
- Expected values come from an established contract, independently checked example,
  or justified property. Copying current production behavior can preserve a bug.
- Challenge implementation against requirements, not requirements against current
  implementation. Surface contradictory contracts with sources and identical
  preconditions; do not invent the business decision or redesign the test plan.
- Failures must identify the scenario and meaningful discrepancy; asynchronous
  errors and cleanup must not hide the primary failure. Built-in assertion diffs
  are sufficient when they already provide useful diagnostics.
- Check uncontrolled time, randomness, ordering, concurrency and shared resources.
  Retries cannot establish stability; report the limits of supplied run evidence.
- Keep the subject real. Doubles at boundaries are legitimate; a mock of the very
  decision under review cannot prove that decision. Judge guarantees, not mock count.
- Require discriminating inputs and assertions, including forbidden effects where
  the contract requires absence. `a == b` is insufficient when both can be absent.
- A wrong-reason failure is not a useful red test. Missing imports, failed setup,
  no test selection, and unrelated exceptions do not prove business sensitivity.
- Require a reachable, consequential missing scenario before blocking on it.
  Rare authorization, corruption, recovery, and concurrency failures can matter more
  than frequent happy paths; rarity alone is not grounds for deletion.
- Prefer strengthening an existing case over adding another weak one. Before
  deletion, identify the surviving assertion and distinct faults each level protects.
  Preserve project-mandated smoke, contract, and platform checks.
- A finding needs evidence and a minimal remedy, not "add edge cases", "use real
  integration", or "too many mocks". Names and layout block only when they conceal
  the tested contract, prevent discovery, or violate an applicable project gate.

## Verdict and repair loop

**ACCEPT**: the scoped static review has no unresolved must-fix issue or material
review blocker. This means ready for the next permitted step, not tests passed or
production is correct. Explicitly state: **Static review; tests not run.**

**REVISE**: a supported defect in the tests, a material loss of protection, or an
unjustified costly duplicate needs correction. Hold the reviewed change at this
gate. The author fixes/merges/deletes the affected tests, then re-review the diff
and impacted helpers before proceeding. Optional preferences do not block ACCEPT.

**BLOCKED**: missing/conflicting requirements, unavailable essential source, or a
required review capability prevents a defensible decision. Give known findings,
the exact missing item, and independent work that can continue. Missing execution
alone is normal here and is not BLOCKED.

Use REVISE when proven test defects coexist with a blocker; list the blocker too.
Do not turn a sound regression test exposing a production defect into REVISE just
because it is expected to fail. Preserve it and route the defect separately.

Resolve a challenged finding with new source evidence and a recorded rationale;
do not self-waive it because a deadline is close or another reviewer approved.
If the same substantive disagreement survives two repair passes, report the
remaining disagreement and stop automatic cycling with the gate still unresolved.
An explicit authorized user waiver is a waiver, not ACCEPT; it cannot bypass higher
priority requirements. After ACCEPT, follow the project's execution/TDD gates in
the surrounding task. Any changed contract, test, fixture, or relevant code path
invalidates affected conclusions and needs a scoped re-review.
