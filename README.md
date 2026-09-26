# PCR3BP G459 certification — private staging repository

This repository is a **private pre-publication staging area** for the R16 all-subcritical G459 computer-assisted proof package.

## Current status

- Mathematical project status: closed at project level for the frozen R16 theorem target.
- This repository is **not yet the final public release**.
- The manuscript and quick-audit bundle here are release candidates.
- The final portable full-reproduction launcher/tree, final author metadata, license, citation metadata, DOI/repository identifiers, and final byte-freeze are still to be completed before any public release.

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

## Important

Do not treat this staging repository as the archival release. Public release should occur only after the final reproducibility tree and final metadata are frozen and audited.
