# Repository setup and observed state

Repository: [JoshuaKosakowsky/rental-maintenance-optimization](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization).
Owner-approved visibility: public. Default branch: main. License: Apache-2.0.
The checkout has fresh history separate from the surrounding course repository.
Original proposal/PDF files are excluded from publication.

## Setup verification record

Verified during the November 11, 2026 setup (America/Denver; November 12 UTC):

- The public [Project](https://github.com/users/JoshuaKosakowsky/projects/3) contains
  all 32 issues, initially in Backlog. It has Workflow and Team plan views.
- [Issues](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues)
  contain six parents and 26 native sub-issues. All eight embedded Word comments
  were copied verbatim to the matching task/decision issues with source anchors.
- [Nine milestones](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestones)
  preserve all eight proposal dates and the December 10 course deadline.
- JoshKozy accepted the collaborator invitation; Write permission was verified.
  The Windows restricted reviewer runtime remains [issue #12](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues/12).
- [Cross-platform CI](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/actions/runs/43153963133)
  passed on Linux, Windows, and macOS. Local Ruff, two environment tests,
  dependency-export checks, repository checks, and a clean hashed pip install
  passed. The pip path is also checked by the final CI configuration.
- CodeQL default setup is configured for Python and GitHub Actions; both initial
  analyses passed in [the setup scan](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/actions/runs/43155302469).
- Secret scanning, push protection, dependency alerts/security updates, and private
  vulnerability reporting were enabled and read back from GitHub.
- Default workflow permissions are read-only; Actions cannot approve PR reviews;
  repository action policy requires full commit SHA pins.

The [main ruleset](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/rules/27091613)
and [version-tag ruleset](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/rules/27091616)
are the authoritative live controls. Main enforcement is activated after the final
bootstrap commit passes CI. The final activation audit is recorded on
[scope parent #1](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues/1);
consult that evidence and the live ruleset rather than inferring activation from
this policy text.

## GitHub control configuration

- Require pull requests, one eligible approval, dismissal of stale approvals,
  approval after the latest push by another account, and resolved conversations.
- Require the stable GitHub Actions `test` check and an up-to-date branch.
- Block force pushes and deletion of main; no bypass actors, including admins.
- Protect version tags from deletion and forced updates.
- Use squash merges and delete merged branches automatically.
- Enable secret scanning, push protection, private vulnerability
  reporting, dependency graph/alerts, and dependency update PRs.
- Use read-only default workflow tokens, SHA-pinned actions, no persisted checkout
  credentials, and no public-PR access to credential secrets.

`CODEOWNERS` records the two confirmed account contacts. Required code-owner review
is not enabled before teammate handles and ownership are agreed; the ordinary
independent approval requirement still applies. The fully AI reviewer cannot
approve its own authority/policy changes. No local blocking Git hooks are installed.

## Planning conventions

Native parent/sub-issue links represent hierarchy. Milestones preserve all eight
proposal dates plus the course deadline. Issue bodies retain human leads without
guessing unknown collaborator handles. The owner will invite classmates separately.

The Project uses Status (Backlog, Ready, In Progress, In review, Done), Priority,
and native issue fields such as milestone/assignee/parent. Labels classify issue
type and work area rather than duplicating status. Issues are the live work record.
The auto-add filter is scoped only to this repository's open issues. Native
sub-issues are automatically added when their parent is in the Project. Priority
values and GitHub assignees remain unset until the team agrees them.

## Workflows

`ci.yml` validates Linux, Windows, and macOS environments, formatting/linting,
pytest, repository checks, and dependency export consistency. A stable aggregate
`test` gate fails if any required job fails or is unexpectedly skipped.

`release.yml` packages a checked commit on main as a source archive for a version
tag. It does not certify final course deliverables or claim optimization results.
Do not tag a submission release until its real acceptance checks are complete.

When settings change, verify live GitHub state and update this record. A Markdown
policy or JSON file alone does not activate server-side protection.
