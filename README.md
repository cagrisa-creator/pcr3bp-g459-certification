# PCR3BP G459 certification

This repository contains the R16 all-subcritical G459 computer-assisted proof package for the planar circular restricted three-body problem.

## Current status

- Mathematical project status: closed at project level for the frozen R16 theorem target.
- The manuscript and quick-audit bundle are release candidates.
- The repository is being prepared for public archival release and Zenodo deposit.
- The final portable full-reproduction launcher/tree, final license, citation metadata, DOI/repository identifiers, and final byte-freeze are still to be completed before the archival release is declared final.

## Contents

- `manuscript/` — current Gate-9 manuscript candidate (`.tex` and `.pdf`).
- `quick_audit/` — portable quick-audit script, manifests, hashes, and frozen evidence packages.
- `release_candidate/` — current candidate manifest and quick-audit revalidation record.

## Quick audit

From the repository root:

```bash
python3 quick_audit/scripts/QUICK_AUDIT.py
```

The expected success marker is:

```text
PASS_QUICK_AUDIT_R16
```

## Release note

Public visibility does not by itself declare this repository to be the final archival release. The final release will be frozen only after the remaining reproducibility and metadata tasks are completed and audited.
