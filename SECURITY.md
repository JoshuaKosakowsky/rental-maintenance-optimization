# Security

Do not post credentials, solver license contents, tenant information, private
documents, or sensitive logs in public issues or PRs. Keep all project inputs
synthetic. Store local license files outside the checkout and never upload them
as workflow artifacts.

Use GitHub's private vulnerability reporting under the repository Security tab
when enabled. If that option is unavailable, contact the repository owner through
an existing private channel rather than publishing sensitive details.

CI uses minimal token permissions and SHA-pinned actions. Public PR validation
must not receive deployment, reviewer, model-provider, or solver-account secrets.
Do not execute untrusted PR code in a credentialed reviewer broker.

Report a leaked credential immediately to its owner so it can be revoked and
replaced; deleting a file from the latest commit does not remove its history.
