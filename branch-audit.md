# Branch and attribution audit

This file preserves the branch migration record used by the original
publication workflow. The detailed final map is in
`BRANCH_AUDIT.md`; this file keeps the former names and their evidence
roles visible for readers following old experiment links.

## Historical migration

| Former branch | Published branch | Evidence role |
| --- | --- | --- |
| `orx/baseline-exact-claim-1-contract` | `audit/claim-1-spectral-separability` | Claim 1 exact collision |
| `orx/claim-2-exact-assumption-counterexample` | `audit/claim-2-eigenspace-invariance` | Claim 2 counterexample |
| `orx/claim-3a-paper-text-eigenvalue-algorithm` | `audit/claim-3-algorithm-1` | Literal Algorithm 1 |
| `orx/claim-3b-released-code-semantics` | `audit/claim-3-released-implementation` | Author implementation semantics |
| `orx/claim-4-calibrated-fluctuation-scaling` | `audit/claim-4-empirical-fluctuations` | Blocked empirical route |
| `orx/claim-4-route-2-analytical-calibration` | `audit/claim-4-analytical-calibration` | Accepted analytical route |
| `orx/claim-5-exact-section-4-benchmark` | `audit/claim-5-section-4-benchmark` | Section 4 benchmark |
| `orx/evaluator-visible-release-candidate` | `release/evaluator-visible-candidate` | Evaluator-facing candidate |
| `orx/final-release-gates` | `release/final-gates` | Cumulative release gates |
| `orx/post-publication-exact-revision-verification` | `release/post-publication-verification` | Published Space verification |
| `orx/publication-manifest-and-release-report` | `release/publication-manifest` | Publication manifest |

## Current remote readback

- Repository: `MachineLearning-Nerd/icml26-mean-shift-pca-knockoff-mean`
- Default branch: `main`
- Public branches: 12 total, consisting of `main` and the 11 published
  names above.
- Pre-dossier unique reachable commits: 19.
- Pre-dossier main tip: `747b344d70ca5f6fed5d61bcd7be561f6569e171`
- Published dossier tip: `3d1fb6b6c337e9489c0bc37c1137023e722c8735`
- All pre-dossier reachable author and committer identities:
  `MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>`
- Legacy `orx/*` branch refs: absent from the GitHub API response.
- Temporary `refs/original/*`: absent from local refs.

The released-implementation branch intentionally diverges from the cumulative
claim-audit line. All other claim and release tips are retained as evidence
branches; no branch was deleted to make the dossier pass.

## Recovery and attribution

Before dossier edits, a complete bundle was created and verified:

- Path: `/tmp/icml-mean-shift-before-dossier.3ewDID/mean-shift-before-dossier.bundle`
- SHA-256: `3c79b3fd7950b7e0ae49ad972797a90534d3d268287eae522eff806f264abd4b`

The dossier commit is authored and committed as
`MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>`.
No `Co-authored-by:` trailer is permitted. The final structural check
`verify_final.py` rechecks all local and origin branches and every reachable
commit after cloning.
