# Reproducibility

## Foundation environment

Python is pinned to 3.12.14 and uv to 0.12.19. `pyproject.toml` declares Gurobi
13.0.3 and the approved development tools. `uv.lock` records exact dependency
resolution; exported requirements include package hashes for pip users.

CI installs the pinned Python through uv's managed Python distribution on each
platform. Gurobi 13.0.3 matches the locally verified version-13 license; an initial
version-14 check correctly failed rather than being skipped. Major solver updates
require an explicit compatibility review and are excluded from automatic update PRs.

Use the README's uv or pip path to install the editable `rental_maintenance`
package. Both paths use the same locked runtime/development dependencies.
Hatchling is included in development requirements so the documented pip editable
install can use `--no-build-isolation --no-deps` without another resolution.

## Update dependencies deliberately

Edit `pyproject.toml`, resolve and review the lock, then export both files:

```bash
uv lock
uv export --locked --no-dev --no-emit-project --no-header --output-file requirements.txt
uv export --locked --no-emit-project --no-header --output-file requirements-dev.txt
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv run --locked python scripts/check_repository.py
```

Do not manually maintain two different dependency lists. CI compares the committed
requirements with fresh exports from the lock and fails on drift. Change Python,
uv, or solver versions deliberately and verify supported operating systems.

## Solver access

Gurobi's [pip installation guide](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python)
states that the package includes a limited license for small models. The tiny
environment test deliberately fits that license. The future eight-job model's
actual size and successful runs still need to be verified. Do not assume an
academic license file works on GitHub-hosted runners or publish one in the repo.

No license credentials are configured in CI. Solver failures must fail visibly;
do not silently skip them. If project scope outgrows the available license, agree
an appropriate licensed environment or instructor-approved solver before claiming
reproducibility. [Supported Gurobi platforms](https://docs.gurobi.com/projects/optimizer/en/13.0/reference/releasenotes/platforms.html)
include Python 3.12; retain exact version evidence with project runs.

## Analysis run contract to implement

Izzy will supply the real analysis command and expected outputs after the runner
and data exist. Each run should identify its scenario, source commit, input
checksums, configuration, Python/solver versions, solver settings, random seed if
used, termination status, available solution, objective, and gap/bound where useful.

Preserve base inputs. Record scenario changes explicitly. Publish tables with
units and report incomplete/infeasible cases honestly. Compare costs only for
equivalent completed workloads. Validate all business rules independently of the
model builder. Selected report figures must be traceable to their producing run.

Before submission, a teammate follows the README from a clean checkout/unpacked
package and compares the key numerical results within documented tolerances.
Equivalent optimal assignments are acceptable when feasibility/objective agree.
Record the environment and evidence; do not require a particular tie solution
unless the team explicitly specifies a tie-breaking rule.
