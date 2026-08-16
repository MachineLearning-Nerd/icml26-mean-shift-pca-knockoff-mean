# Audit report

## Decision

**FALSIFIED_CLAIMS_1_TO_2_VERIFIED_SCOPED_CLAIMS_3_TO_5**

The repository is a scoped, published audit of all five paper targets. Claims
1 and 2 fail their stated universal/assumption-level contracts. Claims 3–5
pass only the finite or analytical scopes documented in
`CLAIM_EVIDENCE.md`; this is not a claim that the entire paper is proved or
disproved.

## Evidence decision

- C1: exact collision of the two mapped locations at `14/3`; unequal-strength
  control gap `31/20`.
- C2: assumption-level residual counterexample remains near `0.2`; centered
  control follows root-n scaling.
- C3: literal Algorithm 1 reaches `91.667%` joint success and `100%`
  mean-spike removal over 36 trials.
- C4: analytical Gaussian/supercritical/right-invariance derivation passes;
  the empirical finite-size route remains blocked.
- C5: finite Section 4 grid gives MS-PCA alignment `0.9403` versus PCA
  `0.0858` and Robust PCA `0.0791` on the paired subset.

## Publication boundary

The live judge's historical score is `5/10`. It is retained as release
provenance and is not a scientific result. The repository does not claim a
new score, full paper-grid execution, unrestricted theorem validation, or
author endorsement.

## Target repository

`MachineLearning-Nerd/icml26-mean-shift-pca-knockoff-mean` is the clean public
name for the former
`icml26-repro-ISNSiAC3n1-mean-shift-pca-by-knockoff-mean`. It retains all 11
descriptive audit/release branches plus `main`, the paper citation, author
thanks, claim ledger, source audit, branch audit, content hashes, and a
dependency-free final-state verifier.
