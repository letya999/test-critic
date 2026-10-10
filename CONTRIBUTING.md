# Contributing

Open issues for concrete test-review failures, misleading verdicts, missing platform
semantics or documentation problems. Use synthetic examples and remove credentials,
customer data and private project context. Report vulnerabilities privately through
[SECURITY.md](SECURITY.md).

## Branch flow

`feature branch → dev → main`. `dev` is the default development branch. Open ordinary
pull requests against `dev`. Only a pull request from this repository's `dev` may
update `main`; direct pushes, force pushes and deletion are blocked there, including
for administrators. Required checks and resolved review conversations gate merging.
Do not delete `dev` after a release merge. Maintainers may merge a release PR once
checks pass; no second maintainer is artificially required for this single-owner repo.

## Checks

Authoring tools require Python 3.12+; the installed skill has no runtime dependency.

```bash
python scripts/validate.py
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/validate.py --package
gitleaks git --redact
```

Install [pre-commit](https://pre-commit.com/) and Gitleaks, then run `pre-commit install`
and `pre-commit run --all-files`. CI also scans Python and Actions with CodeQL.
Dependencies in Actions are SHA-pinned and updated by Dependabot.

For instruction changes, follow [evals/protocol.md](evals/protocol.md): include clean
controls, keep reviewer and author roles separate, preserve historical results and
report actual evidence limits. Do not claim better trigger rates from description
inspection or claim behavioral quality from structural checks. Changes to observable
behavior need focused evaluation; README-only changes do not need a full benchmark.

Keep runtime instructions and the English README in English. Update the Russian
README when public usage or guarantees change. Use small, focused commits explaining
the resulting behavior. Do not distribute evals or local state in the `.skill` archive.
