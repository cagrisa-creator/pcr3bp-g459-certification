# v1.0.0 release checklist

This file is the release gate for the first archival GitHub/Zenodo release.
A checked item means the exact pre-release tree satisfies the stated
condition.

## Manuscript

- [x] Publication candidate source finalized.
- [x] Author metadata finalized.
- [x] Funding statement finalized.
- [x] Competing-interests statement finalized.
- [x] Single-author contribution statement finalized.
- [x] Generic AI-use paragraph absent from the base manuscript.
- [x] Internal project/campaign labels removed from the main narrative.
- [x] Three explanatory figures included.
- [x] Independent LaTeX build PASS.
- [x] Page-by-page visual QA PASS.
- [x] Static citation/reference audit PASS.
- [x] Data availability statement finalized without an unresolved DOI
      placeholder.
- [x] Code availability statement finalized with the public repository and
      archival-Zenodo wording.

## Repository metadata

- [x] Public repository.
- [x] Zenodo GitHub integration enabled by the author.
- [x] Repository licensing file added.
- [x] MIT terms applied to software source code and scripts.
- [x] Manuscript/scientific prose licensing kept separate.
- [x] CITATION.cff added.
- [x] CITATION.cff schema validation PASS in GitHub Actions.
- [x] REPRODUCE.md added.
- [x] README updated to archival pre-release wording.
- [x] Draft v1.0.0 release notes prepared.

## Reproducibility and byte freeze

- [x] Quick-audit evidence present.
- [x] Quick-audit manifest present.
- [x] Quick-audit expected PASS marker documented.
- [x] Complete blockwise clean-room replay obligations documented in
      REPRODUCE.md.
- [x] Publication PDF generated automatically from the audited TeX source.
- [x] Publication PDF committed to the release-candidate tree.
- [x] Root SHA256SUMS generated from the exact tracked release tree.
- [x] Quick audit rerun in a clean GitHub Actions checkout.
- [x] Fail-closed root release verifier PASS.
- [x] Release-tree hash verification PASS.
- [x] Automated freeze workflow commits generated PDF/hash changes back to
      the release-candidate branch.

The full numerical replay remains available as the reproducibility route
specified in REPRODUCE.md. The release-byte freeze does not restart historical
search campaigns or repeat long theorem-critical computations merely to
change repository metadata; it relies on the already frozen independent
evidence packages and rechecks their hashes, internal integrity, exact
parameter data, and theorem-core accounting.

## External archival action

- [ ] Author explicitly authorizes creation/publication of GitHub Release
      v1.0.0.
- [ ] Git tag v1.0.0 created from the audited release commit.
- [ ] GitHub Release published.
- [ ] Zenodo successfully archives the GitHub Release.
- [ ] Zenodo version DOI recorded for citation and future manuscript
      submission metadata.

## Gate status

Technical pre-release gate:

```text
PASS_PRE_RELEASE_TECHNICAL_GATE
```

External publication gate:

```text
WAITING_FOR_EXPLICIT_AUTHOR_AUTHORIZATION
```

Creating or publishing GitHub Release v1.0.0 is a separate external action
and is not authorized by this checklist.
