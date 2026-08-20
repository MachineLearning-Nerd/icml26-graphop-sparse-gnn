#!/usr/bin/env python3
"""Verify the committed publication contract for this repository."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_STATUS = (
    "PARTIAL_C1_C2_C5_VERIFIED_C3_C4_C6_FALSIFIED_"
    "HISTORICAL_SCORE_9_OF_12_NO_CURRENT_SCORE"
)
EXPECTED_BRANCHES = {
    "audit/claim2-bounded-fibers",
    "audit/claim3-uniform-constant",
    "audit/claim4-depth-zero",
    "audit/claim5-mpnn-approximation",
    "audit/claim5-proof-reconstruction",
    "audit/claim6-generalization-counterexample",
    "audit/claims1-2-finite-certificates",
    "audit/claims1-2-general-proof",
    "historical/judged-baseline",
    "main",
    "release/evaluator-candidate",
    "release/final-publication",
    "release/general-proof-candidate",
    "release/strengthened-evidence",
}
EXPECTED_COMMITS = 41
CANONICAL_IDENTITY = (
    "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
)
CLAIM_IDS = ["C1", "C2", "C3", "C4", "C5", "C6"]


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"verification failed: {message}")


def published_branches() -> set[str]:
    remote = {
        name.removeprefix("origin/")
        for name in git(
            "for-each-ref",
            "refs/remotes/origin",
            "--format=%(refname:short)",
        ).splitlines()
        if name.startswith("origin/") and name != "origin/HEAD"
    }
    if remote:
        return remote
    return set(git("for-each-ref", "refs/heads", "--format=%(refname:short)").splitlines())


def main() -> None:
    claims = load("claims.json")
    verdicts = load("reproduction_verdicts.json")
    manifest = load("EVIDENCE_MANIFEST.json")
    state = load("AUTONOMOUS_STATE.json")
    logbook = load("release/space_upload/logbook.json")
    live = load("release/space_upload/evidence/source/live_verdict_9of12.json")
    claim1 = load(".openresearch/artifacts/claim_1/checker_output.json")
    claim2 = load(".openresearch/artifacts/claim_2/checker_output.json")
    claim3 = load(".openresearch/artifacts/claim_3/checker_output.json")
    claim4 = load(".openresearch/artifacts/claim_4/checker_output.json")
    claim5 = load(".openresearch/artifacts/claim_5/checker_output.json")
    claim6 = load(".openresearch/artifacts/claim_6/checker_output.json")

    expected_statuses = {
        "C1": "VERIFIED_SCOPED",
        "C2": "VERIFIED_SCOPED",
        "C3": "FALSIFIED_SCOPED",
        "C4": "FALSIFIED_SCOPED",
        "C5": "VERIFIED_SCOPED",
        "C6": "FALSIFIED_SCOPED",
    }
    require(claims["overall_status"] == EXPECTED_STATUS, "claims overall status")
    require(state["overall_status"] == EXPECTED_STATUS, "autonomous state overall status")
    require(
        verdicts["overall_verdict"] == "PARTIAL_C1_C2_C5_VERIFIED_C3_C4_C6_FALSIFIED",
        "overall verdict",
    )
    require([claim["id"] for claim in claims["claims"]] == CLAIM_IDS, "claim ordering")
    require(
        {claim["id"]: claim["status"] for claim in claims["claims"]} == expected_statuses,
        "claim statuses",
    )
    require(verdicts["claim_statuses"] == expected_statuses, "verdict statuses")
    require(
        all((ROOT / path).exists() for path in manifest["required_paths"]),
        "manifest paths",
    )

    require(logbook["space_id"] == "DineshAI/tRsnpaRO0m", "Space identity")
    require(logbook["root"]["file"] == "pages/current/index.md", "current entrypoint")
    require(logbook["revision"] == "release-candidate", "release logbook revision")
    require(live["record"]["space_id"] == "DineshAI/tRsnpaRO0m", "live verdict identity")
    require(live["record"]["sha"] == "3ed60dc4ac62b111cb7ca0ef7c752586a10aa8b5", "latest judged SHA")
    require(live["record"]["derived_score"] == "9/12", "latest historical score")
    require(live["record"]["claims"][0]["verdict"] == "toy", "historical Claim 1 verdict")

    family_sweeps = claim1["family_sweeps"]
    require(sum(item["instances"] for item in family_sweeps) == 34, "C1 family count")
    require(
        sum(item["total_operator_cells_certified"] for item in family_sweeps)
        == 448593904,
        "C1 operator-cell count",
    )
    require(claim1["generic_finite_atomic_audit"]["criterion_equivalences_checked"] == 324, "C1 finite certificate")
    require(claim2["generic_finite_atomic_audit"]["fiber_uniqueness_from_atom_indicators"] is True, "C2 uniqueness")
    require(claim2["negative_controls"][0]["rejected_as_bofop"] is True, "C2 unbounded-fiber control")
    require(claim3["status"] == "FALSIFIED", "C3 verdict")
    require(claim3["input_action_metric_upper_bound"] == "8", "C3 metric bound")
    require(claim3["output_gap_formula"] == "M", "C3 output gap")
    require(claim3["adversarial_choice"] == "M=8*C+1", "C3 adversary")
    require(claim4["status"] == "FALSIFIED", "C4 verdict")
    require(claim4["quantified_depth_includes_zero"] is True, "C4 depth quantifier")
    require(claim4["arbitrary_probability_measure_realized"] is True, "C4 arbitrary measure")
    require(claim4["conclusion"] == "Gamma_0(BF_d^r)=P(H0), not a strict subset", "C4 conclusion")
    require(claim5["status"] == "VERIFIED", "C5 verdict")
    require(claim5["topological_restriction_route_complete"] is True, "C5 proof route")
    require(claim5["independent_sparse_graph_readout"]["first_knot_count_meeting_threshold"] == 17, "C5 readout threshold")
    require(claim5["weighted_cycle_continuum"]["final_threshold_passes"] is True, "C5 continuum")
    require(claim5["negative_control"]["discontinuous_target_rejected"] is True, "C5 negative control")
    require(claim6["status"] == "FALSIFIED", "C6 verdict")
    require(claim6["odd_sample_sizes_have_sure_infinite_supremum"] is True, "C6 odd samples")
    require(claim6["even_sample_bad_probability_at_least_half"] is True, "C6 even samples")
    require(claim6["bad_probability_limit"] == "1", "C6 probability limit")
    require(claim6["bounded_offset_control_restores_finite_envelope"] is True, "C6 control")

    branches = published_branches()
    require(branches == EXPECTED_BRANCHES, "published branches")
    require(not any(branch.startswith("orx/") for branch in branches), "legacy orx branch")
    require(int(git("rev-list", "--all", "--count")) == EXPECTED_COMMITS, "reachable commit count")
    identities = git("log", "--all", "--format=%an <%ae>\n%cn <%ce>").splitlines()
    require(identities and all(identity == CANONICAL_IDENTITY for identity in identities), "canonical identity")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    branch_audit = (ROOT / "branch-audit.md").read_text(encoding="utf-8")
    require("STATUS.md" in readme and "CLAIM_EVIDENCE.md" in readme, "README dossier links")
    require("MachineLearning-Nerd@users.noreply.github.com" in readme, "README attribution")
    require("37579156+" not in branch_audit, "stale attribution")

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(branches)} commits={EXPECTED_COMMITS} "
        "claims=C1:C2:C5_verified_scoped,C3:C4:C6_falsified_scoped "
        "historical_score=9/12 current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()
