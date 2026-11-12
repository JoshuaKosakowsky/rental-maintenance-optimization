# Verification work

`test_environment.py` verifies Python 3.12 and a tiny Gurobi solve. Passing it
does not verify the rental-maintenance formulation, data, or results.

Josh leads independent model verification with Izzy. Add tests for input data,
the greedy benchmark, independent feasibility/cost checks, and the implemented
model as those tasks are completed. Include independently checked small examples,
infeasible instances, invalid inputs, and equivalent optimal solutions.

Never skip a required solver check because a license or dependency is missing.
Report the actual failure and fix the environment.
