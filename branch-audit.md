# Branch and attribution audit

The initial inventory below was captured before the documentation, repository rename, branch rename, and attribution normalization. The final state is recorded at the end of this file.

## Remote inventory

- Former repository: MachineLearning-Nerd/icml26-repro-ISNSiAC3n1-mean-shift-pca-by-knockoff-mean
- Pre-cleanup default branch: main at 23c4f666caed8fa16d6be0eef9be0a9255f47b7b
- Additional remote branches: 11
- Historical names: all additional branches used the ORX prefix
- Main-line relation: 10 additional branches are ancestors of main; the released-code semantics branch intentionally diverges

## Branch rename plan

| Old branch | New branch | Evidence role |
| --- | --- | --- |
| orx/baseline-exact-claim-1-contract | audit/claim-1-spectral-separability | Claim 1 exact collision |
| orx/claim-2-exact-assumption-counterexample | audit/claim-2-eigenspace-invariance | Claim 2 counterexample |
| orx/claim-3a-paper-text-eigenvalue-algorithm | audit/claim-3-algorithm-1 | Literal Algorithm 1 |
| orx/claim-3b-released-code-semantics | audit/claim-3-released-implementation | Author implementation semantics |
| orx/claim-4-calibrated-fluctuation-scaling | audit/claim-4-empirical-fluctuations | Blocked empirical route |
| orx/claim-4-route-2-analytical-calibration | audit/claim-4-analytical-calibration | Accepted analytical route |
| orx/claim-5-exact-section-4-benchmark | audit/claim-5-section-4-benchmark | Section 4 benchmark |
| orx/evaluator-visible-release-candidate | release/evaluator-visible-candidate | Evaluator-facing candidate |
| orx/final-release-gates | release/final-gates | Cumulative release gates |
| orx/post-publication-exact-revision-verification | release/post-publication-verification | Published Space verification |
| orx/publication-manifest-and-release-report | release/publication-manifest | Publication manifest |

The old names are retained in this file as migration history. The new names are the canonical public names after cleanup.

## Attribution plan

The reachable history currently contains:

    Dinesh Jinjala <dinesh.jinjala@mareana.com>
    Dinesh Jinjala <37579156+MachineLearning-Nerd@users.noreply.github.com>
    GitHub <noreply@github.com>

Before publishing the normalized copy, rewrite every reachable commit's author and committer to:

    MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>

The rewrite changes identity metadata only. It preserves the claim evidence, branch topology, source links, and release artifacts.

## Final published state

- Repository: MachineLearning-Nerd/icml26-mean-shift-pca-knockoff-mean
- Default branch: main
- Published branches: main plus the 11 descriptive audit/release names in the table above
- Deleted refs: all 11 old ORX branch names
- Reachable commit identity: MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com> for both author and committer
- Branch evidence preserved: yes; the released-implementation audit remains a deliberately diverged branch
