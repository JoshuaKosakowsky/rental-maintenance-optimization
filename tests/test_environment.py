"""Verify the approved runtime and solver installation, not the project model."""

import sys

import gurobipy as gp
import pytest
from gurobipy import GRB


def test_python_version():
    assert sys.version_info[:2] == (3, 12)


def test_gurobi_can_solve_a_tiny_instance():
    """Fail visibly if the solver or license cannot support this environment."""
    with gp.Env(empty=True) as environment:
        environment.setParam("OutputFlag", 0)
        environment.start()
        with gp.Model(env=environment) as model:
            quantity = model.addVar(lb=0, name="quantity")
            model.addConstr(quantity <= 2)
            model.setObjective(quantity, GRB.MAXIMIZE)
            model.optimize()
            assert model.Status == GRB.OPTIMAL
            assert model.ObjVal == pytest.approx(2)
            assert quantity.X == pytest.approx(2)
