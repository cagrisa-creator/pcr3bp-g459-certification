# v1.0.0 release checklist

This file is the release gate for the first archival GitHub/Zenodo release.
A checked item means the exact release bytes satisfy the stated condition.

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
- [ ] Final archival DOI inserted into Data availability / Code availability
      when the DOI exists.

## Repository metadata

- [x] Public repository.
- [x] Zenodo GitHub integration enabled by the author.
- [x] Repository licensing file added.
- [x] MIT terms applied to software source code and scripts.
- [x] Manuscript/scientific prose licensing kept separate.
- [x] CITATION.cff added.
- [x] REPRODUCE.md added.
- [ ] Final README updated to archival-release wording.
- [ ] Final release notes frozen.

## Reproducibility

- [x] Quick-audit evidence present.
- [x] Quick-audit manifest present.
- [x] Quick-audit expected PASS marker documented.
- [x] Full clean-room replay obligations documented in REPRODUCE.md.
- [ ] Final publication PDF committed from the audited source.
- [ ] Root release SHA256SUMS generated for the exact release tree.
- [ ] Quick audit rerun against the exact final release bytes.
- [ ] Final release-tree audit records no missing/extra critical files.
- [ ] Final clean extraction/replay record frozen.

## External archival action

- [ ] Author explicitly authorizes creation of GitHub Release v1.0.0.
- [ ] Git tag v1.0.0 created from the audited release commit.
- [ ] GitHub Release published.
- [ ] Zenodo successfully archives the GitHub Release.
- [ ] Zenodo version DOI recorded.
- [ ] Data availability / Code availability updated with the archival DOI
      according to the chosen release procedure.

## Release gate

Current status:

```text
NOT_READY_FOR_V1.0.0
```

The release may be promoted to `READY_FOR_V1.0.0` only when all
pre-publication items above are closed. Publishing the GitHub Release remains
a separate author-authorized action.
