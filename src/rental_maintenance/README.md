# Reusable Python code

Put reusable functions in this importable package. After installing the project,
scripts and notebooks can import them with `from rental_maintenance... import ...`.
Keep entry points thin and put business logic here so it can be tested and reused.

The planned domain modules are `data.py`, `model.py`, `baseline.py`, `verify.py`,
and `run.py`. Create each when its assigned task begins; none is implemented yet.

Use `common/` for small helpers with multiple real callers, such as shared file
handling. Keep model-specific logic in its domain module. Independent solution
verification must not reuse the model's constraint-building logic as its oracle.
Importing the package must not solve a model, write files, or contact a service.
