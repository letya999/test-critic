# Maintaining test-critic

This project authors one portable Agent Skill. Read `SKILL.md` and the affected
reference before editing. Keep all distributed content and project documentation
in English; respond to users in their language.

## Boundaries to preserve

- The runtime critic is an independent reviewer role, read-only before execution.
  Actual independence needs fresh context; retained authorship is self-review.
  No runners, collection/import, mutations, installations or automatic delegation.
- Separate design, authoring, critique, execution and production implementation.
  ACCEPT clears only static review. Review-only does not authorize file edits.
- Review code and configuration, including callers/fixtures and removed protection.
  Never use coverage percentages or the author's confidence as a substitute.
- Require concrete findings and minimal repairs. Protect sound mocks, smoke checks,
  snapshots and cross-level tests from ideological false positives.
- Honor project instructions and user authority; no silent hook/tool bypass, no
  invented mandatory stack, no personal paths/secrets in the portable payload.
- Preserve test-designer/Ponytail/Probity/Memory Bank cooperation without requiring
  any of them. Do not edit the sibling test-designer project as part of this skill.

## Layout

`SKILL.md` is the compact entrypoint; `references/` contains targeted supporting
instructions and provenance. `agents/openai.yaml` is optional UI metadata. README,
this file and `evals/` are authoring material, not runtime dependencies. No `docs/`
tree, second memory system, runner wrapper or enforcement framework is needed.

## Validation

Run available Agent Skills/frontmatter validators and check all local Markdown
links and JSON. A clean structure does not prove behavioral effectiveness.

For material instruction changes, use `evals/protocol.md`. Skill-authoring evaluations
may use fresh independent agents; this is distinct from runtime critique. Keep
baseline and with-skill inputs identical except for skill availability, hide grading
keys, include clean controls and pressure, and preserve raw outputs. Grade exact
findings, omissions, false positives and phase violations, not verbose checklists.

Use isolated authoring workspaces for test execution or generated artifacts; do not
run arbitrary fixture code through the runtime critic. Do not label static review
as executed validation, or one small evaluation as a reliable measured uplift.

Package only `SKILL.md`, `references/`, `agents/openai.yaml` and `LICENSE` under `test-critic/`.
Validate the packaged copy and links. Exclude evals, private task context, caches,
scanner state, .git, README and AGENTS. Do not install globally, publish, commit or
push unless requested by the user.

## Public repository maintenance

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Work on `dev`
or a feature branch targeting `dev`; `main` accepts only a release PR from this
repository's `dev`. Never bypass protection, disable checks or force-push a protected
branch. Keep `dev` after merging releases. Treat the owner's explicit publication
instruction as authorization; do not ask again for already-authorized actions.

Run `python scripts/validate.py` and the focused script unit tests before commit;
build with `python scripts/validate.py --package` when runtime payload changes.
Run staged/history secret scans before publication. CI uses minimal permissions
and full SHA-pinned Actions. Dependabot updates target `dev`. The branch-policy
workflow uses trusted base metadata only: never add checkout, user code or secrets
to that `pull_request_target` job.

Keep the root `SKILL.md` discoverable by the skills CLI. Runtime instructions remain
English; English and Russian README usage/guarantees must agree. Authoring scripts
are repository maintenance tools, never commands for the runtime critic. Keep their
dependencies in the Python standard library. Do not publish personal paths, private
chat links, customer data, raw private traces, local scanner state or attachments.
Do not fabricate skill-catalog listing, scan coverage, benchmark uplift or guarantees
of stability. Inspect remote settings after changing them and report actual CI
results. Route prompt-injection and security reports privately as documented.
