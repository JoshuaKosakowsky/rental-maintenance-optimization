"""Archive a clean committed source tree; this is not a final course submission."""

from __future__ import annotations

import argparse
import subprocess
import tempfile
import zipfile
from pathlib import Path

from check_repository import ROOT, path_problem


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (ROOT / ".git").exists():
        raise SystemExit("Run from the independent Git checkout, not an unpacked archive.")
    status = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain", "--untracked-files=normal"],
        check=True,
        capture_output=True,
        text=True,
    )
    if status.stdout:
        raise SystemExit(
            "Commit or remove pending source changes before creating a source archive."
        )
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing archive: {output}")
    with tempfile.TemporaryDirectory(prefix="rental-source-") as temp:
        archive = Path(temp) / "source.zip"
        subprocess.run(
            ["git", "-C", str(ROOT), "archive", "--format=zip", "--output", str(archive), "HEAD"],
            check=True,
        )
        with zipfile.ZipFile(archive) as zipped:
            for item in zipped.infolist():
                if problem := path_problem(item.filename):
                    raise SystemExit(f"Unsafe archive member {item.filename}: {problem}")
                if ((item.external_attr >> 16) & 0o170000) == 0o120000:
                    raise SystemExit(f"Symlink is not allowed in source archive: {item.filename}")
        output.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation avoids overwriting an existing file even in a race.
        with output.open("xb") as destination:
            destination.write(archive.read_bytes())
    print(f"Created source snapshot: {output}")
    print(
        "Final report, generated analysis results, and recording still require submission review."
    )


if __name__ == "__main__":
    main()
