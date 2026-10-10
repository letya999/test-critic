# Test Critic

[Русский README](README.ru.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

[![CI](https://github.com/letya999/test-critic/actions/workflows/ci.yml/badge.svg?branch=dev)](https://github.com/letya999/test-critic/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![skills.sh](https://skills.sh/b/letya999/test-critic)](https://skills.sh/letya999/test-critic)

A portable Agent Skill for reviewing written tests **before their first run**.
It requires meaningful regression protection and concrete repairs when tests give
false confidence. Backend, web, mobile, desktop, CLI, and library tests are in scope.

The normal flow is:

```text
test-designer (optional) → write tests → test-critic → repair and re-review
                                      ↓ ACCEPT
                           project test/TDD workflow
```

The critic is a read-only reviewer: it reads tests, requirements, implementation
paths, callers, helpers and configuration. It never authors repairs or runs tests.
Actual independence from the author needs fresh context with raw artifacts, without
the author's preferred verdict. Retained authoring context is labelled self-review;
it cannot satisfy a required independence gate. The host supplies reviewer context;
the skill adds no orchestration service or mandatory agent API.

## What it rejects

- Tests that observe their own mocks, copy production logic into the oracle, or
  compare values that can both be absent.
- Unreachable setups, wrong-reason failures, unawaited assertions, order dependence,
  and fixtures that erase the very behavior being claimed.
- Missing consequential outcomes, forbidden effects, realistic recovery paths, and
  meaningful boundaries within the change's scope.
- Tests excluded from the configured run, undisclosed placeholders, and unjustified
  expensive duplicates.
- Noisy timing checks presented as performance evidence or oversized fixtures with
  no additional protection.

It does **not** reject mocks, snapshots, smoke tests, multiple assertions, or overlap
between test levels on sight. Every blocking finding needs a supported consequence
and a minimal repair. A clean review is a valid result.

## Decisions

| Verdict | Meaning |
|---|---|
| ACCEPT | No material issue found in the scoped static review; proceed to the next permitted step. |
| REVISE | Repair supported test defects or material protection gaps, then re-review. |
| BLOCKED | Essential source, requirement, or required review capability is missing. |

Every verdict states that tests were not run. Missing runtime evidence is normal
before execution. ACCEPT does not prove tests pass, that production is correct,
or that TDD/CI gates have completed. A Markdown skill is not a command interceptor.

## Use

Install through the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add letya999/test-critic --skill test-critic
```

This follows the default `dev` branch. For the stable `main` track:

```bash
npx skills add https://github.com/letya999/test-critic/tree/main --skill test-critic
```

Use `--agent codex` or `--agent claude-code` to select a host; `--global` installs
for your user rather than the current project. Review the instructions before use.
The skill is framework-neutral; the host must provide allowed source access.
No paid service, test runner, MCP server or orchestration framework is required.

Install the portable payload as a directory named `test-critic` in the skill location
your agent host supports. Include `SKILL.md`, `references/`, and optionally
`agents/openai.yaml` for hosts that understand that UI metadata, and `LICENSE`. Exclude this README,
AGENTS.md, evals, and local authoring outputs. No runtime dependencies to install.

Examples:

```text
Use $test-critic on the new checkout tests. Review before running them.
Check these CLI tests for meaningful assertions and wrong-reason failures.
Review the retry tests: do they prove idempotency or only mock call counts?
Within this feature task, fix blocking test-review findings and re-review before execution.
```

For review-only requests, the output is a report. In an authorized feature/fix task,
the surrounding authoring task repairs tests and resubmits them to the reviewer
without asking for approval at each already-authorized step. Repository rules and actual execution permissions still apply.

## Files

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Trigger, workflow, strict criteria and verdict rules. |
| [Project context](references/project-context.md) | Source/tool discovery and cooperation with the user's setup. |
| [Review method](references/review-method.md) | Trace the proof and assess necessity/maintenance. |
| [Quality bank](references/quality-bank.md) | False-green mechanisms, legitimate doubles, properties and examples. |
| [Platform checks](references/platform-checks.md) | API/storage, UI, native, CLI, concurrency and performance. |
| [Evidence and gates](references/evidence-and-gates.md) | Static versus executed evidence; TDD and mutation-artifact interpretation. |
| [Report format](references/report-format.md) | Findings, severity and repair handoff. |
| [Sources](references/sources.md) | Research, provenance and limits. |
| [Evaluation protocol](evals/protocol.md) | Reproducible behavioral checks and scoring. |
| [Validation record](evals/validation.md) | Actual checks performed and known limitations. |
| [Revision validation](evals/revision-validation.md) | Targeted checks of reviewer boundaries, diagnostics and evidence. |

## Compatibility

The sibling test-designer chooses cases; this skill reviews authored tests. Ponytail
constrains unnecessary work while preserving meaningful coverage. Probity and project
hooks own their configured gates. Memory Bank owns document routing and persistence.
Serena, Context7, Semble, ripgrep, and other tools are used according to project policy
when available or required. The skill never silently bypasses a mandatory capability.

Research and examples are framework-neutral. Framework semantics still need version-
appropriate source or documentation. Strictness cannot eliminate model mistakes;
material findings should remain checkable against code and requirements.

## Evidence limits

The review checks diagnostic failures, flaky-test risk and plausible fault
sensitivity. Supplied logs can establish bounded observations, not universal
stability. Static review cannot guarantee that a test actually fails on the intended
defect. It surfaces contradictory requirements without deciding the product rule.
Historical evaluation results describe the version tested, not later revisions.

## Development and distribution

`dev` is the default development branch. Changes flow through feature branches to
`dev`; protected `main` accepts release PRs only from this repository's `dev`.
See [CONTRIBUTING.md](CONTRIBUTING.md) for required checks and contribution details.

```bash
python scripts/validate.py
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/validate.py --package
```

The archive is generated at `dist/test-critic.skill`; generated outputs and local
evaluation traces are not committed. Packaging includes runtime instructions and
MIT license only. CI validates links, fixtures, archive integrity and maintenance
tests; Gitleaks checks secrets, CodeQL checks Python/Actions, and Dependabot tracks
Actions updates. These checks are distinct from evaluating reviewer behavior.

The root SKILL.md is discoverable by skills CLI. [skills.sh listing](https://skills.sh/docs/faq)
is driven by CLI installation telemetry; repository publication alone does not
guarantee a listing, ranking or endorsement. No fabricated installs are used.

Released under [MIT](LICENSE). Research sources are linked in
[references/sources.md](references/sources.md); third-party material keeps its own license.
