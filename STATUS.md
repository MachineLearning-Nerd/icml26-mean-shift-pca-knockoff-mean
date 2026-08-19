# Repository status

- Paper: Mean-Shift PCA by Knockoff Mean
- Authors: Mengda Li; Zeng Li; Jianfeng Yao
- Primary record: arXiv 2605.25460, marked ICML 2026
- Author code: https://github.com/Mengda-Li/ms-pca
- Author code pin: 540d660761af1d168813e6c80c6bdefcf2557217
- Former repository: icml26-repro-ISNSiAC3n1-mean-shift-pca-by-knockoff-mean
- Current repository: icml26-mean-shift-pca-knockoff-mean
- Canonical branch: main
- Public branches: main plus 11 descriptive audit/release branches
- Branch cleanup: complete; no live `orx/*` branch remains
- Commit attribution: all reachable commits use MachineLearning-Nerd as author and committer
- Current phase: published_scoped_audit
- Live judge score: 5/10, retained as provenance and not a scientific result
- Compute: historical Hugging Face `cpu-upgrade`, 8 vCPUs, 32 GB, no GPU
- Official code status: public; paper-text Algorithm 1 and released `main.py` are audited as separate semantics

## Claim state

- Claim 1: **FALSIFIED** for universal disjointness wording; exact collision at `14/3`; generic unequal-strength separation remains distinct.
- Claim 2: **FALSIFIED** under cited assumptions by a residual counterexample; centered control decays at root-n.
- Claim 3: **VERIFIED_SCOPED** within literal Algorithm 1, `c = 1`, 5% contamination, `n = 500/1000/2000`, 12 trials each.
- Claim 4: **VERIFIED_SCOPED** within corrected analytical Gaussian supercritical/right-invariance scope; empirical finite-size route remains blocked.
- Claim 5: **VERIFIED_SCOPED** within `c = 1`, 5% contamination, `n = 500/1000/2000`; Robust PCA comparison limited to 12 paired `n = 500` trials.

Publication status: published as a scoped audit with citation, author thanks,
claim-to-evidence ledger, source pin, branch map, reproduction verdicts, and
final-state verifier. publication_allowed=true applies only to this scoped
dossier; score_claim=false and official_author_endorsement=false.
Overall verdict: FALSIFIED_CLAIMS_1_TO_2_VERIFIED_SCOPED_CLAIMS_3_TO_5
