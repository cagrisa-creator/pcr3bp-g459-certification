# Publication Editorial Revision Plan — 2026-09-27

Repository: `cagrisa-creator/pcr3bp-g459-certification`
Working branch: `publication-editorial-revision-20260927`
Scope: editorial/publication revision only. The frozen theorem mathematics is not reopened unless a concrete contradiction is found.

## Objective

Transform the current Gate-9 manuscript from a compressed internal-audit style into a journal-ready mathematical article with a clear external-reader narrative:

problem -> literature gap -> exact theorem -> two proof regimes -> intermediate propositions -> validated certificates -> dynamical convexity -> global surface of section -> reproducibility.

The target standard is comparable to strong Springer celestial-mechanics/dynamical-systems papers, while remaining venue-neutral until a journal is chosen.

## Non-regression rules

- Do not change theorem scope, exact parameter, thresholds, certified counts, inequalities or proof dependencies without a separate mathematical audit.
- Preserve the existing Gate-9 candidate as provenance.
- Make publication edits on a new manuscript candidate.
- No GitHub Release or Zenodo archival release until the editorial audit, metadata audit and reproducibility audit all pass.
- Do not add self-citations unless scientifically necessary.
- Keep the base manuscript free of a generic AI-use declaration. If a future venue requires a specific disclosure, handle that at submission time.
- Preserve complete auditability in the repository/supplement even when internal project labels are removed from the main prose.

## Author metadata to freeze in the new candidate

Author: Cesar Grisa Segundo
Affiliation: Independent researcher, Brazil
Email: cagrisa@id.uff.br
Funding: No funding was received for conducting this study.
Competing interests: The author declares no competing interests.
Author contributions: single-author statement covering conception, methodology, formal analysis, software, validation, investigation, data curation, writing, review/editing and project administration.

## Phase 1 — Narrative and metadata repair

1. Correct author name, affiliation and declarations.
2. Remove placeholders.
3. Remove the generic AI-assistance paragraph from the base manuscript.
4. Retitle the paper so that `gamma=459/1000` is not presented ambiguously as the conventional PCR3BP mass ratio.
5. Replace internal-language expressions such as “frozen R16”, “project-level”, “authoritative N5” and similar labels in the main text with publication-facing mathematical language.
6. Keep internal package names only in a compact reproducibility table or supplement when they are needed for traceability.

Gate P1: a reader unfamiliar with the project can identify the theorem, parameter convention, proof split and conclusion from title/abstract/introduction alone.

## Phase 2 — Introduction and state of the art

Expand the introduction into four visible functions:

1. classical Birkhoff/global-section motivation;
2. regularization/contact/dynamical-convexity framework;
3. strongest previous PCR3BP results and validated-numerics context;
4. the precise gap closed by this paper and what is not claimed.

Core references to audit/include include:
- Birkhoff;
- Hofer-Wysocki-Zehnder;
- Hryniewicz-Salomao;
- Albers-Frauenfelder-van Koert-Paternain on contact type;
- Albers-Fish-Frauenfelder-Hofer-van Koert on global surfaces of section;
- Frauenfelder-van Koert monograph;
- Joung-van Koert on validated symplectic/CZ computation;
- Liu-Salomao on finite-energy foliations and the near-equal-mass all-subcritical result.

Gate P2: every literature claim has a precise source and the novelty statement is neither broader nor weaker than the evidence supports.

## Phase 3 — Reorganize the proof as mathematics rather than campaign history

Target structure:

1. Introduction
2. PCR3BP, regularization and conventions
3. Main theorem and proof architecture
4. Deep subcritical regime
   - exact symplectic shear
   - tangent-Hessian reduction
   - finite convexity certificate
   - deep-regime proposition
5. Near-critical regime
   - rotation inequality
   - low-index occupation budget
   - short-period exclusion
   - finite return graph
   - long-orbit contradiction
   - exceptional block / first-hit argument
   - near-critical proposition
6. Proof of the main theorem
7. Computer-assisted proof architecture and reproducibility
8. Relation to previous work, scope and limitations
9. Statements and declarations
10. References

Gate P3: the main theorem follows from named intermediate statements without requiring the reader to know internal node names N0-N5/C0-C4.

## Phase 4 — Figures and explanatory geometry

Target 3 original explanatory figures:

Figure 1. Energy-regime map:
`0 < Delta < 3/50000` versus `Delta >= 3/50000`, with the two bounded components and the role of the first critical level.

Figure 2. Proof architecture:
deep branch -> exact shear -> strict convexity -> dynamical convexity;
near branch -> rotation/return/first-hit -> CZ >= 3 -> dynamical convexity;
then rational open book/global section.

Figure 3. Exceptional first-hit block:
schematic of the bad block B, allowed upper-theta and upper-A entries, excluded phi entries and monotonic directions.

No decorative figures. Every figure must carry proof-explanatory value and have a self-contained caption.

Gate P4: each figure removes a real conceptual burden from the text.

## Phase 5 — Bibliography and citations

Expand the bibliography from the current minimal set to a focused research bibliography, expected roughly in the 20-30 reference range if justified by the literature audit.

Rules:
- no padding;
- no self-citations unless necessary;
- prefer primary sources;
- normalize DOI presentation;
- verify theorem numbers and version-sensitive claims before freezing.

Gate P5: every historical/theoretical bridge in the introduction and final theorem can be traced to an appropriate primary source.

## Phase 6 — Reproducibility presentation

The article should explain:
- what is symbolic/exact;
- what is interval/validated;
- what the finite proof objects are;
- what the independent checker/replay verifies;
- how coverage is established;
- what the reader can reproduce quickly versus fully.

Move project-governance terminology, exhaustive node genealogy and long package identifiers out of the narrative when they are not mathematically necessary.

Gate P6: a specialist can understand why the computer-assisted part is a proof, not merely a computation.

## Phase 7 — Final editorial audit

Run a clean-room read as an external referee:
- theorem scope;
- notation consistency;
- parameter convention;
- logical continuity;
- unexplained acronyms/internal labels;
- missing definitions;
- figures/captions;
- references;
- declarations;
- data/code availability;
- grammar/style;
- absence of placeholders;
- absence of unsupported self-citation.

Only after P1-P7 pass:
1. merge publication candidate to main;
2. freeze final bytes;
3. generate SHA256SUMS;
4. finalize CITATION.cff and license;
5. create GitHub Release v1.0.0;
6. allow Zenodo to archive that release;
7. insert final DOI into the archival manuscript or create a DOI-bearing follow-up release only according to the chosen release policy.

## Current round

Execute Phase 1 and begin Phases 2-3:
- create a new publication manuscript candidate;
- fix metadata/declarations;
- remove internal project language from the main narrative;
- rewrite title, abstract and introduction;
- add publication-facing intermediate proposition structure without changing the proof;
- add the verified historical references needed for the introduction;
- leave the original Gate-9 candidate untouched.
