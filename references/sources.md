# Research and design rationale

Original synthesis researched on October 10, 2026. Read for provenance, not as a
mandatory runtime dependency. Links to live documentation and branches can change;
check the project's installed version before using framework-specific semantics.

## Constraints inherited from the supplied project context

The supplied backend-test-critic provided a useful starting point: business meaning,
realistic data, observable outcomes, necessity, and a repair loop. The later explicit
context narrowed the role to same-session static critique after writing and before
running tests. That later clarification is retained instead of importing the sample's
mandatory independent-agent workflow or universal pre-implementation failure rule.

The local test-designer handoff informed project-rule precedence, framework-neutral
boundaries, and cooperation with Ponytail, Probity and Memory Bank. It is optional
context, not a dependency. Private source messages, personal paths and transcripts
are not redistributed. No claim is made to have verified unavailable original archives.

## Sources investigated and what was adopted

| Source | Applied idea / limit |
|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | Portable YAML frontmatter, a concise entrypoint and relative references. The format does not enforce a workflow. |
| [Google Testing Blog — Test Behavior, Not Implementation](https://testing.googleblog.com/2013/08/testing-on-toilet-test-behavior-not.html?hl=de_AT) | Behavioral assertions should tolerate harmless implementation changes. Internal interaction assertions remain valid when the interaction itself is the contract. |
| [GoogleTest — gMock Cookbook](https://google.github.io/googletest/gmock_cook_book.html) | Distinguish meaningful interaction expectations from unnecessarily constraining implementation. No C++ or mock-framework dependency is adopted. |
| [jamestexas — test-fidelity](https://github.com/jamestexas/agents/blob/main/skills/test-fidelity/SKILL.md) | Trace actual-value origins, overly permissive assertions, unreachable inputs and unsubstantiated coverage. Its special analysis tools, coverage execution and delegation are not adopted. |
| [Trail of Bits — property-based-testing](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | Consider meaningful properties for structured data and review whether generated cases exercise the claim. Property-based testing is optional, not inherently superior. |
| [Hypothesis — strategies reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) | Generator domains and filtering affect which cases are reachable. No mandatory framework or sample quota. |
| [Testing Library — considerations for fireEvent](https://testing-library.com/docs/guide-events/) | A dispatched event may omit parts of a real interaction sequence. Low-level events are not automatically wrong; match the tested claim. |
| [Playwright — best practices](https://playwright.dev/docs/best-practices) | User-visible behavior, isolation, stable locators and awaited operations. No mandatory browser execution during critique. |
| [pytest — flaky tests](https://docs.pytest.org/en/stable/explanation/flaky.html) | Uncontrolled state, order dependence, overly strict assertions and thread lifecycle can undermine reliability. Generalized beyond Python. |
| [Stryker — mutant states and metrics](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/) | Separate killed, survived, uncovered, timeout and invalid outcomes. The critic's behavioral-evidence rule is deliberately narrower than a tool's raw detected score. |
| [Google SRE — Testing for Reliability](https://sre.google/sre-book/testing-reliability/) | Different test levels, smoke checks and performance/reliability goals have distinct purposes. No universal test ratio, arbitrary timing budget or production test execution. |
| [Android — testing strategies](https://developer.android.com/training/testing/fundamentals/strategies) | Fidelity and scope depend on the level and platform boundary. Native guarantees cannot be inferred solely from host-side logic tests. |

## Decisions from the synthesis

- Review proof chains, not assertion counts or coverage targets. Source-level
  counterexamples make criticism falsifiable without falsely claiming execution.
- Separate review acceptance from runtime evidence and implementation gates. A good
  new regression may intentionally fail; a refactor test may correctly stay green.
- Be severe about a demonstrated false pass, but protect useful tests from blanket
  bans on doubles, snapshots, smoke checks, or cross-layer overlap.
- Include suite cost and performance-test validity as separate concerns. Do not add
  benchmarks just to sound rigorous or treat a noisy timing assertion as an SLO proof.
- Require correction for substantial findings without an infinite escalation loop.
  Explicit waivers remain visible; ordinary technical disagreements need evidence.

## Research limits

This is not an exhaustive literature review or a comparative evaluation of the
linked tools. No paid book was read in full, no published experiment reproduced,
and no reliability percentage is inferred from documentation or source popularity.
Behavioral evaluation of this skill is recorded separately in the project's evals.
Instructions are newly written; source code and third-party skill text are not
vendored. Review licensing before future verbatim reuse.

## Approved role clarification

The later user request clarified that the critic is an independent reviewer of
written tests. This revision keeps pre-execution, read-only review and separates
author repairs from critic decisions. Fresh context provides actual independence;
same-context self-review is explicitly labelled. Diagnostic, stability, schema and
cross-operation checks were added without moving scenario design into this skill.
The supplied research note is useful as a hypothesis bank; its unsupported statistics
and mixed design/execution workflow are not accepted as established evidence.
