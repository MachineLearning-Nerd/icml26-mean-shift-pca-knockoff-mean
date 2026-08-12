# Repository status

- Paper: Mean-Shift PCA by Knockoff Mean
- Authors: Mengda Li; Zeng Li; Jianfeng Yao
- arXiv: 2605.25460
- Venue note: ICML 2026
- Author code: https://github.com/Mengda-Li/ms-pca
- Author code pin: 540d660761af1d168813e6c80c6bdefcf2557217
- Former repository: icml26-repro-ISNSiAC3n1-mean-shift-pca-by-knockoff-mean
- Target repository: icml26-mean-shift-pca-knockoff-mean
- Canonical branch: main
- Historical branch count: 11 claim/release branches plus main
- Historical branch cleanup: ORX names will be replaced by descriptive audit/ and release/ names; evidence branches are retained
- Current phase: completed_scoped_audit_awaiting_live_judge
- Live judge score: 5/10, not a scientific result
- Compute: Hugging Face cpu-upgrade, recorded 8-vCPU/32 GB allocation, no GPU
- Official code status: public author implementation available; paper-text Algorithm 1 and released main.py are audited as separate semantics

## Claim state

- Claim 1: FALSIFIED for universal disjointness wording; exact collision at 14/3; generic unequal-strength separation remains distinct.
- Claim 2: FALSIFIED under cited assumptions by residual counterexample; centered control decays at root-n.
- Claim 3: VERIFIED within literal Algorithm 1, c = 1, 5% contamination, n = 500/1000/2000, 12 trials each.
- Claim 4: VERIFIED within corrected analytical Gaussian supercritical/right-invariance scope; empirical finite-size route remains blocked.
- Claim 5: VERIFIED within c = 1, 5% contamination, n = 500/1000/2000; Robust PCA comparison limited to 12 paired n = 500 trials.

Publication status: published as a scoped audit; not a claim of unrestricted theorem or full-grid reproduction.
