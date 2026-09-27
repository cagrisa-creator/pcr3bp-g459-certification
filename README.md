# PCR3BP certification at gamma = 459/1000

This repository contains the computer-assisted proof package for an
all-subcritical Birkhoff global-section theorem at the exact parameter
`gamma = 459/1000` in the planar circular restricted three-body problem.

The proof combines two complementary mechanisms:

- a deep subcritical branch based on an exact symplectic momentum shear,
  strict convexity, and validated interval certification;
- a near-critical branch based on validated rotation estimates,
  short-period exclusion, finite return geometry, and a first-hit
  compensation argument.

The theorem-critical numerical claims are represented by finite proof
objects and checked independently.

## Current status

The mathematical theorem and publication-facing manuscript audit are closed
at project level. The current manuscript candidate has passed:

- source-level clean-room editorial audit;
- independent LaTeX compilation;
- citation/cross-reference consistency checks;
- page-by-page visual QA.

The repository is now in **pre-release freeze preparation** for the first
archival version `v1.0.0`.

No GitHub Release has been published yet. The first release will be created
only after the exact release tree, hashes, reproducibility records, and
metadata are frozen.

## Manuscript

Current publication source:

```text
manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex
```

Title:

> A computer-assisted all-subcritical Birkhoff global-section theorem at
> gamma = 459/1000 for the planar circular restricted three-body problem

Author:

**Cesar Grisa Segundo**  
Independent researcher, Brazil  
cagrisa@id.uff.br

The earlier Gate-9 manuscript is retained for provenance and is not the
publication-facing source.

## Repository structure

- `manuscript/` — publication manuscript source and preserved earlier candidate;
- `quick_audit/` — compact fail-closed integrity/accounting audit and evidence;
- `release_candidate/` — preserved pre-publication manifests;
- `publication/` — editorial, clean-room, and visual-QA audit records;
- `REPRODUCE.md` — clean-room reproduction specification;
- `RELEASE_CHECKLIST.md` — v1.0.0 release gate;
- `CITATION.cff` — citation metadata;
- `LICENSE` — repository licensing and MIT terms for software code/scripts.

## Quick audit

From the repository root:

```bash
python3 quick_audit/scripts/QUICK_AUDIT.py
```

Expected final output:

```text
PASS_QUICK_AUDIT_R16
packages=9 exact_parameter=PASS theorem_core=PASS
```

The quick audit checks integrity and theorem-core accounting. It does not
replace the complete numerical replay.

For the complete replay obligations and expected outputs, see
`REPRODUCE.md`.

## Building the manuscript

With a standard TeX Live installation:

```bash
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode \
  manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex
```

The repository also contains a GitHub Actions PDF-QA workflow.

## Licensing

Software source code and executable scripts are available under the MIT
terms included in `LICENSE`.

The manuscript, article text, article figures, captions, and scientific
prose are not licensed under MIT by default; their copyright status is
stated separately in `LICENSE`.

## Citation

Citation metadata are provided in `CITATION.cff`.

The archival DOI will be added after the first GitHub Release is archived by
Zenodo.

## Release policy

Public repository visibility does not itself constitute the archival
release.

The first archival release will be tagged `v1.0.0` only after:

1. the audited publication PDF is committed;
2. the exact release-tree SHA-256 manifest is generated;
3. the quick audit is rerun against the final bytes;
4. the final release-tree audit passes;
5. the author explicitly authorizes publication of the GitHub Release.

See `RELEASE_CHECKLIST.md` for the current gate.
