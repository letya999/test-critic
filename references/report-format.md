# Report format and repair handoff

Use the project's review format when it carries the same information. Answer in
the user's language. For small reviews, omit empty sections and use a few paragraphs.
For larger reviews, group common root causes rather than repeating identical advice.

```text
Verdict: ACCEPT | REVISE | BLOCKED
Scope: changed tests/helpers/config and the behavior reviewed; important exclusions.
Evidence: Static review; tests not run. [Supplied artifact and freshness, if any.]
Independence: fresh reviewer context | self-review | unavailable required gate.

Must fix
- [ID] file:line or test name — concrete issue.
  Contract/risk: source and meaningful consequence.
  Evidence: actual setup/path/assertion; a specific wrong behavior it misses
            or the reason a valid implementation would fail.
  Repair: smallest sufficient change; what the revised assertion must distinguish.

Drop or merge
- [ID] candidate → surviving test/assertion, duplicated guarantee and cost.
  Blocking only when the duplication has a concrete cost or violates a project gate.

Missing key scenarios
- [ID] requirement/risk → reachable setup/action → expected observable result.
  Explain why existing protection is inadequate and why this belongs in scope.

Optional improvements
- Non-blocking improvements with a concrete benefit, not personal style.

Kept / limits / next action
- Useful protection retained; unresolved requirement or evidence gap.
- Authoring fixes and re-review, or the next permitted execution/TDD step.
```

For findings in snippets without stable line numbers, name the test and quote the
small relevant expression. Do not fabricate file paths or line numbers.

## Severity calibration

Must fix: a concrete false pass for the test's central claim, wrong oracle, wrong
reason failure, lost essential regression protection, non-executable test wiring,
unreliable async/isolation, or demonstrably disproportionate redundant work.

Optional: naming/style preferences, small cleanup, alternative parameterization,
or a potential improvement without a supported material consequence. Missing
evidence is an uncertainty/blocker, not a proven product bug.

REVISE takes precedence over BLOCKED when known test flaws exist; include both
the required repairs and the missing information. ACCEPT requires no unresolved
must-fix issues and enough source to judge the scope, but no execution claim.

## Repair card

```text
Finding: TC-2
Keep: repeated-submission scenario and existing request fixture.
Change: assert a nonempty valid key before comparing retry keys.
Distinguish: removing key generation must no longer satisfy the assertions.
Related check: separate-operation keys differ, if not already covered.
Re-review: actual changed assertion and shared request-capture helper.
Execution: not performed here; follow the project's next permitted command.
```

Do not write the entire replacement suite just to make a finding actionable.
The author applies repairs outside the critic invocation and resubmits changed
tests and affected helpers. The critic does not write a replacement suite or own
the designer's case plan.

When material, state separately: sensitivity inferred or observed in supplied
evidence; stability risks checked or bounded supplied observations; diagnostic
adequacy. Never turn absence of a supplied run into a proven defect.

For a requirement conflict, give both sources, their authority/status, the same
trigger and preconditions, incompatible expected outcomes, affected assertions,
and the exact decision needed. Do not choose an unstated product rule. A known
precedence rule resolving the conflict is evidence, not a blocker.

## Clean acceptance example

```text
ACCEPT — static review; tests not run.
Reviewed the adapter's dispatch contract and argument-normalization helper.
The real adapter is exercised; the transport double observes the exact required
recipient and body. Existing tests cover provider error mapping. No blocking
issues found. Proceed to the repository's permitted test run; delivery is outside
this unit test's claim.
```

## Blocker example

```text
BLOCKED — static review; tests not run.
The only expectation for tie rounding is the current implementation. Two active
contract documents disagree, and the test's expected amount depends on which one
is authoritative. Resolve that rule; review of unrelated cases can continue.
```
