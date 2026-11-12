# Verification plan and evidence

Josh leads independent verification with Izzy. No rental-maintenance model results
have been verified yet. `tests/test_environment.py` only checks Python and a tiny
Gurobi installation solve.

## Required project checks

- Work a small instance independently by hand and compare its result to the code.
- Validate every required repair is assigned exactly once, the selected contractor
  is qualified, and available hours are respected.
- Recompute objective cost from original inputs and selected assignments.
- Inspect solver termination status and solution availability before using results.
  Record bounds/gaps where relevant; do not label a time-limited incumbent optimal.
- Test invalid inputs, infeasibility, and alternative equally optimal assignments.
- Verify the greedy benchmark follows fixed ordering and documented tie-breaking.
  A greedy dead end is not proof of model infeasibility.
- Compare costs only for equivalent completed workloads. Report unfinished work
  separately rather than presenting its lower cost as a saving.
- Verify both scenarios modify exactly the documented inputs and interpret results.

An independent enumeration oracle is a possible additional check: eight jobs and
three contractors give 3^8 = 6,561 assignments before feasibility filtering.
Keep this independent of the model's constraint-building code. It is a proposed
verification technique, not an implemented or completed test.

## Evidence to record when work is completed

For each check, record the tester, date, source commit, input/version, command,
expected result, observed result, and limitations. Link CI or saved reports where
appropriate. Record failures and skipped checks honestly. Solver OPTIMAL alone
does not validate the problem translation or assumptions.
