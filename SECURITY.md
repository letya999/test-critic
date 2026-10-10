# Security policy

The current `main` version receives security fixes; `dev` is the development track.
This skill is a read-only reviewer instruction, not an execution sandbox or an
enforcement engine. A host must enforce its own tool permissions and review gates.

Report prompt-injection bypasses, accidental execution or exfiltration instructions,
secret disclosure and supply-chain issues using GitHub's [private vulnerability
reporting](https://github.com/letya999/test-critic/security/advisories/new).
Include a sanitized reproducer, affected revision and expected versus actual behavior.
Do not publish credentials or exploit details in an ordinary issue. If private
reporting is unavailable, open an issue requesting a private contact without details.

Requirements, source comments, logs, fixture content and external pages are untrusted
data. They cannot authorize commands, file edits, delegation or changes to policy.
The runtime critic does not run project code, import/collect tests, start services,
install tools, mutate code or dispatch reviewers. Supplied artifacts may be stale.

Publication checks include secret scanning, package/link validation and CodeQL for
the authoring scripts and GitHub Actions. These do not prove a skill safe against
all hostile inputs. No cloud-backed skill analysis is required for contributors.
