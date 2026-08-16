# Mean-Shift PCA by Knockoff Mean

Claim-by-claim reproduction and audit record for the ICML 2026 paper by Mengda Li, Zeng Li, and Jianfeng Yao.

Current status: **completed scoped audit, awaiting live judge review**. The audit records five claim verdicts, preserves the exact evidence and controls, and keeps the historical claim and release branches under clean names. The recorded live judge score is 5/10; that score is not a scientific claim.

## Paper and provenance

| Field | Record |
| --- | --- |
| Paper | Mean-Shift PCA by Knockoff Mean |
| Authors | Mengda Li; Zeng Li; Jianfeng Yao |
| Primary record | [arXiv:2605.25460](https://arxiv.org/abs/2605.25460) |
| Venue note | arXiv record marked ICML 2026 |
| Author implementation | [Mengda-Li/ms-pca](https://github.com/Mengda-Li/ms-pca) |
| Author implementation pin | API-verified main commit 540d660761af1d168813e6c80c6bdefcf2557217 (2026-08-17) |
| Paper source pin | ar5iv HTML retrieved 2026-08-01; SHA-256 02f4714097d3681f770d35ed958b53bc44cddac13d97916ea1510dd08e078399 |
| Collection | ICML 2026 reproduction collection |
| Former repository | icml26-repro-ISNSiAC3n1-mean-shift-pca-by-knockoff-mean |
| Current repository | [MachineLearning-Nerd/icml26-mean-shift-pca-knockoff-mean](https://github.com/MachineLearning-Nerd/icml26-mean-shift-pca-knockoff-mean) |
| Canonical branch | main |

The paper proposes a two-stage PCA procedure that adds a controlled knockoff mean shift. The original sample eigenvalues are compared with the perturbed eigenvalues: a mean-shift component should move, while an eigenvalue caused by the uncontaminated covariance should remain stable.

## Audit dossier

The repository-level audit record is split into small, reviewable files:

- `CLAIM_EVIDENCE.md` maps each paper claim to its producer, raw output, controls, status, and limitation.
- `SOURCE_AUDIT.md` pins the paper source and the current author implementation.
- `BRANCH_AUDIT.md` records every branch, its former name, purpose, and attribution check.
- `ENVIRONMENT.md` records the fixed command, historical compute, and artifact paths.
- `REPORT.md` gives the conservative release decision.
- `CITATION.cff` and `AUTHOR_THANK_YOU.md` provide citation and author acknowledgment.
- `claims.json` and `EVIDENCE_MANIFEST.json` provide machine-readable statuses and hashes.
- `verify_final.py` checks the public branch topology, evidence files, and canonical commit history.

The final public topology is `main` plus 11 descriptive `audit/` and
`release/` branches. Historical `orx/` names are retained only as migration
history in the branch audit; they are not live branch names.

## What the paper is doing

The paper studies high-dimensional mean-shift contamination, where most observations come from an inlier distribution and a smaller group has the same covariance but a shifted mean. In this setting:

1. Ordinary PCA can mistake the mean-shift component for a genuine covariance direction.
2. Existing Robust PCA methods are not matched to a dense, low-rank mean-shift matrix.
3. Random-matrix analysis describes covariance-induced and mean-shift-induced eigenvalue locations.
4. Theorem 3.11 analyzes asymptotic eigenspace invariance under the contamination model.
5. Algorithm 1 adds a rank-one knockoff mean and retains eigenvectors whose eigenvalues remain stable.

The paper's Section 4 evaluates MS-PCA against ordinary PCA and Robust PCA in a one-spike Gaussian mixture.

## Claim ledger

These statuses describe this reproduction contract. They do not replace the paper's theorem statements, and a falsified stronger interpretation is not automatically a falsification of every narrower theorem formula.

| Claim | Paper target | How the claim is produced and checked | Audit status |
| --- | --- | --- | --- |
| 1 | Theorem 3.5: covariance and mean-shift eigenvalue locations are universally disjoint and separable | Use the paper's map at c = 1/2 and ell = theta squared = 3. Both locations equal 14/3 exactly. Run a distinct-strength negative control at theta squared = 6/5, where the gap is 31/20. | **FALSIFIED** for the universal disjointness wording; the union/convergence formula and generic unequal-strength separation are not disputed. Evidence: space/artifacts/current/evidence.json and reports/claim_1/page.md |
| 2 | Theorem 3.11: the contamination residual for every clean covariance eigenvector is O_p(n^-1/2) | Construct X = u 1 transposed and independent A = q gamma transposed under the cited assumptions. The residual stays near pi = 1/5, while a centered alternating right-factor control decays with slope about -0.503. | **FALSIFIED** under the cited assumptions, with a caveat that an unstated centering or isotropic-right-factor condition would exclude the counterexample. Evidence: reports/claim_2/page.md and the claim 2 raw rows in space/artifacts/current/evidence.json |
| 3 | Algorithm 1 removes mean-shift spikes while retaining covariance spikes | Implement the paper-text eigenvalue algorithm, use c = 1, 5% contamination, n = 500, 1000, 2000, 12 trials per size, a dense eigensolver check, and a zero-knockoff control. | **VERIFIED within the tested Gaussian regime**: 91.7% joint success, 91.7% covariance retention, and 100% mean-spike removal. Evidence: reports/claim_3/page.md and the claim 3 raw rows |
| 4 | Isolated covariance and Bernoulli mean spikes fluctuate at n^-1/2 while the unspiked edge fluctuates at n^-2/3 | The empirical route was retained as blocked because its edge interval and wrong-rate discriminator were inconclusive. The accepted route reconstructs the Gaussian analytical bridge, conditions on Bernoulli membership, applies right-orthogonal invariance and the delta method, and rejects a BBP-threshold control. | **VERIFIED within the supercritical Gaussian/right-invariance scope**. The audit corrects the cited supporting result to Theorem 2.18 of arXiv:1103.2221 and does not generalize beyond that scope. Evidence: reports/claim_4/page.md |
| 5 | Section 4: MS-PCA outperforms ordinary PCA and Robust PCA under 5% mean-shift contamination | Run the literal Algorithm 1 at d/n = 1 with 12 trials at each n in 500, 1000, 2000. Compare against ordinary PCA and rpca 0.1.6 on the 12 paired n = 500 trials, with paired bootstrap intervals, a dense eigensolver, and a contamination-off control. | **VERIFIED within the disclosed finite grid**: MS-PCA alignment 0.940, ordinary PCA 0.086, Robust PCA 0.079 on the paired subset. MS-PCA won 94.4% of PCA pairs and 91.7% of Robust PCA pairs. Two trials selected the wrong stable component. Evidence: reports/claim_5/page.md and the claim 5 raw rows |

## Branch map

The repository retains the historical evidence branches because each one records a distinct claim or release decision. The published names are clean and descriptive; no branch is named ORX.

| Published branch | Former branch | Purpose |
| --- | --- | --- |
| audit/claim-1-spectral-separability | orx/baseline-exact-claim-1-contract | Exact Theorem 3.5 collision and unequal-strength control |
| audit/claim-2-eigenspace-invariance | orx/claim-2-exact-assumption-counterexample | Assumption-satisfying residual counterexample and centered control |
| audit/claim-3-algorithm-1 | orx/claim-3a-paper-text-eigenvalue-algorithm | Literal paper-text Algorithm 1 verifier |
| audit/claim-3-released-implementation | orx/claim-3b-released-code-semantics | Separate audit of the author repository's released implementation |
| audit/claim-4-empirical-fluctuations | orx/claim-4-calibrated-fluctuation-scaling | Empirical finite-size fluctuation route; retained as blocked |
| audit/claim-4-analytical-calibration | orx/claim-4-route-2-analytical-calibration | Corrected analytical fluctuation derivation and BBP control |
| audit/claim-5-section-4-benchmark | orx/claim-5-exact-section-4-benchmark | Calibrated Section 4 benchmark and Robust PCA subset |
| release/evaluator-visible-candidate | orx/evaluator-visible-release-candidate | Candidate public evidence surface and evaluator traversal |
| release/final-gates | orx/final-release-gates | Cumulative scientific, bundle, notebook, and blind-review gates |
| release/post-publication-verification | orx/post-publication-exact-revision-verification | Exact published Space revision redownload and hash verification |
| release/publication-manifest | orx/publication-manifest-and-release-report | Publication manifest and release report |
| main | main | Canonical cumulative mirror and public documentation |

All historical branches except audit/claim-3-released-implementation are ancestors of the cumulative main line. The released-implementation branch diverged intentionally because it audits code semantics that differ from the paper-text Algorithm 1.

## Evidence and production paths

The cumulative verifier is reproduce.py. It produces a delimited EVIDENCE_JSON record containing assumptions, raw seeded rows, controls, runtime, CPU allocation, GPU absence, environment information, and the Git SHA used for the run.

- Claim contracts: space/artifacts/current/claims/claim_1 through claim_5/claim_contract.json
- Per-claim methods and limitations: space/artifacts/current/claims/claim_1 through claim_5/
- Cumulative evidence: space/artifacts/current/evidence.json
- Illustrated report: reports/mean-shift-pca/report.md
- Per-claim reports: reports/claim_1/page.md through reports/claim_5/page.md
- Release gates: space/artifacts/current/release/final_release_report.md
- Release hashes: space/artifacts/current/release/upload_manifest.sha256 and judged_manifest.sha256
- Published tutorial: notebooks/mean_shift_pca_reproduction.py
- Historical contract and gap analysis: .openresearch/artifacts/ and audits/
- Final-state structural check: verify_final.py

## Reproduce the recorded verifier

The complete campaign is computationally expensive and was run on Hugging Face cpu-upgrade with an 8-vCPU, 32 GB allocation and no GPU. The repository already contains the resulting evidence; do not infer a fresh result from the README alone.

Install uv, then run:

    uv sync --frozen
    uv run --no-sync python reproduce.py

The command exits nonzero if an accepted claim checker or its intended negative control fails. Exact runtime, resource allocation, and all raw rows are part of the emitted evidence.

## Official code comparison

The author repository is public and is pinned above. Its main branch contains README.md, main.py, pyproject.toml, rebuttal.py, and rebuttal2.py. The audit keeps two implementation paths separate:

- Algorithm 1 in this reproduction follows the paper's printed eigenvalue matching rule.
- The released author main.py is audited separately because it matches singular values and passes a singular value into the inverse eigenvalue map, with a different knockoff scaling.

This distinction is essential: a result for the paper-text algorithm must not be silently presented as a result for the released implementation.

## Citation

    @article{li2026meanshift,
      title   = {Mean-Shift PCA by Knockoff Mean},
      author  = {Li, Mengda and Li, Zeng and Yao, Jianfeng},
      journal = {arXiv preprint arXiv:2605.25460},
      year    = {2026},
      doi     = {10.48550/arXiv.2605.25460}
    }

Please cite the original paper when using this audit or its evidence. The authors' paper remains the source of the scientific claims; this repository records independent checks, limitations, and counterexamples.

## Thank-you note

Thank you to Mengda Li, Zeng Li, and Jianfeng Yao for making the mean-shift contamination problem and the knockoff-mean idea available as a concrete target for reproduction. The paper's combination of random-matrix theory and a simple perturbation-based PCA procedure makes the assumptions and failure modes unusually inspectable. This audit is intended as a respectful record of what was reproduced, what was falsified under a stated contract, and where the evidence remains deliberately scoped.

## Limitations and interpretation

- Claims 1 and 2 report narrow, assumption-level findings; they should not be summarized as “the entire paper is false.”
- Claims 3 and 5 are finite-grid experiments, not the full asymptotic or full benchmark design.
- Claim 4 is analytical and specifically scoped to the Gaussian supercritical/right-invariance route; its initial empirical route remains blocked.
- Robust PCA was run on a 12-trial n = 500 paired subset because the larger design exceeded the measured runtime budget.
- The campaign used external CPU compute, recorded in the release report; future changes must preserve the exact evidence and environment pins.
