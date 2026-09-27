#!/usr/bin/env python3
"""Fail-closed verifier for the planned v1.0.0 release tree."""

from __future__ import annotations

import hashlib
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SUMS = ROOT / "SHA256SUMS"
QUICK = ROOT / "quick_audit" / "scripts" / "QUICK_AUDIT.py"


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_sums() -> None:
    if not SUMS.is_file():
        raise SystemExit("FAIL: missing SHA256SUMS")

    seen: set[str] = set()
    for raw in SUMS.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        try:
            expected, rel = line.split(None, 1)
        except ValueError as exc:
            raise SystemExit(f"FAIL: malformed SHA256SUMS line: {raw!r}") from exc
        rel = rel.lstrip("*")
        if rel in seen:
            raise SystemExit(f"FAIL: duplicate SHA256SUMS path: {rel}")
        seen.add(rel)
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"FAIL: missing release file: {rel}")
        got = sha256(path)
        if got != expected:
            raise SystemExit(
                f"FAIL: SHA256 mismatch for {rel}\n"
                f" expected {expected}\n got      {got}"
            )

    if not seen:
        raise SystemExit("FAIL: SHA256SUMS contains no entries")


def run_quick_audit() -> None:
    if not QUICK.is_file():
        raise SystemExit("FAIL: missing quick-audit script")
    proc = subprocess.run(
        [sys.executable, str(QUICK)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    if proc.returncode != 0:
        raise SystemExit(f"FAIL: quick audit returned {proc.returncode}")
    if "PASS_QUICK_AUDIT_R16" not in proc.stdout:
        raise SystemExit("FAIL: quick-audit PASS marker not found")


def main() -> None:
    verify_sums()
    run_quick_audit()
    print("PASS_RELEASE_VERIFY_V1_0_0")


if __name__ == "__main__":
    main()
