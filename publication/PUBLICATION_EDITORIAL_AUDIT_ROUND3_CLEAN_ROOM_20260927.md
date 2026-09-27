# Publication Editorial Audit — Round 3 / Clean-Room Source Audit — 2026-09-27

## Scope

This audit reviews the current publication candidate as if read by an external referee with no knowledge of the project history. It checks self-containment, parameter conventions, theorem-facing literature bridges, internal consistency of the LaTeX source, references/cross-references, publication metadata, and separation between proof logic and computational provenance.

The frozen mathematical theorem is not reopened in this editorial round unless a concrete contradiction is found.

Candidate:
`manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex`

Working branch:
`publication-editorial-revision-20260927`

## Changes completed before this audit

### A. Exact parameter map made self-contained

The manuscript now defines
[
D(gamma)=1-2gamma+gamma^2+2gamma^3-gamma^4,
]
[
m_s(gamma)=rac{gamma^3(gamma^2-3gamma+3)}{D(gamma)},
]
and records the exact smaller-mass representative at (gamma=459/1000):
[
m_s=rac{177321681763299}{441699674239000}=0.4014530508060817ldots .
]

The complementary internal label is
[
mu_*=1-m_s=rac{264377992475701}{441699674239000}=0.5985469491939183ldots .
]

The manuscript explicitly explains that (mu_*>1/2) is only a primary-label convention and that the standard representative after primary exchange is (m_sle1/2).

It also records
[
x_{L_1}=1-m_s(gamma)-gamma
]
and
[
c_{L_1}(gamma)=rac{x_{L_1}^2}{2}
+rac{1-m_s(gamma)}{1-gamma}
+rac{m_s(gamma)}{gamma},
]
which yields the exact rational first critical value used by the proof.

These formulas were cross-checked against the preserved earlier manuscript/material in the project library.

### B. Hamiltonian and regularization conventions expanded

The article now gives the rotating-frame Hamiltonian explicitly and explains:
- primary exchange (muleftrightarrow1-mu);
- the Jacobi convention (Sigma_c=H^{-1}(-c));
- why (Delta=c-c_{L_1}>0) is the subcritical side;
- the (S^3) regularization double cover and (mathbb{R}P^3) quotient;
- positive Levi--Civita time changes;
- transported contact-plane frame/trivialization;
- why no equal-clock shortcut is used.

### C. Residual project language removed

The main manuscript currently contains zero occurrences of:
- R16;
- N0--N5;
- C0--C4;
- G459 as an internal theorem label;
- VAST;
- authoritative;
- seed-7;
- expected-PASS.

The theorem is now named by its mathematical parameter, not by the internal project codename.

### D. Sensitive external theorem references rechecked

The literature bridge was re-audited against current source text.

1. Liu--Salomão, arXiv:2506.17867v2:
   - Theorem 9.1 is indeed the tangent-Hessian criterion for the magnetic-mechanical Hamiltonian form used in the manuscript.
   - Theorem 1.16 is indeed the all-subcritical Birkhoff/dynamical-convexity statement for mass ratios sufficiently close to (1/2).
   - Theorem 1.5 supplies the retrograde-orbit family and the surrounding text records the 2-unknot/self-linking (-1/2) topology used in the final binding step.

2. Hryniewicz--Salomão:
   - Corollary 1.8 of arXiv:1505.02713v3 gives the rational-open-book/global-section implication for a (p)-unknotted orbit of self-linking (-1/p) in a dynamically convex lens-space Reeb flow.
   - The authors later issued an erratum correcting a broader lens-space statement in the introduction.
   - The erratum explicitly states that the (L(2,1)=mathbb{R}P^3) case used here remains valid and that the results of the paper are unaffected.
   - The manuscript now cites this correction explicitly rather than silently relying on the original paper.

### E. Bibliographic metadata corrections

The Hryniewicz--Salomão publication is now recorded as volume 55, issue 2, Article 43.

The Albers--Frauenfelder--van Koert--Paternain contact-geometry article now includes pages 229--263.

The DOI syntax is normalized and no malformed `https://doi.org/10}...` entries remain.

## Static LaTeX audit

Current source-level checks:

- bibliography entries: 15;
- citation occurrences: 22;
- figures: 3;
- tables/longtables: 2;
- undefined citation keys: 0;
- bibliography entries never cited: 0;
- undefined cross-references: 0;
- duplicate labels: 0;
- duplicate bibliography keys: 0.

Balanced environments:
- abstract: PASS;
- figure: 3/3 PASS;
- table: 1/1 PASS;
- longtable: 1/1 PASS;
- theorem: 1/1 PASS;
- proposition: 2/2 PASS;
- lemma: 1/1 PASS;
- corollary: 1/1 PASS;
- proof: 1/1 PASS;
- align*: 1/1 PASS;
- tikzpicture: 3/3 PASS.

Publication metadata:
- author = Cesar Grisa Segundo: PASS;
- affiliation = Independent researcher, Brazil: PASS;
- no-funding declaration: PASS;
- no-competing-interest declaration: PASS;
- author-contribution statement: PASS;
- generic AI-use paragraph in base manuscript: absent;
- self-citations by the author: none.

## Clean-room referee reading

### 1. Title and abstract — PASS

The title states the exact parameter and the all-subcritical scope without presenting (gamma) as the conventional mass ratio.

The abstract now identifies:
- the theorem;
- the complete energy scope;
- the deep/near split;
- the deep convexification mechanism;
- the near-critical rotation/return mechanism;
- the Conley--Zehnder conclusion;
- the rational-open-book/global-section endpoint;
- independent finite certification.

It no longer reads like a project log.

### 2. Introduction — PASS WITH MINOR FUTURE POLISH

The introduction now follows a standard research-paper sequence:

classical problem -> contact/symplectic framework -> prior work -> exact gap -> contribution -> proof architecture -> paper roadmap.

This is publication-facing and understandable without internal project history.

No novelty claim currently says that the fixed parameter lies outside the existential Liu--Salomão neighborhood.

### 3. Parameter conventions — PASS

This was previously a likely referee objection because the internal label (mu_*>1/2) could be mistaken for a violation of the conventional PCR3BP mass convention.

That ambiguity is now explicitly resolved by the exact (gammamapsto m_s(gamma)) formula and primary exchange.

### 4. Deep-regime exposition — PASS

The chain
exact shear -> magnetic-mechanical form -> tangent-Hessian criterion -> exact fiber elimination -> finite positivity certificate -> monotone energy propagation -> strict/dynamical convexity
is visible and reader-facing.

### 5. Near-critical exposition — PASS AT ARCHITECTURE LEVEL

The reader can now see the contradiction chain before seeing raw certificate counts:

low index -> rotation budget -> short-period exclusion -> finite return graph -> long-orbit counting contradiction -> exceptional first-hit compensation.

This is a major improvement over the original campaign-style presentation.

The section is still concise relative to the depth of the computer-assisted proof, but its logical sequence is now intelligible.

### 6. Exceptional block — PASS

The article explicitly admits that the baseline pointwise bound fails on two cells and does not relabel them as pointwise PASS cases.

The first-hit compensation mechanism is explained mathematically and accompanied by a schematic figure.

### 7. Final topological bridge — PASS AFTER ERRATUM HARDENING

The retrograde topology is tied to Liu--Salomão.

The (p=2) rational-open-book implication is tied to Hryniewicz--Salomão.

The later correction to the lens-space paper is now acknowledged, and the special (L(2,1)=mathbb{R}P^3) case used in this manuscript is explicitly noted as unaffected.

### 8. Computer-assisted proof explanation — PASS

The article now distinguishes:
1. exact symbolic reduction;
2. search/generation;
3. finite proof objects and exact coverage;
4. independent directed-rounding replay/checkers.

This is the correct conceptual distinction for convincing a referee that the proof is not a numerical experiment.

### 9. Figures — SOURCE-LEVEL PASS / VISUAL QA STILL REQUIRED

Three original TikZ figures are present:
1. exact energy split;
2. proof architecture;
3. exceptional first-hit geometry.

All figure environments and labels are balanced and referenced.

Their mathematical role is appropriate and they are not decorative.

However, final page-level visual inspection of the compiled PDF remains required before release.

### 10. Bibliography — PASS FOR CORE LOGICAL CHAIN, NOT NECESSARILY FINAL

The bibliography now contains the core primary sources needed for:
- Birkhoff;
- regularization;
- contact type/global sections;
- strict/dynamical convexity;
- rational open books;
- Maslov/Robbin--Salamon conventions;
- finite-energy foliations;
- rotating Kepler indices;
- validated symplectic computations;
- current Liu--Salomão result;
- interval arithmetic and MPFR.

Fifteen references is now defensible for this focused theorem. Further references should be added only when they support an actual statement, not to imitate a target citation count.

## Remaining release blockers

### BLOCKER 1 — compiled PDF / visual QA
The revised candidate still needs a full compilation and page-by-page rendering check:
- figure sizing;
- float placement;
- table overflow;
- overfull boxes;
- bibliography wrapping;
- cross-reference resolution;
- glyph/accent rendering;
- page density.

This cannot be marked PASS from source inspection alone.

### BLOCKER 2 — archival identifiers
Two intentional placeholders remain:
- Data availability persistent identifier;
- Code availability persistent identifier.

These are not manuscript defects at the current pre-release stage. They must be filled only after the archival release/Zenodo record exists.

### BLOCKER 3 — final reproducibility freeze
Before v1.0.0:
- final portable reproduce instructions;
- license choice;
- CITATION.cff;
- final SHA256SUMS;
- release-tree audit;
- exact byte freeze;
- rerun of the quick audit against final bytes.

## Final audit status of this round

Mathematical theorem status: NOT REOPENED; no contradiction found.

Editorial source status:
**PASS_CLEAN_ROOM_SOURCE_AUDIT_WITH_RELEASE_BLOCKERS**

Literature/theory bridge:
**PASS_AFTER_ERRATUM_HARDENING**

Parameter/convention self-containment:
**PASS**

Static LaTeX consistency:
**PASS**

Compiled/visual publication QA:
**OPEN**

Archive/DOI completion:
**OPEN_BY_DESIGN**

GitHub v1.0.0:
**DO NOT RELEASE YET**

## Next required action

Compile the current candidate, render every page, fix any visual or LaTeX warnings, and perform the final page-level publication audit. Only after that should the reproducibility tree be frozen and the GitHub/Zenodo release created.
