# Claim-to-evidence map

This repository reports claim contracts and reproducible evidence boundaries.
Finite checks, counterexamples, and scoped numerical results do not replace the
paper's proofs. The production graph is:

    paper anchor -> explicit contract -> independent producer
                 -> raw output -> checker/control -> status and limitation

The canonical cumulative producer is `reproduce.py`. It emits a delimited JSON
record and writes the released evidence surface under
`space/artifacts/current/`. The historical campaign used the fixed command in
`ENVIRONMENT.md`; the dossier cleanup did not rerun that campaign.

## C1 — spectral separability (Theorem 3.5)

- Contract: for every admissible parameter tuple, the covariance-induced
  location set and mean-induced location set are disjoint.
- Paper anchor:
  [Theorem 3.5](https://ar5iv.labs.arxiv.org/html/2605.25460#S3.Thmtheorem5).
- Producer: `reproduce.py::verify_claim_1`, using exact `Fraction` algebra at
  `c = 1/2`, `ell = 3`, and `theta^2 = 3`.
- Evidence: `space/artifacts/current/evidence.json` and
  `reports/claim_1/page.md`.
- Independent check: both locations equal `14/3` exactly, while the
  unequal-strength control at `theta^2 = 6/5` has gap `31/20`.
- Status: **FALSIFIED** for the universal disjointness wording.
- Boundary: the collision does not dispute the union/convergence formula or
  generic separation when the mapped strengths differ.

## C2 — eigenspace invariance (Theorem 3.11)

- Contract: under Assumptions 3.1 and 3.10, every clean covariance eigenvector
  has contaminated residual norm `O_p(n^-1/2)`.
- Paper anchor:
  [Theorem 3.11](https://ar5iv.labs.arxiv.org/html/2605.25460#S3.Thmtheorem11).
- Producer: `reproduce.py::verify_claim_2`, which constructs
  `X = u 1^T` and `A = q gamma^T` under the stated independence structure,
  then compares six sizes from `n = 250` through `8000`.
- Evidence: `space/artifacts/current/evidence.json` and
  `reports/claim_2/page.md`.
- Controls: the uncentered counterexample stays near residual `0.2`; the
  centered alternating right-factor control ends at median
  `0.0032288661416099264` with slope `-0.502738712396082`.
- Status: **FALSIFIED** under the cited assumptions.
- Boundary: an additional unstated centering or isotropic-right-factor
  condition could exclude the counterexample; that condition is not silently
  added to the paper contract.

## C3 — literal Algorithm 1

- Contract: the paper-text eigenvalue algorithm removes the mean-shift spike
  while retaining a covariance spike in the disclosed Gaussian regime.
- Paper anchor:
  [Algorithm 1](https://ar5iv.labs.arxiv.org/html/2605.25460#alg1).
- Producer: `reproduce.py::verify_claim_3`, using `c = 1`, 5% contamination,
  `n in {500, 1000, 2000}`, 12 trials per size, dense eigensolver agreement,
  and a zero-injection control.
- Evidence: `space/artifacts/current/evidence.json` and
  `reports/claim_3/page.md`.
- Results: joint success `0.9166666666666666`, covariance retention
  `0.9166666666666666`, and mean-spike removal `1.0` over 36 trials.
- Status: **VERIFIED within the tested Gaussian regime**.
- Boundary: `audit/claim-3-released-implementation` separately audits the
  author implementation. It must not be conflated with the paper-text
  algorithm because the released code matches singular values and uses a
  different knockoff scaling.

## C4 — fluctuation rates

- Contract: isolated covariance and Bernoulli mean spikes fluctuate at
  `n^-1/2`, while the unspiked upper edge fluctuates at `n^-2/3` in the
  paper's Gaussian high-dimensional model.
- Paper anchor:
  [fluctuation discussion](https://ar5iv.labs.arxiv.org/html/2605.25460#S2.SS0.SSS0.Px3).
- Producers: `reproduce.py::verify_claim_4` contains the empirical route;
  `reproduce.py::verify_claim_4_analytical` is the accepted route called by
  `reproduce.py::main`.
- Evidence: `space/artifacts/current/evidence.json` and
  `reports/claim_4/page.md`.
- Analytical checks: edge `2.914213562373095`, outlier `3.75`, gap
  `0.8357864376269051`, and every reconstructed derivation step passes.
- Controls and limitation: the direct empirical route is retained as
  `BLOCKED` because its slope interval and wrong-rate discriminator were
  inconclusive. The accepted route is **VERIFIED within the supercritical
  Gaussian/right-invariance scope** and rejects a BBP-threshold control.
- Boundary: no extension to arbitrary non-Gaussian matrices or
  threshold-critical spikes is claimed.

## C5 — Section 4 benchmark

- Contract: in the disclosed one-spike Gaussian experiment at `d/n = 1` and
  5% contamination, MS-PCA recovers the clean principal component better than
  ordinary PCA and the tested Robust PCA baseline.
- Producer: `reproduce.py::verify_claim_5`, with 12 trials at each of
  `n = 500, 1000, 2000`, a dense eigensolver check, and a contamination-off
  control. Robust PCA is evaluated on the 12 paired `n = 500` trials.
- Evidence: `space/artifacts/current/evidence.json`,
  `space/artifacts/current/claim5_trials.csv`, and
  `reports/claim_5/page.md`.
- Results on the paired comparison: MS-PCA alignment `0.9403016931618414`,
  PCA `0.08584453793620149`, Robust PCA `0.07908832402231025`; MS-PCA wins
  `94.444%` of PCA pairs and `91.667%` of Robust PCA pairs.
- Status: **VERIFIED within the disclosed finite grid**.
- Boundary: this is not the full 15-size, 25-trial, 16-setting paper grid.
  The larger Robust PCA route was not completed and is not represented by a
  proxy result.

## Overall interpretation

Claims 1 and 2 are falsified under explicit contracts; Claims 3–5 are
verified only at the scopes stated above. The live judge's historical `5/10`
score is provenance, not scientific evidence. The raw outputs, source
anchors, controls, and limitations remain separate so a future rerun can
change a status without rewriting the paper's claims.
