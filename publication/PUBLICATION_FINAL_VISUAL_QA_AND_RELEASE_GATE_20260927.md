# Publication Final Visual QA and Release Gate — 2026-09-27

## Candidate under review

Repository: `cagrisa-creator/pcr3bp-g459-certification`

Branch: `publication-editorial-revision-20260927`

Manuscript source:
`manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex`

Publication-candidate source blob SHA:
`4807ba5e8d76a8d0cc4ccea247822d3aefe32525`

Final typography-polish commit:
`19d583872b6de3c5cd65d081cf0ea4a201e03805`

The original Gate-9 manuscript remains preserved and was not overwritten.

## Independent build record

GitHub Actions workflow:
`.github/workflows/build-publication-pdf.yml`

Final QA workflow run:
`36325897864`

Run result:
`SUCCESS`

Artifact:
`publication-pdf-qa`

Artifact ID:
`10933443599`

Artifact digest:
`sha256:071648ec5180e56de485f709e03bd380689e1cfbdea400f67d6e1ebc3c6ef49a`

Compiled PDF:
`G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.pdf`

Compiled PDF properties:
- pages: 13;
- page size: A4;
- file size: 418482 bytes;
- PDF version: 1.7;
- PDF SHA-256: `93ca9687c1bd6be5675e9b56220d857861b8f0e78541e845d4b1ce2eed17b489`.

## LaTeX QA

The final build completed successfully with `-halt-on-error`.

The collected `LATEX_WARNINGS.txt` is empty.

Final targeted checks:
- overfull boxes: none collected;
- underfull boxes: none collected;
- hyperref warnings: none collected;
- undefined references: none collected;
- multiply-defined labels: none collected.

The earlier QA pass had identified:
1. a small overfull table cell;
2. PDF-string warnings caused by mathematics in a subsection title;
3. an underfull table caption;
4. automatic hyphenation inside proof figures;
5. an overlapping annotation in the exceptional-block figure.

All five were corrected before the final build.

## Page-by-page visual inspection

All 13 pages were rendered at 180 dpi and inspected after the final successful build.

### Page 1 — PASS
- title readable and balanced;
- author, affiliation and email correctly placed;
- abstract visually clear;
- keywords readable;
- introduction begins without crowding.

### Page 2 — PASS
- literature narrative flows cleanly;
- main proof split is readable;
- displayed parameter/energy formulas fit normally;
- no clipping or anomalous spacing.

### Page 3 — PASS
- exact parameter formulas are legible;
- rational values fit on the page;
- convention table remains inside the text block;
- no overflow.

### Page 4 — PASS
- Theorem 1.1 is readable;
- Figure 1 no longer has overlapping regime labels;
- near/deep split is visually clear;
- Hamiltonian section begins cleanly below the figure.

### Page 5 — PASS
- Figure 2 has no broken-word hyphenation in the principal proof boxes;
- arrows and convergence into dynamical convexity are clear;
- the rational-open-book endpoint is legible;
- exact-parameter subsection is not crowded.

### Page 6 — PASS
- regularization conventions and deep-regime formulas are balanced;
- tangent-Hessian formula and certificate counts fit cleanly.

### Page 7 — PASS
- deep-regime proposition and near-critical opening are clear;
- occupation-time equations are centered and readable.

### Page 8 — PASS
- short-period and long-return arguments remain readable despite dense technical content;
- no overflow or clipped mathematics.

### Page 9 — PASS
- Figure 3 exceptional first-hit block is clean;
- the previous overlapping annotation was removed;
- entry arrows, outward phi faces and block inequalities are legible;
- caption correctly says the schematic is not to scale.

### Page 10 — PASS
- first-hit lemma/corollary/proposition are visually separated;
- final theorem assembly begins with sufficient space;
- no awkward float interaction.

### Page 11 — PASS
- computer-assisted proof architecture is readable;
- traceability longtable fits completely inside the page;
- columns remain legible;
- no caption overflow.

### Page 12 — PASS
- scope and reproducibility sections are readable;
- statements/declarations are well separated;
- the two persistent-identifier placeholders are visible and intentional;
- bibliography begins normally.

### Page 13 — PASS
- bibliography is fully contained on the page;
- DOI/URL wrapping is acceptable;
- erratum entry is readable;
- no clipping or orphaned final line.

## Static source consistency retained

The final source audit still has:
- 3 figures;
- 15 bibliography entries;
- no undefined citation keys;
- no undefined cross-references;
- no duplicate labels;
- no generic AI-use declaration in the base manuscript;
- no internal campaign vocabulary such as R16/N0-N5/C0-C4/G459/VAST in the main narrative;
- exactly two intentional placeholders, both for persistent archive identifiers to be inserted after deposit.

## Final manuscript audit status

Mathematical theorem:
`NOT_REOPENED — NO CONTRADICTION FOUND`

Source-level publication audit:
`PASS`

Independent compilation:
`PASS`

LaTeX warning audit:
`PASS — ZERO COLLECTED WARNINGS`

Page-by-page visual QA:
`PASS`

Reader-facing structure/humanization:
`PASS_MANUSCRIPT_CANDIDATE`

Overall manuscript gate:
`PASS_VISUAL_QA_MANUSCRIPT_CANDIDATE`

## Remaining blockers before v1.0.0

The manuscript itself has passed the current publication-facing QA. The remaining blockers are release/reproducibility tasks rather than manuscript-layout tasks:

1. choose/finalize repository code license;
2. create and validate `CITATION.cff`;
3. finalize portable full-reproduction instructions/tree;
4. freeze final release bytes;
5. generate final `SHA256SUMS`;
6. rerun the quick audit against those exact final bytes;
7. create GitHub Release `v1.0.0` only after explicit author authorization;
8. allow Zenodo to archive that release and generate the persistent DOI;
9. insert the final persistent identifier into Data availability / Code availability according to the chosen archival-release procedure.

## Release decision

GitHub/Zenodo release remains:
`BLOCKED_PENDING_REPRODUCIBILITY_FREEZE_AND_AUTHOR_AUTHORIZATION`

This QA report is not authorization to publish or create a release.
