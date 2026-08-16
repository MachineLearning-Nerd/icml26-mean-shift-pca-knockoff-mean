# Environment and artifact record

## Recorded scientific run

The released evidence was produced by:

    uv sync --frozen && uv run --no-sync python reproduce.py

The run metadata in `space/artifacts/current/evidence.json` records:

- backend/flavor: Hugging Face `cpu-upgrade`;
- 8 selected and cgroup vCPUs, 32 GB memory, no GPU devices;
- Python 3.12.12;
- Linux 6.12.94 / glibc 2.36;
- scientific runtime: `472.82791089` seconds;
- estimated run cost: `$0.00394023259075`;
- evidence-producing SHA: `13b55da6455a15560c274deb9f06ce0a0214ebe0`.

The broader release report records cancelled and diagnostic campaign work
separately. Neither the campaign nor the author implementation was rerun
during this documentation cleanup. Any future scientific run must create a
new evidence record and preserve its resource allocation.

## Pinned project inputs

- Root dependency files: `pyproject.toml`, `uv.lock`.
- Cumulative producer: `reproduce.py`.
- Public notebook: `notebooks/mean_shift_pca_reproduction.py`.
- Released copy of the producer: `space/artifacts/current/reproduce.py`.
- Machine-readable evidence: `space/artifacts/current/evidence.json`.
- Release checker output: `space/artifacts/current/release/checker_output.json`.
- Release hashes: `space/artifacts/current/release/upload_manifest.sha256` and
  `space/artifacts/current/judged_manifest.sha256`.

The content-addressed hashes for these artifacts are listed in
`EVIDENCE_MANIFEST.json` and checked by `verify_final.py`.
