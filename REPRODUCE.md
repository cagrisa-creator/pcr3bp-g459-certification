# Reproducing and auditing the G459 certification

This repository separates a fast integrity audit from the complete numerical
replay. The theorem-critical computation is accepted through finite proof
objects, exact arithmetic, validated interval arithmetic, coverage checks,
and independent fail-closed replay.

The release must be reproduced from a clean extraction. Do not replace a
certificate replay by a new heuristic search or by ordinary floating-point
trajectory sampling.

## 1. Quick audit

Requirements:

- Python 3.10 or newer;
- no third-party Python package is required for the wrapper itself.

From the repository root:

```bash
python3 quick_audit/scripts/QUICK_AUDIT.py
```

Expected terminal output:

```text
PASS_QUICK_AUDIT_R16
packages=9 exact_parameter=PASS theorem_core=PASS
```

The quick audit fails closed on missing evidence packages, SHA-256
mismatches, invalid ZIP files, exact-parameter mismatches, and audited
theorem-core count/status mismatches.

This route is an integrity and accounting audit. It is not a substitute for
the complete numerical replay.

## 2. Manuscript build

The publication candidate is:

```text
manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex
```

A standard TeX Live installation with `latexmk`, `pdflatex`, TikZ,
`natbib`, `booktabs`, `longtable`, and `microtype` is sufficient.

From the repository root:

```bash
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode \
  manuscript/G459_ALL_SUBCRITICAL_PUBLICATION_CANDIDATE_20260927.tex
```

The repository also contains a GitHub Actions workflow that builds the same
source and collects the PDF and LaTeX log for visual QA.

## 3. Full clean-room replay: environment

The complete replay should record exact tool versions. The validated
fixed-energy replay was closed in an environment containing:

- Linux;
- GCC 14.2.0;
- Clang 17.0.0;
- Python 3.13.5;
- MPFR 4.2.2;
- GMP;
- official MPFR development headers.

Equivalent newer environments may be used only if the exact finite
obligations are replayed with the same directed-rounding semantics and all
release acceptance conditions below remain satisfied.

## 4. Full replay blocks

### F — fixed-energy strict convexity

Reference archive:

```text
G459_GLOBAL_SYMPLECTIC_SHEAR_CONVEXITY_R10_20260920.zip
SHA-256 22e6cc69d4d5ee16a6dbe895f65f292143361e3e895f99694cb7bcb1bb9faaa7
```

Replay obligations:

1. regenerate the exact symbolic data and coefficient headers;
2. compare regenerated exact files byte-for-byte with the frozen inputs;
3. rerun Stage A with GCC and Clang;
4. rerun Stage B on every Stage-A deferred root;
5. refine the final pending roots;
6. reconstruct the final ledger;
7. audit exact tiling on a common denominator;
8. replay every final leaf with MPFR-192 directed rounding.

Expected:

- Stage A processed: 24,144;
- outside: 1,670;
- deferred: 11,426;
- Stage B roots: 11,426;
- Stage B PASS: 11,272;
- Stage B OUTSIDE: 83;
- Stage B PENDING: 71;
- refinement tested nodes: 1,189;
- refinement PASS leaves: 630;
- refinement PENDING: 0;
- final ledger: 13,655 = 11,902 PASS + 1,753 OUTSIDE;
- exact tiling gaps: 0;
- exact tiling overlaps: 0;
- MPFR-192: 13,655/13,655 OK;
- minimum lower bound: 8.331573711073198e-09 > 0.

Final-ledger SHA-256:

```text
320397db374d7da2a6aee41788fa07736d8572a8de1ad0a8f3f4c5c0bbca7db2
```

### D1 — deep-energy rebase and propagation

Repository evidence:

```text
quick_audit/evidence/R16_D1_I2_GLOBAL_MPFR_REPLAY_20260925.zip
SHA-256 6f2f8cfbf13817dab25689a4ba8821573ad79f1a53c33454f7e1656119444e77
```

Expected:

- 15,364/15,364 OK;
- 13,612 PASS;
- 1,752 OUTSIDE;
- 0 FAIL;
- residual expected-PASS replay: 4,207/4,207 closed;
- minimum PASS lower bound:
  1.212999365920566124851808e-09 > 0.

### N0 — two-component semantics

Repository evidence:

```text
quick_audit/evidence/R16_N0_TWO_COMPONENT_SEMANTICS_AUDIT_20260925.zip
SHA-256 772f4d994c4a995240ac67892e8d963f3f30703076b238e35bc94d79f8257191
```

Replay both focus-specific Levi-Civita charts, exact positive time factors,
reduced-cocycle quotient conjugacy, transported frame/trivialization
identities, and both component barriers.

Expected:

```text
35/35 gates PASS
```

### N1 — validated rotation lower bound

Repository evidence:

```text
quick_audit/evidence/R16_N1_I2_EVIDENCE_PACKAGE_FINAL_20260926.zip
SHA-256 d7dc02a37bb1480e1b37a123a2c1b035a32ef0d7eebc5af07e43dccc91b611c0
```

Expected:

- mathematical universe: 32,661/32,661 PASS;
- repair cells: 92/92 closed;
- final repair leaves: 1,857 PASS;
- unresolved: 0;
- prefix-free: true;
- duplicate final paths: 0;
- exact weight identity: 1 for every repair cell.

The historical parent search is not part of the replay and must not be
restarted.

### N2 — exact rotation/occupation bridge

Recheck exactly:

```text
(2/5)t40 + (7/200)t35 + (1/100)tR
= (1/100)T + (39/100)t40 + (1/40)t35
```

For hypothetical disk-trivialized CZ <= 2:

```text
2T + 78t40 + 5t35 <= 400*pi
```

The associated convention audit checks the complementary
Robbin-Salamon contribution and the CZ/RS comparison constants used in the
manuscript.

Expected:

```text
R16_N2_EXACT_BUDGET_CHECK=PASS
```

### N3 — current-neck short-period exclusion

Repository evidence:

```text
quick_audit/evidence/R16_N3_I2_AUTHORITATIVE_EVIDENCE_20260926.zip
SHA-256 119f4771af2abc22fa582f6cc6df0ad583d22e214526380d1f112edc1ff8330a
```

Expected:

- 1,212 unweighted Yorke closures;
- 9 weighted Yorke closures;
- 1 scalar-displacement closure;
- 1,222/1,222 closed;
- exact canonical key-order audit PASS.

### N4 — finite return graph

Repository evidence:

```text
quick_audit/evidence/R16_N4_I2_AUTHORITATIVE_EVIDENCE_20260926.zip
SHA-256 fefb2caa2e9371584687616099160f0b0a865eca03661b5878fd7e871f60f5f3
```

Expected:

- 30/30 half-phase transitions PASS;
- 34 collapsed hard edges;
- 0 self edges;
- 0 theta-order violations;
- DAG PASS;
- maximum hard-edge path length: 5.

### N5 — long-regime validated propagation

Repository evidence:

```text
quick_audit/evidence/R16_N5_I2_AUTHORITATIVE_EVIDENCE_20260926.zip
SHA-256 999033ed462bd788b718eff6ce6c5a94117fad49b31e20de4c11fb969f9176ce
```

Expected:

- strong window: 2,392/2,392 PASS;
- minimum A^2 lower bound approximately
  0.1465874050659875668456;
- threshold: (3/200)^2 = 0.000225;
- outer safe halves: 2,362/2,362 PASS;
- hard-sink halves: 10/10 PASS;
- detachment halves: 2,372/2,372 PASS;
- minimum theta_dot lower bound approximately
  0.1896620789449094706178;
- minimum endpoint angular margin approximately
  0.0002847191060330499631457.

Exact visit arithmetic must re-establish:

- residual connected residence < 145*pi/106496 < 1/230;
- tR >= 219/100;
- minimum visits: 504;
- maximum visits per completed cluster: 7;
- minimum clusters: 72;
- final exact contradiction PASS.

### U/A/E — final-entry assembly

Repository evidence:

```text
quick_audit/evidence/R16_FINAL_ENTRY_ASSEMBLY_I2_EVIDENCE_20260926.zip
SHA-256 3a1ec9850f8127635b9c7a4205ffe9e588515f08b31285ca94862a777286c5d8
```

Expected upper-theta genealogy:

- exact roots: 3,072;
- direct roots: 58;
- refined roots: 3,014;
- Tier 1 children: 48,224;
- Tier 1 FAIL: 19,311;
- Tier 2 children: 77,244;
- residual partition: 41,020 BETA + 8,624 EVENT;
- all final BETA/EVENT obligations PASS;
- global minimum Klo:
  0.005708670873993645 > 0.004922.

Expected upper-A and outward-face results:

- 32/32 A-bands replayed;
- summed dwell upper:
  0.083811044147392185915 < 17/200;
- beta >= 1/20 on 39 exact phi cells;
- entry time > 1/40;
- both B phi faces: 1,024/1,024 outward;
- upper-A final margin: 3/20000 > 0;
- upper-theta margin:
  0.0007874964368999028 > 0;
- final 16-cell assembly:
  14 pointwise + 2 integrated = 16/16.

### C — complementary trust base

Repository evidence:

```text
quick_audit/evidence/R16_COMPLEMENTARY_TRUST_BASE_I2_EVIDENCE_20260926.zip
SHA-256 53bd25304a10c6d3b932f2a6c8787dd9e91b2f16aee0bc8c7e0e01455bdef5eb
```

Replay:

- exact 16-cell cover and 14-cell pointwise terminal checker;
- one-way corridor flow and outward faces;
- 39-seed whole-shell beta >= 1/20 cover and flow;
- 50 exact jobs and narrow negative sublayer;
- beta >= 0 on the two exceptional cells;
- global A_dot < 0;
- modified-rotation arithmetic.

Expected terminal checker aggregate:

```text
130,848 leaves in 302 chunks
failures=0
```

## 5. Final theory bridge

The final non-numerical audit must check that:

- the exact symplectic shear preserves disk-trivialized CZ under the
  transported disk trivialization;
- positive time changes preserve the reduced CZ/RS data under transported
  cocycle conjugacy;
- a contractible capping disk lifts through S3 -> RP3 and the disk-CZ index
  agrees;
- strict convexity implies dynamical convexity;
- the standard retrograde binding is a 2-unknot with self-linking -1/2;
- the p=2 rational-open-book theorem gives disk-like global pages.

These are theorem/version-sensitive obligations and must be checked against
the exact cited sources used by the manuscript.

## 6. Full clean-room acceptance

A complete replay passes only when:

- every archived SHA-256 matches;
- every finite universe has no missing, extra, or duplicate obligation;
- every strict inequality remains strict;
- every coverage audit passes;
- every independent replay/checker result matches the expected result above;
- the final manuscript claims are no stronger than the archived evidence.

The expected final marker is:

```text
PASS_FULL_REPRODUCE_R16
```

The release is not considered frozen merely because the quick audit passes.
The final release gate also requires the exact release-tree SHA-256 manifest
and a clean replay record for the bytes that are actually tagged as v1.0.0.
