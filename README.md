# Rental Maintenance Optimization

MSBC 5680, Fall 2026 · Track A Optimization Analysis · Dora, Josh, Izzy, and Anete

This project will assign rental-property repairs to qualified contractors at the
lowest total cost while respecting available hours. The agreed starting scope is
eight repairs across six houses, three contractors, and one week. The data will
be synthetic and justified. Exact appointments and travel routing are outside
the proposal's scope.

**Current status: repository foundation only.** The dataset, mathematical
formulation, project optimizer, greedy benchmark, numerical results, and final
report are team tasks; they are not implemented or verified yet. CI currently
checks the development environment and repository safety, including a tiny
Gurobi installation check. It does not establish that the project is complete.

## Start here

1. Read [the requirements](docs/requirements.md) and [team plan](docs/team-plan.md).
2. Find your task in the [Project](https://github.com/users/JoshuaKosakowsky/projects/3),
   [parent/sub-issues](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues),
   and [dated milestones](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestones).
3. Follow [CONTRIBUTING](CONTRIBUTING.md) to branch, change, test, and open a PR.
4. Put reusable Python functions in `src/rental_maintenance/`; small shared
   helpers belong in `src/rental_maintenance/common/` when they have real callers.

Team readiness target: **December 3, 2026**. Canvas deadline: **December 10, 2026**.
The proposal's milestone dates are preserved. Dates do not imply a submission
time; the instructor's documents do not specify one.

## Repository map

```text
rental-maintenance-optimization/
├── .github/                Issue/PR templates, reviewers, dependencies, CI/release
├── src/rental_maintenance/  Importable reusable analysis code
│   └── common/             Small helpers shared by actual callers
├── data/
│   ├── base/               Dora's agreed synthetic base tables
│   └── scenarios/          Explicit input changes for the two alternatives
├── configs/                Nonsecret run/scenario settings
├── tests/
│   └── fixtures/           Small independently checked verification instances
├── docs/                   Requirements, formulation, verification, team guidance
├── reports/
│   ├── sections/           Each member's polished writing
│   ├── figures/            Selected figures with their producing run recorded
│   └── presentation/       Recording outline and speaking assignments
├── scripts/                Repository checks and source-package helpers
├── outputs/                Generated analysis results, ignored by Git
├── dist/                   Generated source archives, ignored by Git
├── README.md               Setup and navigation
├── AGENTS.md               Contributor and AI reviewer role boundaries
├── CONTRIBUTING.md         Team development workflow
├── AI_USE.md               AI assistance and how outputs were verified
├── SECURITY.md             Private security reporting and credential handling
├── LICENSE                 Apache License 2.0
├── pyproject.toml          Authoritative Python dependency declarations
├── uv.lock                 Exact resolved dependencies
├── requirements.txt        Generated runtime requirements for pip users
├── requirements-dev.txt    Generated development requirements for pip users
└── .python-version         Tested Python version
```

The original proposal and instructor PDF remain local, outside this public
repository. [Source notes](docs/source-notes.md) identify the source versions.

## Install and check

Use **64-bit Python 3.12**. The tested patch version is in `.python-version`.
The approved solver is Gurobi. This project pins `gurobipy==13.0.3`; another solver
requires instructor approval. Gurobi's pip package includes a limited license for
small models. Check the [solver notes](docs/reproducibility.md) before scaling up.

Recommended, using **uv 0.12.19**:

```bash
git clone https://github.com/JoshuaKosakowsky/rental-maintenance-optimization.git
cd rental-maintenance-optimization
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv run --locked python scripts/check_repository.py
```

These commands work in PowerShell and macOS/Linux shells once Git and uv are
installed. [Official uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)
explain installation and choosing a specific version.

Alternatively, use pip. In **PowerShell**:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --require-hashes -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pip install --no-deps --no-build-isolation -e .
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe scripts/check_repository.py
```

On **macOS/Linux**:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.txt
.venv/bin/python -m pip install --no-deps --no-build-isolation -e .
.venv/bin/python -m pytest
.venv/bin/python scripts/check_repository.py
```

`requirements.txt` contains runtime dependencies. `requirements-dev.txt` also
includes tests, linting, and the build backend for the editable install above.
Both are generated from `uv.lock`; do not edit them by hand. See
[reproducibility](docs/reproducibility.md) for regeneration and the future analysis
run contract. There is no project analysis command yet.

## Team and review

| Member | Responsibility |
| --- | --- |
| Dora | Problem, data and assumptions; recording coordination |
| Josh | Formulation and independent verification; collaborate with Izzy |
| Izzy | Python implementation, experiments, results, README |
| Anete | Recommendations, limitations, report integration, submission assembly |

Everyone supplies their own polished section, AI-use notes, and recording segment,
and reviews the final package. Joshua will invite classmates separately. Human
lead names are recorded in issues; unknown GitHub handles are not guessed.

**JoshKozy is a fully AI code reviewer operated for Joshua. It does not write
code or modify project files.** It may review and merge eligible PRs through a
separately configured restricted reviewer profile. Both JoshKozy and
JoshuaKosakowsky belong to Joshua: this is disclosed automated review, not another
human's review or another teammate's contribution. See [reviewer policy](docs/ai-reviewer.md)
and [setup status](docs/reviewer-setup.md). Cloning this repository does not install
or start that reviewer.

## Deliverables and license

Track A requires a 10–12-page double-spaced analytical report, reproducible Python
code and data, a short README, and a brief AI-use statement. The general
instructions/rubric also require a recording; confirm Track A's format with the
instructor. [The submission checklist](docs/submission-checklist.md) includes the
appendix limit and final review steps. Required files go to Canvas; a GitHub link
only supplements them.

Team-authored repository content is licensed under [Apache-2.0](LICENSE).
Third-party dependencies and the original course documents retain their own terms.
