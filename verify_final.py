#!/usr/bin/env python3
"""Fail-closed structural checks for the published Mean-Shift PCA audit."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = "MachineLearning-Nerd/icml26-mean-shift-pca-knockoff-mean"
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "MachineLearning-Nerd@users.noreply.github.com"
EXPECTED_OVERALL_VERDICT = "FALSIFIED_CLAIMS_1_TO_2_VERIFIED_SCOPED_CLAIMS_3_TO_5"
EXPECTED_BRANCHES = {
    "main",
    "audit/claim-1-spectral-separability",
    "audit/claim-2-eigenspace-invariance",
    "audit/claim-3-algorithm-1",
    "audit/claim-3-released-implementation",
    "audit/claim-4-analytical-calibration",
    "audit/claim-4-empirical-fluctuations",
    "audit/claim-5-section-4-benchmark",
    "release/evaluator-visible-candidate",
    "release/final-gates",
    "release/post-publication-verification",
    "release/publication-manifest",
}
EXPECTED_CLAIMS = {
    "C1": "FALSIFIED",
    "C2": "FALSIFIED",
    "C3": "VERIFIED_SCOPED",
    "C4": "VERIFIED_SCOPED",
    "C5": "VERIFIED_SCOPED",
}
EXPECTED_HASHES = {
    "README.md": "192b5bf44fa15f8682fe8db5298b975e24fb6b4e3428a1abe99acb387dd0544e",
    "STATUS.md": "ca44ef3815c9535074a19eae3dbda3107fcb393d602dacc9e7d2658964e033a8",
    "REPORT.md": "ffa5c3dad1fb8e2af20a186039372ff86b72ccd835dd36fd4bd1f954e3d4e72b",
    "claims.json": "fcc07267edcbfe35123b4907e5ca6f64074c1e5a7a44675c1aac3fed46b48c80",
    "reproduction_verdicts.json": "19e90f7c24cbbea7132853f22ed7a106af2e156284a96ee297831a7f9ea3350b",
    "AUTONOMOUS_STATE.json": "e7c2a8c67adf13dc16dbbbf7e983554237546a83a86fefe9a136bc05a73af20c",
}
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "REPORT.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "BRANCH_AUDIT.md",
    "ENVIRONMENT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "claims.json",
    "reproduction_verdicts.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
    "AUTONOMOUS_STATE.json",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def run(*args: str) -> str:
    result = subprocess.run(
        args, cwd=ROOT, check=True, capture_output=True, text=True
    )
    return result.stdout


def read_json(relative_path: str) -> object:
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def sha256(relative_path: str) -> str:
    digest = hashlib.sha256()
    with (ROOT / relative_path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def local_branches() -> set[str]:
    refs = run(
        "git",
        "for-each-ref",
        "refs/heads",
        "--format=%(refname:strip=2)",
    )
    return {ref.strip() for ref in refs.splitlines() if ref.strip()}


def remote_branches() -> set[str]:
    prefix = "refs/remotes/origin/"
    refs = run(
        "git",
        "for-each-ref",
        "refs/remotes/origin",
        "--format=%(refname)",
    )
    return {
        ref.strip()[len(prefix):]
        for ref in refs.splitlines()
        if ref.strip().startswith(prefix) and ref.strip() != prefix + "HEAD"
    }


def verify_history() -> None:
    records = run(
        "git", "log", "--all", "--format=%an%x00%ae%x00%cn%x00%ce"
    ).splitlines()
    if not records:
        fail("no reachable commits")
    expected = (
        f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}\x00"
        f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}"
    )
    unexpected = sorted({record for record in records if record != expected})
    if unexpected:
        fail(f"non-canonical reachable identities: {unexpected}")
    if "Co-authored-by:" in run("git", "log", "--all", "--format=%B"):
        fail("co-author trailer found")
    if int(run("git", "rev-list", "--count", "--all").strip()) < 19:
        fail("historical evidence commits are missing")
    if run("git", "for-each-ref", "refs/original", "--format=%(refname)").strip():
        fail("temporary refs/original remain")
    all_refs = run("git", "for-each-ref", "--format=%(refname)")
    if any("/orx/" in ref or ref.endswith("/orx") for ref in all_refs.splitlines()):
        fail("legacy orx ref remains")


def verify_remote() -> None:
    remote = run("git", "config", "--get", "remote.origin.url").strip()
    normalized = remote.removesuffix(".git").rstrip("/")
    if not normalized.endswith(EXPECTED_REPOSITORY):
        fail(f"origin is {remote!r}, expected {EXPECTED_REPOSITORY!r}")


def verify_branch_tips() -> None:
    local = local_branches()
    for branch in EXPECTED_BRANCHES:
        remote = run("git", "rev-parse", f"refs/remotes/origin/{branch}").strip()
        if branch in local:
            local_tip = run("git", "rev-parse", f"refs/heads/{branch}").strip()
            if local_tip != remote:
                fail(
                    f"local and origin tips differ for {branch}: "
                    f"{local_tip} != {remote}"
                )
    head = run("git", "symbolic-ref", "refs/remotes/origin/HEAD").strip()
    if head != "refs/remotes/origin/main":
        fail(f"origin HEAD is {head!r}, expected origin/main")


def verify_manifest() -> None:
    manifest = read_json("EVIDENCE_MANIFEST.json")
    if not isinstance(manifest, dict):
        fail("manifest must be a JSON object")
    if manifest.get("repository") != EXPECTED_REPOSITORY:
        fail("manifest repository marker is wrong")
    if manifest.get("claim_statuses") != EXPECTED_CLAIMS:
        fail("manifest claim statuses are wrong")
    if manifest.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        fail("manifest overall verdict is wrong")
    if manifest.get("publication_allowed") is not True:
        fail("manifest publication boundary is wrong")
    if manifest.get("score_claim") is not False:
        fail("manifest score boundary is wrong")
    if manifest.get("official_author_endorsement") is not False:
        fail("manifest author-endorsement boundary is wrong")
    expected_audit_files = REQUIRED_FILES
    if set(manifest.get("required_audit_files", [])) != expected_audit_files:
        fail("manifest audit-file list is wrong")
    if set(manifest.get("branches", {}).get("expected_final", [])) != EXPECTED_BRANCHES:
        fail("manifest branch set is wrong")
    if manifest.get("attribution", {}).get("email") != CANONICAL_EMAIL:
        fail("manifest attribution is wrong")
    artifacts = manifest.get("content_addressed_artifacts", [])
    if not artifacts:
        fail("manifest has no content-addressed artifacts")
    for item in artifacts:
        relative_path = item.get("path")
        expected_hash = item.get("sha256")
        if not isinstance(relative_path, str) or not isinstance(expected_hash, str):
            fail("malformed content-addressed artifact")
        if not (ROOT / relative_path).is_file():
            fail(f"missing content-addressed artifact: {relative_path}")
        if sha256(relative_path) != expected_hash:
            fail(f"artifact hash mismatch: {relative_path}")
    artifact_hashes = {
        item["path"]: item["sha256"] for item in artifacts
    }
    for relative_path, expected_hash in EXPECTED_HASHES.items():
        if artifact_hashes.get(relative_path) != expected_hash:
            fail(f"reader-document hash is not pinned: {relative_path}")
        if expected_hash != "PENDING" and sha256(relative_path) != expected_hash:
            fail(f"reader-document hash mismatch: {relative_path}")


def verify_evidence() -> None:
    manifest = read_json("EVIDENCE_MANIFEST.json")
    for relative_path in manifest["required_evidence_paths"]:
        if not (ROOT / relative_path).is_file():
            fail(f"missing required evidence path: {relative_path}")
    evidence = read_json("space/artifacts/current/evidence.json")
    if evidence.get("all_verifiers_passed") is not True:
        fail("recorded cumulative verifier did not pass")
    if evidence.get("arxiv") != "2605.25460":
        fail("evidence paper identifier is wrong")
    claims = {f"C{row['claim']}": row for row in evidence.get("claims", [])}
    raw_statuses = {key: row.get("status") for key, row in claims.items()}
    if raw_statuses != {
        "C1": "FALSIFIED",
        "C2": "FALSIFIED",
        "C3": "VERIFIED",
        "C4": "VERIFIED",
        "C5": "VERIFIED",
    }:
        fail("raw evidence statuses are wrong")
    if claims["C1"]["raw"]["covariance_location_fraction"] != "14/3":
        fail("C1 exact collision is missing")
    if claims["C1"]["negative_control"]["location_gap_fraction"] != "31/20":
        fail("C1 negative control is missing")
    if claims["C2"]["independent_checker"]["counterexample_limits"]["residual_norm"] != 0.2:
        fail("C2 counterexample is missing")
    if claims["C3"]["raw"]["aggregate_joint_success_rate"] < 0.9:
        fail("C3 recorded joint-success result is unexpectedly low")
    if claims["C3"]["raw"]["aggregate_mean_removed_rate"] != 1:
        fail("C3 mean-removal result is missing")
    if not claims["C4"]["independent_checker"]["all_steps_checked"]:
        fail("C4 analytical checker did not pass")
    if claims["C4"]["raw"]["route_1_empirical_evidence"]["status"] != "BLOCKED":
        fail("C4 empirical boundary is missing")
    if claims["C5"]["raw"]["aggregate"]["ms_mean_alignment"] < 0.9:
        fail("C5 MS-PCA alignment result is missing")


def verify_ledgers_and_state() -> None:
    claims = read_json("claims.json")
    state = read_json("AUTONOMOUS_STATE.json")
    if claims.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        fail("claims overall verdict is wrong")
    if claims.get("publication_allowed") is not True:
        fail("claims publication boundary is wrong")
    if claims.get("score_claim") is not False:
        fail("claims score boundary is wrong")
    if claims.get("official_author_endorsement") is not False:
        fail("claims author-endorsement boundary is wrong")
    if {row.get("id"): row.get("status") for row in claims["claims"]} != EXPECTED_CLAIMS:
        fail("claims.json statuses are wrong")
    if state.get("target_github_repository") != (
        "https://github.com/" + EXPECTED_REPOSITORY
    ):
        fail("state repository marker is wrong")
    if state.get("official_code_commit") != (
        "540d660761af1d168813e6c80c6bdefcf2557217"
    ):
        fail("state official-code pin is wrong")
    if state.get("canonical_branch") != "main":
        fail("state canonical branch is wrong")
    if state.get("canonical_identity", {}).get("name") != CANONICAL_NAME:
        fail("state canonical identity is wrong")
    if state.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        fail("state overall verdict is wrong")
    if state.get("publication_allowed") is not True:
        fail("state publication boundary is wrong")
    if state.get("score_claim") is not False:
        fail("state score boundary is wrong")
    if state.get("official_author_endorsement") is not False:
        fail("state author-endorsement boundary is wrong")
    if state.get("branch_count") != len(EXPECTED_BRANCHES):
        fail("state branch count is wrong")
    if state.get("canonical_identity", {}).get("verified_reachable_commits") != 21:
        fail("state reachable-commit checkpoint is wrong")

    reproduction = read_json("reproduction_verdicts.json")
    if reproduction.get("repository") != EXPECTED_REPOSITORY:
        fail("reproduction verdict repository is wrong")
    if reproduction.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        fail("reproduction verdict is wrong")
    if reproduction.get("publication_allowed") is not True:
        fail("reproduction publication boundary is wrong")
    if reproduction.get("score_claim") is not False:
        fail("reproduction score boundary is wrong")
    if reproduction.get("official_author_endorsement") is not False:
        fail("reproduction author-endorsement boundary is wrong")
    if {
        row.get("id"): row.get("status") for row in reproduction["claims"]
    } != EXPECTED_CLAIMS:
        fail("reproduction claim statuses are wrong")


def verify_documentation() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in (
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "BRANCH_AUDIT.md",
        "ENVIRONMENT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "FALSIFIED",
        "VERIFIED",
        "reproduction_verdicts.json",
        "AUTONOMOUS_STATE.json",
        "publication_allowed",
        "score_claim",
        "official_author_endorsement",
        "verify_final.py",
    ):
        if marker not in readme:
            fail(f"README is missing marker {marker!r}")
    branch_audit = (ROOT / "BRANCH_AUDIT.md").read_text(encoding="utf-8")
    if branch_audit.count("| `orx/".replace("`", chr(96))) != 11:
        fail("branch migration table is incomplete")


def main() -> int:
    missing = sorted(
        path for path in REQUIRED_FILES if not (ROOT / path).exists()
    )
    if missing:
        fail(f"missing required paths: {missing}")
    verify_manifest()
    verify_evidence()
    verify_ledgers_and_state()
    verify_remote()
    if local_branches() != {"main"}:
        fail(f"local branches differ: {sorted(local_branches())}")
    if remote_branches() != EXPECTED_BRANCHES:
        fail(f"remote branches differ: {sorted(remote_branches())}")
    verify_branch_tips()
    verify_history()
    verify_documentation()
    print(
        "PASS: Mean-Shift PCA dossier, evidence hashes, 12-branch topology, "
        "canonical history, and final documentation verified"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (
        AssertionError,
        subprocess.CalledProcessError,
        OSError,
        json.JSONDecodeError,
        KeyError,
        TypeError,
    ) as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
