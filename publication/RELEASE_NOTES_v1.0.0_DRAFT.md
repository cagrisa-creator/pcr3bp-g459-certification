# Draft release notes for v1.0.0

This is a pre-publication draft. It does not create or publish a GitHub Release.

This planned archival version freezes the computer-assisted proof package for
the all-subcritical Birkhoff global-section theorem at the exact parameter
gamma = 459/1000 in the planar circular restricted three-body problem.

The proof uses two complementary regimes:

- Deep subcritical regime: exact symplectic shear, strict convexity,
  validated interval certification, and independent MPFR replay.
- Near-critical regime: validated rotation estimates, short-period
  exclusion, finite return geometry, long-orbit counting, and first-hit
  compensation.

Included components are planned to comprise the publication-facing
manuscript source and audited PDF, theorem-critical evidence packages,
quick-audit wrapper, manifests and hashes, clean-room reproduction
specification, publication QA records, citation metadata, and licensing.

Quick audit:

```bash
python3 quick_audit/scripts/QUICK_AUDIT.py
```

Expected:

```text
PASS_QUICK_AUDIT_R16
packages=9 exact_parameter=PASS theorem_core=PASS
```

Author: Cesar Grisa Segundo
Affiliation: Independent researcher, Brazil
Email: cagrisa@id.uff.br

The archival DOI will be inserted only after an explicitly authorized
GitHub Release is archived by Zenodo.
