# Contributing

This setup supports the four-person proposal in [the team plan](docs/team-plan.md).
Joshua adds classmates as collaborators; do not guess account handles or invite
people not named by the owner. Until handles are confirmed, issues identify the
proposal's human lead in their body and leave GitHub assignment open.

## Working on a task

1. Read the parent issue, task acceptance criteria, requirements, and relevant
   source notes. Claim a task and confirm dependencies before implementing it.
2. Branch from current `main`. Agents use `codex/<issue>-<description>`; humans
   may use `feat/`, `fix/`, or `docs/`. Never work directly on protected `main`.
3. Make the smallest complete change. Reuse functions from
   `src/rental_maintenance/`; use `common/` only for genuinely shared helpers.
4. Run the checks listed in README plus tests relevant to your change. Inspect
   the diff for accidental data, secrets, solver licenses, and generated files.
5. Open a PR using the template. Use `Closes #N` only when the whole task is
   complete; use `Refs #N` for partial work. Include actual validation evidence.
6. Request an eligible review, address blocking findings, and refresh approval
   after code changes. Merge only after the active GitHub checks and rules pass.

The initial foundation is owner-authorized bootstrap work. Once protections are
active, the same review/check requirements apply to owner and automated accounts;
do not disable them to finish a task. [GitHub setup](docs/repository-setup.md)
records the observed state. No local blocking hooks are installed.

## Roles and review

Creators implement, explain, and test their changes. Reviewers check acceptance,
model correctness, reproducibility, and safety. Separate concrete defects from
optional style/refactor suggestions. Batch findings with a trigger, expected
behavior, actual behavior, location, and useful verification steps.

An eligible human reviewer must not have implemented the PR. JoshKozy is an
owner-authorized, fully AI reviewer, operating under [its restricted policy](docs/ai-reviewer.md).
It never writes code, patches, tests, configuration, documentation, or commits.
It can inspect, comment, approve/request changes, and merge eligible PRs. Its
review is its handoff. A separate coding agent or human implements fixes.

Both named accounts belong to Joshua. Another GitHub account is not another
human. Coding agents cannot switch to JoshKozy to approve their own work, and
JoshKozy cannot approve or merge changes to its own authority, tools, credentials,
or policy. Such changes need an eligible human reviewer; leave them open until
one is available. Do not dismiss a blocking finding without evidence and an
eligible confirming review.

## Shared ownership and decisions

The proposal assigns leads; it does not make Anete responsible for writing other
members' sections. Everyone provides their own AI-use notes and recording segment.
Agree on data schema and interfaces before dependent coding. Do not build against
assumed unmerged changes. Record overtime, priority, recording, and schedule
decisions in their issues and summarize adopted outcomes in `docs/decisions.md`.

Use Project Status for Backlog, Ready, In progress, In review, and Done. Labels
describe type and area; do not maintain competing status labels. An issue being
assigned does not mean work has started. Keep parent issues open until integrated
deliverables satisfy all their acceptance criteria.

## Reproducibility and records

Dependency changes begin in `pyproject.toml`, then update `uv.lock` and regenerate
both requirements files using the commands in `docs/reproducibility.md`.
Do not report a skipped or mocked solver check as real verification. A successful
solver status proves properties of the coded model, not its business assumptions.

Issues own live work status; team-plan owns agreed dates/roles; README owns setup;
verification owns model evidence; AI_USE owns assistance disclosure. Update the
affected source rather than duplicating every update everywhere. Agents keep a
short current `handoff.md` entry with actual tests, remaining gaps, and next steps.
