# Branch audit

## Final branch policy

The public branch names are descriptive and preserve the historical claim and
release topology. The old `orx/` names are migration history only; no remote
branch uses that prefix.

| Final branch | Former branch | Evidence role | Pre-dossier tip |
| --- | --- | --- | --- |
| `main` | `main` | Cumulative public documentation and evidence mirror | `747b344d70ca5f6fed5d61bcd7be561f6569e171` |
| `audit/claim-1-spectral-separability` | `orx/baseline-exact-claim-1-contract` | Exact Theorem 3.5 collision and unequal-strength control | `200727991e5cddf0b22cf23fb851e4a32609b3d9` |
| `audit/claim-2-eigenspace-invariance` | `orx/claim-2-exact-assumption-counterexample` | Assumption-level residual counterexample and centered control | `6266a933dfdc87a5c4434a36b1997855ff91df64` |
| `audit/claim-3-algorithm-1` | `orx/claim-3a-paper-text-eigenvalue-algorithm` | Literal paper-text Algorithm 1 | `dd585205c8e255344179980694b3f64c1b9d490f` |
| `audit/claim-3-released-implementation` | `orx/claim-3b-released-code-semantics` | Author implementation semantics audit | `e245d08bbae9ae8862f7089912f6a3a6aa04f139` |
| `audit/claim-4-analytical-calibration` | `orx/claim-4-route-2-analytical-calibration` | Corrected analytical fluctuation route | `12aff1180d4befc70b8855d0ac1d6e32cbce9d8a` |
| `audit/claim-4-empirical-fluctuations` | `orx/claim-4-calibrated-fluctuation-scaling` | Empirical route retained as blocked | `1ee1c0fff87a3202103dcb891d549c1ccd2c45e7` |
| `audit/claim-5-section-4-benchmark` | `orx/claim-5-exact-section-4-benchmark` | Calibrated Section 4 benchmark | `d568945f1476e3eb1e42ff61f615aeda34c22cba` |
| `release/evaluator-visible-candidate` | `orx/evaluator-visible-release-candidate` | Evaluator-facing evidence surface | `8bf61ad65ae4b053b7c4c1f2921920c57aa2eecf` |
| `release/final-gates` | `orx/final-release-gates` | Cumulative scientific and packaging gates | `9427f87b1be1f1d2850b9cbb18873dbffe8601e8` |
| `release/post-publication-verification` | `orx/post-publication-exact-revision-verification` | Published Space revision verification | `3ae59f94c278a3fe252bf4721dd22600f98fe3a2` |
| `release/publication-manifest` | `orx/publication-manifest-and-release-report` | Publication manifest and release report | `c4a8ee35e5be24b6d081f47f44d4822af68c13ae` |

The pre-dossier snapshot contains 12 public branches and 19 unique reachable
commits. The cumulative `main` line had 18 commits; the
released-implementation branch intentionally diverges from the common
claim-audit line. The first dossier commit on `main` is
`3d1fb6b6c337e9489c0bc37c1137023e722c8735`. Dossier metadata updates
remain on `main` only and do not erase or rewrite any evidence branch.

## Attribution and safety record

- Repository: `MachineLearning-Nerd/icml26-mean-shift-pca-knockoff-mean`.
- Recovery bundle before attribution normalization:
  `/tmp/icml26-mean-shift-history.Q2Jx2O/pre-attribution.bundle`.
- Recovery bundle SHA-256:
  `68094368221b45f48831b14b0dbe1e1941fd5e16d5ed3bb88a5119c29d7c5eaf`.
- The pre-dossier remote was read back through the GitHub API and local refs.
- Every reachable published commit now has both author and committer set to
  `MachineLearning-Nerd
  <MachineLearning-Nerd@users.noreply.github.com>`.
- The dossier commits use the same canonical identity; no
  `Co-authored-by:` trailers are allowed.
- No `refs/original/*`, legacy `orx/*`, or untracked branch rename is part
  of the final public inventory.

`verify_final.py` checks the final branch set, local/remote tip agreement,
canonical history, and absence of temporary rewrite refs after cloning.
