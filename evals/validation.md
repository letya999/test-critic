# Validation record

Historical initial-version record. Later changes and targeted checks are documented
in [revision-validation.md](revision-validation.md); samples below do not validate
the revised payload.

Date: October 10, 2026. This record distinguishes artifact validation, native-agent
review samples, and execution of synthetic authoring controls.

## Artifact checks performed

- Codex skill-creator quick validation: passed for the source and portable copy.
- skill-conductor deterministic validation: **17/17** checks passed for the portable
  payload. The authoring root intentionally has a README; it is excluded from the
  payload and therefore does not create a packaging warning there.
- All portable Markdown links and evaluation JSON/fixture references checked.
- Package contents checked byte-for-byte against the nine allowlisted source files:
  SKILL.md, seven references, and optional agents/openai.yaml. No evals, private
  context, README, AGENTS, scripts, or authoring state are included.
- Gitleaks directory scan: no leaks found in the scanned project at that point.
- Independent static artifact review: no material contradictions or unsafe/nonportable
  assumptions reported. This is a review result, not proof of behavioral effectiveness.

An initial human-readable validator invocation hit Windows console encoding for an
emoji. Its JSON mode ran successfully; this was a reporting issue, not a skill failure.

## Behavioral samples actually performed

Eighteen fresh native-agent contexts completed reviews: nine with the skill and nine
without it. Each condition included five repetitions of retry-pressure and one run
of each of the other four fixtures. Skill references were available only to the
with-skill condition. Grading keys and other replies were withheld from executors.
No runtime skill wording was changed after observing these outputs.

| Case | Observed decisions in both conditions |
|---|---|
| Retry pressure, five samples per condition | Require repair; identify absent-key equality and constant-factory masking; retain the boundary fake. |
| Clean adapter | Accept the real adapter's exact dispatch test with a transport mock. |
| API suspension | Require an existing owned document, typed denial and unchanged stored state. |
| Browser recovery | Replace synthetic submit with normal activation; preserve the regression and legitimate API stub. |
| Evidence and cost | Preserve the sound pricing regression, reject excluded/vacuous sorting and unsupported latency claims, retain distinct restart protection. |

Output-level assertion grading and quotes are stored in [results.json](results.json).
Raw replies, per-run grades, input metadata and payload hashes are retained locally
under `.eval-work/benchmark/iteration-1/`; that local directory is not distributed.
The standalone local review viewer includes the preserved replies and grades.

One baseline pressure reply additionally required exactly one key-factory invocation.
The supplied contract constrains outgoing keys, not internal call count; this is an
unnecessarily coupled repair. It is a calibration observation, not evidence of a
reliable measured advantage. Both conditions found the principal planted defects.

## Executable authoring controls

An isolated authoring script executed the exact Python retry example from the
fixture. It verified that the weak test passes with the header deleted, that a
strengthened assertion fails for that fault, and that the restored baseline passes.
A separate assertion demonstrated that identity sorting satisfies the weak
idempotence property while violating the required order.

These are actual executed synthetic controls. They were performed by the authoring
harness, not the runtime critic. The browser, native-platform and API fixture code
was reviewed as text, not run against live applications.

## Limits

- These are small authored development cases, not an unseen holdout, a production
  rollout, or a statistically established superiority benchmark. No accuracy or
  productivity uplift is claimed.
- The independent grader evaluated final-output content. Native executor tool traces
  were not exported; actual action compliance is unverified, despite explicit no-run
  instructions and consistent self-reports. No hidden-action audit is claimed.
- The host did not expose per-run model identifiers, tokens or durations in completion
  notices; these are recorded as unavailable, not zero or estimated costs.
- Eight trigger examples were inspected as description fit; the host's actual
  automatic skill-selection mechanism was not exercised.
- No live project suite, CI gate, browser/device session, or mutation campaign was
  run through this skill. Missing-API and requirement-conflict behavior have written
  rules but no dedicated behavioral fixture in this initial set.
- No global skill installation, commit, push, deployment, or changes to test-designer
  were performed. Markdown instructions alone do not technically enforce the gate.
