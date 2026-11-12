# Agent instructions

Follow direct user instructions first. Apply these rules throughout this repository.

## Roles

The default role is a contributing coding agent. Joshua's coding identity is
`JoshuaKosakowsky`; classmates use their own authorized identities. Only Joshua's
separately launched, restricted reviewer profile for this repository, authenticated
as `JoshKozy`, follows `docs/ai-reviewer.md`. Reading that file does not select the
reviewer role or authorize switching credentials.

JoshKozy is fully AI and NEVER writes or changes code, tests, documentation,
configuration, branches, or commits. It cannot implement suggested fixes. It may
review and merge eligible changes through the restricted reviewer interface.
Its posted review is its handoff; instructions to edit handoff.md do not apply.

## Start and scope

Read README, CONTRIBUTING, handoff.md, the assigned issue, and relevant acceptance
criteria. Inspect the branch, working tree, and existing implementation first.
Preserve others' work. This is an independent repository; never stage, commit,
publish, or modify the surrounding course repository.

The authorized foundation includes repository setup, documentation, dependency
configuration, CI, planning, and issues. It does not authorize inventing project
data, completing the team's model, choosing overtime/priority policy, or writing
the final report. Those are separate assigned tasks. Ask about unresolved business
decisions rather than silently assuming values or expanding scope.

Original Word/PDF course documents and local credential/profile files must stay
outside this public repository. The owner approved Apache-2.0 for repository work.

## Implementation

Prefer simple, maintainable changes to existing code. Put reusable logic in
`src/rental_maintenance/`, with small shared helpers in `common/` only when needed.
Keep scripts thin. Do not introduce speculative frameworks, duplicate business
logic, or new dependencies without a clear benefit. Explain significant choices.

Use focused `codex/<issue>-<description>` branches and PRs. Required review and CI
apply to all accounts once main protections are active. Never weaken a gate,
self-approve through another identity, bypass an author hold, or claim unrun tests.
Do not use JoshKozy credentials from a coding session. The reviewer cannot approve
or merge its own policy, tools, credentials, or authority changes.

## Verification and finish

Run relevant tests and the README checks. Independently validate assignments,
qualifications, capacity, cost, and solver status when model code exists. Greedy
failure is not proof of infeasibility; compare costs for equivalent completed work.
No rental-model verification exists until its actual tests and evidence are added.

Update affected docs and a concise handoff entry: task/branch, changes, exact
checks and outcomes, unchecked areas, blockers, and next steps. Record AI help in
AI_USE.md when substantive. Explain what changed, why, and how it was verified.
