# Publication Editorial Audit — Round 2 — 2026-09-27

## Scope

This round continues the journal-facing revision without reopening the frozen mathematical theorem. It focuses on explanatory figures, near-critical readability, reproducibility exposition, literature depth, and removal of internal campaign language from the main manuscript.

## Candidate

`manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex`

Branch:
`publication-editorial-revision-20260927`

## Completed in this round

### 1. Three proof-explanatory figures added

Figure 1 — exact energy split:
- first critical face at `Delta=0`;
- near-critical regime `0 < Delta < 3/50000`;
- deep regime `Delta >= 3/50000`;
- explicitly states that the theorem concerns the complete subcritical ray.

Figure 2 — logical proof architecture:
- deep branch: exact shear -> tangent-Hessian reduction -> validated strict convexity;
- near branch: rotation inequality -> short-period exclusion -> return graph -> first-hit compensation;
- both branches -> dynamical convexity -> rational open book/global surface of section.

Figure 3 — exceptional first-hit geometry:
- block B;
- upper-theta and upper-A admissible entry families;
- outward phi faces;
- monotone forward flow;
- caption explicitly states that the schematic is not a coordinate projection and is not to scale.

The figures are original TikZ schematics generated from the proof architecture, not borrowed illustrations.

### 2. Near-critical narrative strengthened

The near-critical section now begins with the actual contradiction logic before exposing certificate counts:

low CZ -> upper rotation budget -> validated lower rotation estimate -> occupation budget -> short-period exclusion -> long orbit -> repeated return obligations -> contradiction.

The exceptional block is introduced as a genuine failure of the baseline pointwise bound rather than as an internal project label.

### 3. Internal campaign vocabulary removed

Current main manuscript counts:
- `R16`: 0
- `N0...N5`: 0
- `C0...C4`: 0
- `authoritative`: 0
- `seed-7`: 0

Internal genealogy remains available in the archival project, but is no longer required vocabulary for reading the article.

### 4. Reproducibility section rewritten

The main computational section now explains four publication-facing layers:

1. exact symbolic reduction;
2. finite proof-object generation;
3. independent coverage/completeness checking;
4. independent exact/validated replay with directed rounding.

The text explicitly distinguishes exploratory search from theorem acceptance and explains why replacement of the search heuristic would not change the proof if the same finite obligations are independently accepted.

The old node/package table has been replaced by:
- proof component;
- finite mathematical evidence;
- independent acceptance.

### 5. Literature expanded

The bibliography now contains 14 focused references, including:
- Birkhoff;
- Moser regularization;
- Robbin–Salamon;
- Hofer–Wysocki–Zehnder strict convexity;
- Hofer–Wysocki–Zehnder finite-energy foliations;
- Hryniewicz–Salomao;
- Albers et al. contact geometry;
- Albers et al. global surfaces of section;
- rotating Kepler CZ indices;
- Frauenfelder–van Koert monograph;
- Joung–van Koert;
- Liu–Salomao;
- Moore interval analysis;
- MPFR.

Malformed DOI links introduced in the previous editing pass were corrected.

## Current manuscript metrics

Approximate:
- 4.8k words including figure captions and TeX-visible text;
- abstract: ~181 words;
- 9 sections;
- 12 subsections;
- 3 figures;
- 2 tables;
- 14 bibliography entries;
- 1 theorem;
- 2 propositions;
- 1 lemma;
- 1 corollary.

## Audit status

### PASS
- title identifies gamma explicitly;
- author metadata fixed;
- funding and competing-interest text fixed;
- no generic AI-use paragraph in the manuscript base;
- no internal R16/N/C campaign labels in the main narrative;
- deep/near proof architecture readable without project history;
- three original explanatory figures now present in source;
- computer-assisted proof architecture has a publication-facing explanation;
- original Gate-9 source remains preserved;
- no GitHub Release created.

### OPEN
- final compilation and visual inspection of the new candidate;
- final primary-source verification of every bibliographic datum and theorem-number-sensitive statement;
- literature may still need selective expansion; 14 references is improved but not necessarily final;
- the Hamiltonian/regularization section is still very compressed compared with the depth of the theorem;
- the exact gamma-to-mass-label convention deserves one additional explanatory paragraph for readers accustomed to conventional mu <= 1/2;
- data/code availability still contains DOI placeholders intentionally, because no archival release has yet been created;
- clean-room referee read remains open;
- figures have source-level sanity checks but not yet page-level visual QA.

## Next actions

1. Expand the parameter/regularization explanation just enough to make the paper self-contained.
2. Verify theorem-number-sensitive references and all DOI/volume/page metadata against primary sources.
3. Compile and visually inspect the new manuscript.
4. Perform a clean-room referee-style audit of the compiled PDF.
5. Freeze manuscript only after these pass.
6. Then prepare LICENSE, CITATION.cff, SHA256SUMS, final reproduction instructions, GitHub v1.0.0 release, and Zenodo archive.

## Release decision

`v1.0.0` remains BLOCKED pending final PDF compilation/visual QA and clean-room publication audit.
