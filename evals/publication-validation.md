# Publication checks — October 10, 2026

The public repository adds English/Russian usage docs, MIT license, contributor and
security policies, authoring validation, CI and protected release flow. Runtime
review instructions are unchanged by these repository-maintenance additions.

## Local evidence

- Public artifact validator passed: folded frontmatter, seven references, license,
  metadata, local links, JSON and fixture references.
- Two isolated unit checks passed: missing references block publication and the
  ten-entry archive excludes evaluation/private state while including the license.
- pre-commit validation and staged Gitleaks passed; directory and initial history
  scans found no leaks. TruffleHog reported zero verified/unverified findings.
- Ruff and Bandit passed on the two public authoring scripts. Opengrep's local
  rule set reported no unsuppressed findings on scripts and Actions.
- One generic Opengrep rule flags any pull_request_target trigger. The documented
  narrow suppression covers the metadata-only branch policy: no checkout, project
  execution, secrets or writes. Source branch and repository names are passed as
  environment data, not interpolated into shell code. CodeQL remains independent.
- Archive CRC, exact entry names and source bytes were verified. Private authoring
  state and attachments are ignored and excluded from commits and distribution.

## Scope and limits

The general ai-repo-safety scan initially failed in pip-audit because its helper
Python environment lacks pip; no dependency result is claimed. This project has no
third-party Python dependencies or package manifest: public scripts use only the
standard library. Applicable Python/security checks were run directly; Actions
dependencies are pinned and tracked by Dependabot. No cloud skill scanner ran.

GitHub CI results and branch settings are authoritative in the repository UI/API;
this document does not predict their result. The initial and revised behavioral
samples remain historical. No automatic trigger-rate measurement or production
test suite was added. skills.sh discovery is supported by root SKILL.md and a public
install command; actual directory appearance depends on install telemetry/indexing.
