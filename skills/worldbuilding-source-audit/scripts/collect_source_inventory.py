#!/usr/bin/env python3
"""Collect a read-only inventory for explicitly supplied source paths."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Emit a JSON inventory for explicit files or directories. "
            "The output records bytes, not source authority or meaning."
        )
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to inspect")
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recurse into supplied directories; directory symlinks are not followed",
    )
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_directory(path: Path, recursive: bool) -> Iterable[Path]:
    iterator = path.rglob("*") if recursive else path.iterdir()
    for candidate in sorted(iterator, key=lambda item: str(item).casefold()):
        if candidate.is_file() or candidate.is_symlink():
            yield candidate


def inspect_file(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.absolute()),
        "size_bytes": stat.st_size,
        "modified_utc": datetime.fromtimestamp(
            stat.st_mtime, tz=timezone.utc
        ).isoformat(),
        "sha256": sha256_file(path),
    }


def main() -> int:
    args = parse_args()
    files: list[dict[str, Any]] = []
    warnings: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    seen: set[str] = set()

    for raw_path in args.paths:
        supplied = Path(raw_path).expanduser()
        absolute = supplied.absolute()

        if not supplied.exists() and not supplied.is_symlink():
            errors.append({"path": str(absolute), "error": "path does not exist"})
            continue

        if supplied.is_symlink():
            warnings.append(
                {"path": str(absolute), "warning": "symbolic link was not followed"}
            )
            continue

        try:
            candidates = (
                list(iter_directory(supplied, args.recursive))
                if supplied.is_dir()
                else [supplied]
            )
        except OSError as exc:
            errors.append({"path": str(absolute), "error": str(exc)})
            continue

        for candidate in candidates:
            candidate_absolute = candidate.absolute()
            key = os.path.normcase(str(candidate_absolute))
            if key in seen:
                continue
            seen.add(key)

            if candidate.is_symlink():
                warnings.append(
                    {
                        "path": str(candidate_absolute),
                        "warning": "symbolic link was not followed",
                    }
                )
                continue

            try:
                files.append(inspect_file(candidate))
            except (OSError, ValueError) as exc:
                errors.append({"path": str(candidate_absolute), "error": str(exc)})

    result = {
        "schema_version": 1,
        "recursive": args.recursive,
        "files": files,
        "warnings": warnings,
        "errors": errors,
        "authority_inferred": False,
    }
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
