"""Check the public scaffold without reading credentials or contacting services."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ORIGINALS = {
    "Proposed_Final_Project_Balanced_Rental_Maintenance_Team_Plan.docx",
    "ProjectGuidelines_F2026_TwoTracks.pdf",
}
IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "dist",
    "build",
    ".idea",
    ".vscode",
}
REQUIRED = {
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "AI_USE.md",
    "SECURITY.md",
    "LICENSE",
    "pyproject.toml",
    "uv.lock",
    "requirements.txt",
    "requirements-dev.txt",
    ".python-version",
    ".github/workflows/ci.yml",
    ".github/workflows/release.yml",
    "docs/requirements.md",
    "docs/team-plan.md",
    "docs/ai-reviewer.md",
}
TEXT_SUFFIXES = {".py", ".md", ".toml", ".txt", ".yml", ".yaml", ".json", ".csv"}
TOKEN_PATTERN = re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")
LINK_PATTERN = re.compile(r"\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def path_problem(name: str) -> str | None:
    """Reject credentials, original course documents, and unsafe archive paths."""
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        return "unsafe repository path"
    if path.name in ORIGINALS:
        return "original source document must stay local"
    if path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example"):
        return "local environment file"
    if path.suffix.lower() in {".lic", ".pem", ".key"}:
        return "credential or license file"
    if path.parts and path.parts[0] in {"dist", ".venv", "venv"}:
        return "generated or environment directory"
    if path.parts and path.parts[0] == "outputs" and path.name != "README.md":
        return "generated analysis output"
    return None


def repository_files() -> list[Path]:
    if (ROOT / ".git").exists():
        result = subprocess.run(
            [
                "git",
                "-C",
                str(ROOT),
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "-z",
            ],
            check=True,
            capture_output=True,
        )
        return [ROOT / name.decode() for name in result.stdout.split(b"\0") if name]
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts)
        and not any(part.endswith(".egg-info") for part in path.relative_to(ROOT).parts)
    ]


def main() -> int:
    problems: list[str] = []
    files = repository_files()
    for name in sorted(REQUIRED):
        if not (ROOT / name).is_file():
            problems.append(f"{name}: required foundation file missing")
    for path in files:
        name = path.relative_to(ROOT).as_posix()
        problem = path_problem(name)
        if problem:
            problems.append(f"{name}: {problem}")
        if path.is_symlink():
            problems.append(f"{name}: symlinks are not accepted in this source package")
            continue
        if path.suffix not in TEXT_SUFFIXES or not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        if TOKEN_PATTERN.search(content):
            problems.append(f"{name}: possible GitHub credential; content suppressed")
        if path.suffix == ".md":
            for target in LINK_PATTERN.findall(content):
                if ":" in target or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                if target and not (path.parent / target).exists():
                    problems.append(f"{name}: missing relative link target {target}")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"Repository checks passed for {len(files)} files. This is not model verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
