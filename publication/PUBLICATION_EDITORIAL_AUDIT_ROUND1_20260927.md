# Publication Editorial Audit — Round 1 — 2026-09-27

## Scope

This audit reviews the manuscript as a journal article rather than as an internal proof ledger. The frozen mathematical claim is not reopened here. The objective is readability, external-reader logic, metadata completeness, literature framing, reproducibility presentation, and removal of internal project jargon from the main narrative.

## Source candidate

Original preserved source:
`manuscript/G459_ALL_SUBCRITICAL_R16_GATE9_CANDIDATE_20260926.tex`

Editorial working candidate:
`manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex`

Working branch:
`publication-editorial-revision-20260927`

## Completed in this round

- Preserved the original Gate-9 manuscript unchanged.
- Created a dedicated publication-editing branch.
- Added the formal editorial revision plan.
- Corrected author metadata to:
  - Cesar Grisa Segundo
  - Independent researcher, Brazil
  - cagrisa@id.uff.br
- Replaced author/funding/competing-interest placeholders.
- Added a concise single-author contribution statement.
- Removed the generic AI-use paragraph from the base publication candidate.
- Retitled the paper so that `gamma=459/1000` is presented explicitly as the exact project parameter rather than ambiguously as a conventional mass ratio.
- Rewrote the abstract in journal-facing language.
- Rebuilt the introduction around:
  1. classical Birkhoff/global-section motivation;
  2. contact/symplectic framework;
  3. validated-computation context;
  4. precise novelty and scope;
  5. proof architecture and article map.
- Added foundational references on:
  - PCR3BP contact geometry;
  - global surfaces of section;
  - the Frauenfelder–van Koert monograph.
- Added named Deep-Regime and Near-Critical propositions without changing the mathematical content.
- Made the proof assembly explicitly cite those two propositions.
- Replaced a first layer of internal terms such as “frozen R16” and “authoritative” with publication-facing language.

## Current candidate metrics

Approximate:
- ~3.8k words before references/TeX noise correction;
- abstract ~180 words;
- 9 sections;
- 12 subsections;
- 1 main theorem;
- 2 summary propositions;
- 1 lemma;
- 1 corollary;
- 8 bibliography items;
- 2 tables;
- 0 figures.

The manuscript is therefore materially clearer than the source candidate but still shorter and less visual than the strongest comparable celestial-mechanics/computer-assisted papers reviewed.

## Round-1 audit status

### PASS
- theorem statement remains fixed in scope;
- exact parameter convention is more visible;
- title no longer casually identifies gamma as the conventional mass ratio;
- author identity and independent-researcher status are explicit;
- funding/competing-interest placeholders removed;
- no self-citation added;
- original Gate-9 candidate preserved;
- proof split deep/near is now visible from the introduction;
- two intermediate regime propositions make the final theorem assembly easier to follow.

### OPEN
- bibliography is still too small for final publication;
- state-of-the-art discussion needs a second literature pass;
- internal node/package labels remain in the reproducibility table and should be separated into reader-facing versus archival forms;
- figures are still absent;
- first-hit geometry remains difficult to visualize without a schematic;
- Data availability and Code availability still contain future-tense DOI placeholders;
- final citation-number/theorem-number audit remains open;
- the manuscript has not yet undergone a clean-room external-reader read;
- no final PDF has yet been compiled/rendered from the new candidate;
- no v1.0.0 release should be created yet.

## Next round

1. Expand and verify the literature set with primary sources only.
2. Add three proof-explanatory figures or figure-ready schematics.
3. Rewrite the computer-assisted proof section to distinguish:
   - generator/search,
   - finite certificate,
   - independent checker,
   - exact coverage,
   - quick replay versus full replay.
4. Reduce internal package/node identifiers in the main prose.
5. Expand the near-critical narrative where external readers currently have to infer the logic.
6. Compile and visually inspect the publication candidate.
7. Run a clean-room referee-style audit.
8. Only then prepare CITATION.cff, license, SHA256SUMS, final release tree and Zenodo v1.0.0.

## Release rule

Do not publish GitHub Release v1.0.0 and do not freeze the Zenodo archival release until the final editorial audit, reproducibility audit and byte-freeze all pass.
