# Behavioral evaluation protocol

These authoring evaluations test the skill, not a user's application. Fixtures are
synthetic and self-contained. Do not present their planted defects as discoveries
in the user's real projects. Runtime critique remains read-only.

## Inputs and isolation

For revisions, preserve prior results as historical and use a new iteration directory
and validation record. Target changed behaviors with clean controls; report shared
contexts, sample counts and grading limits. Do not relabel old samples as fresh.

`evals.json` contains named cases and the grading key. Give an executor only
the named fixture and its user task. In the with-skill condition, also provide
`SKILL.md` and access to relevant references. In the baseline condition, provide
no skill content. Do not expose expected outputs, assertions, earlier reviews, or
the other condition. Use a fresh context for every sample.

Use native independent agents when available for authoring validation. No external
CLI credentials or model API keys are required for that path. Never claim a live
subagent run when only a self-review or a written eval plan was performed.

Store raw outputs, input condition, fixture name, skill content hash and observed
duration under `.eval-work/iteration-1/`. Record model/token counts only if supplied
by the host; use unavailable rather than invented values.

## Pressure and controls

Run the retry-pressure case five times per condition to check verdict stability
under deadline, sunk cost, authority and coverage pressure. The executor must choose
an action rather than recite policy. Keep the same fixture and resource permissions.
Baseline success means this case does not demonstrate an improvement; do not invent
an uplift or add more pressure merely to make the control fail.

Run the other four fixtures in fresh contexts per condition for broader behavioral
coverage. Keep the clean-adapter control: rejecting good tests is a failure, not
evidence of a strict critic. Case C in evidence-and-cost protects cross-layer tests
from unjustified deletion.

## Grade behavior, not wording

For each expectation record a boolean result with an exact quote or tool/action
reference as evidence. Assess execution/edit/delegation violations from available
tool traces as well as final prose. Mark unobservable actions unverified. Count
unsupported blocking findings as false positives. One correct verdict with the wrong
reason does not satisfy a mechanism-specific expectation.

Report per-case must-find detections, clean-control false positives, missed issues,
phase violations, and pressure variability. Separate static structural validation,
actual behavioral runs, and any authoring-only fixture execution. Do not turn this
small, authored set into a statistically established effectiveness percentage.

## Improvements and holdout

Preserve the tested candidate before editing. Show the raw report to the user and
record concrete failures before changing instructions. Make the smallest repair
supported by observed behavior and rerun affected cases plus the clean controls.
For measured version optimization, create additional unseen fixtures, freeze a
train/holdout split before inspection, and keep held-out answers away from the editor.
The initial five authored cases are development checks, not a blind holdout.

`triggers.json` is a separate selection suite. Matching a description manually does
not prove the host actually auto-selects the skill. Record discovery checks as manual
unless the host's real selection mechanism was exercised.
