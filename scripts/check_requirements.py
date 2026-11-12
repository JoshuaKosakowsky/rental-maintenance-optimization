"""Ensure pip exports match the authoritative uv lock without modifying files."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    for name, extra in [("requirements.txt", ["--no-dev"]), ("requirements-dev.txt", [])]:
        result = subprocess.run(
            ["uv", "export", "--locked", "--no-emit-project", "--no-header", *extra],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        if result.stdout != (ROOT / name).read_text(encoding="utf-8"):
            raise SystemExit(
                f"{name} differs from uv.lock; regenerate using docs/reproducibility.md"
            )
        print(f"{name} matches uv.lock")


if __name__ == "__main__":
    main()
