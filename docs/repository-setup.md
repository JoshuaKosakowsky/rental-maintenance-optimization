# Repository setup and observed state

Repository: [JoshuaKosakowsky/rental-maintenance-optimization](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization).
Owner-approved visibility: public. Default branch: main. License: Apache-2.0.
The checkout has fresh history separate from the surrounding course repository.
Original proposal/PDF files are excluded from publication.

## Setup verification record

Setup is in progress. This section will be updated with observed repository,
Project, milestone, issue, invitation, CI, and protection results before handoff.
Planned settings below are not a claim of activation.

## Intended GitHub controls

- Require pull requests, one eligible approval, dismissal of stale approvals,
  approval after the latest push by another account, and resolved conversations.
- Require the stable GitHub Actions `test` check and an up-to-date branch.
- Block force pushes and deletion of main; no bypass actors, including admins.
- Protect version tags from deletion and forced updates.
- Use squash merges and delete merged branches automatically.
- Enable available secret scanning, push protection, private vulnerability
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

The Project uses Status (Backlog, Ready, In progress, In review, Done), Priority,
and native issue fields such as milestone/assignee/parent. Labels classify issue
type and work area rather than duplicating status. Issues are the live work record.

## Workflows

`ci.yml` validates Linux, Windows, and macOS environments, formatting/linting,
pytest, repository checks, and dependency export consistency. A stable aggregate
`test` gate fails if any required job fails or is unexpectedly skipped.

`release.yml` packages a checked commit on main as a source archive for a version
tag. It does not certify final course deliverables or claim optimization results.
Do not tag a submission release until its real acceptance checks are complete.

When settings change, verify live GitHub state and update this record. A Markdown
policy or JSON file alone does not activate server-side protection.
