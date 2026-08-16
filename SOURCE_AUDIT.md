# Source audit

## Paper identity

| Source | Record |
| --- | --- |
| Primary paper | [arXiv:2605.25460](https://arxiv.org/abs/2605.25460) |
| Paper title | Mean-Shift PCA by Knockoff Mean |
| Authors | Mengda Li; Zeng Li; Jianfeng Yao |
| Venue note | arXiv record labels the paper ICML 2026 |
| Version used by the evidence | arXiv v1, submitted 2026-05-25 |
| Source HTML | [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2605.25460) |
| Recorded source retrieval | 2026-08-01T19:13:37Z |
| Recorded source SHA-256 | `02f4714097d3681f770d35ed958b53bc44cddac13d97916ea1510dd08e078399` |

The repository records the ar5iv HTML hash used by the original audit. It does
not contain a paper PDF or TeX archive; no newer or unpinned source copy is
silently substituted. Each claim document links to the exact section or
algorithm anchor used by its contract. No OpenReview identifier is recorded
for this paper in the repository, so none is presented as provenance.

## Author implementation

| Field | Record |
| --- | --- |
| Repository | [Mengda-Li/ms-pca](https://github.com/Mengda-Li/ms-pca) |
| Branch | `main` |
| API-observed commit | `540d660761af1d168813e6c80c6bdefcf2557217` |
| API observation date | 2026-08-17 |
| Observed tracked files | `README.md`, `main.py`, `pyproject.toml`, `rebuttal.py`, `rebuttal2.py` |

The author implementation is provenance and a separately audited comparison.
The independent producer in this repository follows the paper-text eigenvalue
matching rule for Claims 3 and 5. The released `main.py` path is kept separate
because it matches singular values, passes a singular value into the inverse
map, and uses different knockoff scaling. A result from either path is not
silently relabeled as the other.

## Evidence boundary

- `space/artifacts/current/evidence.json` records the fixed arXiv source hash,
  Python environment, resource allocation, run SHA, controls, and claim rows.
- `.openresearch/artifacts/claim_1/` through `claim_5/` retain the claim
  contracts and source audits used during the historical campaign.
- The historical run used Hugging Face `cpu-upgrade`, 8 vCPUs, 32 GB, and no
  GPU. The cleanup did not rerun the scientific campaign.
- Claims 3 and 5 are finite experiments; Claims 1 and 2 are contract-level
  algebra/counterexample audits; Claim 4 is a scoped analytical derivation.
- The author repository's existence is not evidence that its full experiments
  were rerun here.
