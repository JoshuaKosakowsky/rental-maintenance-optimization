# Current handoff

## Dora's draft inputs and report section

- Branch `codex/14-dora-draft-inputs`. Dora (`chinchillad-ux`) prepared two
  synthetic workbooks and the problem, data, and assumptions draft. The
  [data notes](data/README.md) link the three original-format files.
- Checked all three Office packages and matched their SHA-256 hashes against
  the supplied files. Checked workbook keys, complete cells, base/scenario
  selection, quote references, and C's zero regular and overtime capacity.
- On Windows, `uv sync --locked`, `uv run --locked ruff check .`,
  `uv run --locked ruff format --check .`, `uv run --locked pytest` (2 passed),
  and `uv run --locked python scripts/check_repository.py` passed.
- Before using the draft data in the model, confirm the 40-job scope, overtime,
  deferral, and schema decisions with the team. The import checks covered data
  consistency. Model feasibility and results still require separate verification.

## Repository foundation

The public repository foundation is ready for team implementation. Start at the
[README](README.md) and [Project](https://github.com/users/JoshuaKosakowsky/projects/3).

- Scope: repository layout, guidance, dependencies, CI/release workflow, planning,
  security controls, and the disclosed AI reviewer policy.
- Planning: six parent issues, 26 native sub-issues, nine dated milestones, and
  all eight original proposal comments attached to the relevant issues.
- Dataset, mathematical model, optimizer, benchmark, results, and final report
  remain assigned team tasks. No project results are claimed by the setup tests.
- The original Word and PDF remain outside the public checkout.
- Python 3.12.14, Gurobi 13.0.3, pytest, Ruff, uv lock and hashed pip exports are set up.
- JoshKozy has accepted Write access. Its policy permits disclosed review and
  eligible merges and forbids all code/file edits and pushes.
- The Windows reviewer runtime still needs operator setup and verification:
  [issue #12](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues/12).
- Joshua will invite classmates and map their handles to the documented human leads.
- First team decisions: overtime, repair priority, the Thanksgiving writing date,
  and Track A recording details; see scope parent #1. Original dates are preserved.
- [Setup evidence](docs/repository-setup.md) links checks and live GitHub controls.
