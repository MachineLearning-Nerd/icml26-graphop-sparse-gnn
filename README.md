# A Graphop Analysis of Graph Neural Networks on Sparse Graphs

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-graphop-sparse-gnn/blob/main/notebooks/graphop_claims.py)

Independent claim-by-claim reproduction audit for [*A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation*](https://arxiv.org/abs/2602.08785), by Ofek Amran, Tom Gilat, and Ron Levie. This repository is an audit and reproduction workspace; it is not the authors' official implementation.

## Paper in one paragraph

The paper develops a graphop-based framework for studying message-passing graph neural networks on both dense and sparse graphs of unbounded size. It uses a compact metric space of graph inputs to analyze MPNN continuity, universal approximation, and generalization, extending graph-limit ideas beyond uniformly bounded sparse graphs.

## Audit headline

The latest evaluator-visible revision is scored **9/12**: Claims 1, 2, and 5 received toy or rigorous credit, while Claims 3, 4, and 6 were accepted as full-credit falsifications. The independent audit records **three verified and three falsified claims**. It added arbitrary probability-space proof certificates, an uncountable singular sparse graphing, an independent Stone–Weierstrass route, an actual sparse-graph MPNN benchmark, and exact counterexamples. The current score and the 9–12 forecast are historical evidence, not a new live judge result.

The standardized dossier is available in [STATUS.md](STATUS.md),
[CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md), [SOURCE_AUDIT.md](SOURCE_AUDIT.md),
[ENVIRONMENT.md](ENVIRONMENT.md), and [REPORT.md](REPORT.md). The historical
9/12 result remains separate from the local audit, and no new score or author
endorsement is claimed.

## Claim and evidence ledger

| Claim | Paper result | Reproduction assessment | How the result is produced |
| --- | --- | --- | --- |
| 1 | Definition 3.1: graphops are self-adjoint, positivity-preserving operators, covering dense kernels and sparse adjacency | **VERIFIED** | Derive arbitrary-space Fubini/positivity certificates, a singular two-neighbour circle graphing, finite detailed-balance characterizations, and 34 dense/sparse family checks. |
| 2 | Theorem 3.3: bofops have unique measurable fibers with bounded essential mass and matching operator norms | **VERIFIED** | Reconstruct extension, disintegration, uniqueness, and norm arguments on standard Borel spaces; independently check finite fibers and an unbounded-fiber control. |
| 3 | Theorem 4.1: the output constant depends only on `L`, `D`, and `r` | **FALSIFIED** | On singleton spaces, keep the input action distance fixed while an unconstrained value-at-zero offset `M` makes the output gap arbitrarily large. |
| 4 | Corollary 5.3: `Gamma_L(BF_d^r)` is a compact strict subset of `P(H^L)` for every `L`, including `L=0` | **FALSIFIED** | At `L=0`, choose `Omega=H^0`, `mu=pi`, `A=0`, and `f=id`; then `Gamma_0=pi` for every probability measure. |
| 5 | Theorem M.1: MPNNs uniformly approximate every continuous target on the realizable bofop-DIDM quotient | **VERIFIED** | Prove DIDM separation by induction, algebra closure, and Stone–Weierstrass without assuming E.12/M.1; corroborate with an actual two-layer MPNN, independent readout, and weighted-cycle continuum. |
| 6 | Section 6.2/Theorem M.5: uniform empirical-to-statistical risk gaps vanish for the formal `MP_D` class | **FALSIFIED** | A fixed two-point distribution and unbounded admissible offsets make the supremum gap infinite whenever the sample is imbalanced; the bad-event probability tends to one. |

The exact contracts, source audits, raw outputs, proof kernels, controls, and limitations are under [`release/space_upload/evidence/`](release/space_upload/evidence/). The illustrated explanation is [`reports/reproduction/report.md`](reports/reproduction/report.md), and the evaluator-visible current pages are under [`release/space_upload/pages/`](release/space_upload/pages/).

## How each claim is produced

Every claim follows one auditable path:

1. Anchor the statement to the paper definition, theorem, or corollary and freeze its quantifiers in `claim_contract.json`.
2. Record source hashes, mathematical trust boundaries, deviations, and limitations in `source_audit.md` and `limitations.md`.
3. Implement the primary proof, construction, counterexample, or benchmark in `graphop_repro/`.
4. Run an independent checker and an assumption-breaking negative control; preserve exact JSON results and commands.
5. Publish the cumulative status through the release Space source, manifests, and the illustrated report.

Universal claims are supported by symbolic derivations or explicit counterexamples. Finite sweeps and the held-out MPNN experiment are corroboration, not substitutes for the quantified theory. The proof kernels explicitly expose their standard measure-theory and functional-analysis trust boundaries rather than presenting them as foundationally formalized.

## Repository contents

- [`graphop_repro/`](graphop_repro/) — claim implementations, proof kernels, and independent checkers.
- [`reports/reproduction/report.md`](reports/reproduction/report.md) — technical report with equations, evidence, and limits.
- [`notebooks/graphop_claims.py`](notebooks/graphop_claims.py) — self-contained tutorial notebook.
- [`release/space_upload/`](release/space_upload/) — evaluator-visible Space source, evidence pages, release code, and manifests.
- [`candidate/`](candidate/) — compact candidate pages used during release review.
- [`release/validate_candidate.py`](release/validate_candidate.py) — release-surface validator.
- [`branch-audit.md`](branch-audit.md) — old-to-clean branch lineage and migration record.

## Reproduce locally

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
uv sync --frozen
uv run --frozen python -m graphop_repro.run_all
```

The runner executes one primary verifier and one independent checker per claim. It exits nonzero when a certificate, exact result, source obligation, or negative control fails. The environment is Python 3.12 with no third-party runtime dependency; formal strengthened jobs used Hugging Face `cpu-upgrade` but the verifier itself is single-threaded.

## Branch map

`main` is the cumulative publication surface. Focused branches preserve the proof and evidence lineage with descriptive names; the complete mapping from the former `orx/*` names is in [`branch-audit.md`](branch-audit.md).

| Clean branch | Purpose | Status |
| --- | --- | --- |
| [`historical/judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/historical/judged-baseline) | Preserve the original exact graphop baseline and judged release lineage | Historical record |
| [`audit/claims1-2-finite-certificates`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claims1-2-finite-certificates) | Generalize the finite graphop/bofop certificates across dense and sparse families | Claims 1–2 evidence |
| [`audit/claims1-2-general-proof`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claims1-2-general-proof) | Add arbitrary-space and standard-Borel proof certificates | Claims 1–2 strengthened |
| [`audit/claim2-bounded-fibers`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claim2-bounded-fibers) | Characterize unique bounded fibers and exact norms | Claim 2 audit |
| [`audit/claim3-uniform-constant`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claim3-uniform-constant) | Construct the unbounded-offset Theorem 4.1 counterexample | Claim 3 falsified |
| [`audit/claim4-depth-zero`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claim4-depth-zero) | Falsify the strict-subset clause at `L=0` | Claim 4 falsified |
| [`audit/claim5-proof-reconstruction`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claim5-proof-reconstruction) | Reconstruct the universal-approximation proof route | Claim 5 evidence |
| [`audit/claim5-mpnn-approximation`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claim5-mpnn-approximation) | Add the actual sparse-graph MPNN, independent readout, continuum, and controls | Claim 5 verified |
| [`audit/claim6-generalization-counterexample`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/audit/claim6-generalization-counterexample) | Falsify uniform generalization with an exact infinite-gap event | Claim 6 falsified |
| [`release/strengthened-evidence`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/release/strengthened-evidence) | Preserve the 9/12 judged revision with strengthened evidence | Historical release |
| [`release/evaluator-candidate`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/release/evaluator-candidate) | Preserve the earlier evaluator-visible six-claim release | Historical candidate |
| [`release/general-proof-candidate`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/release/general-proof-candidate) | Package the arbitrary-space proof release and blind-review materials | Candidate release |
| [`release/final-publication`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn/tree/release/final-publication) | Freeze final publication metadata before the current cumulative main | Publication history |

## Citation

If this audit or its evidence package is useful, please cite the paper:

```bibtex
@misc{amran2026graphop,
  title        = {A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation},
  author       = {Amran, Ofek and Gilat, Tom and Levie, Ron},
  year         = {2026},
  eprint       = {2602.08785},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url          = {https://arxiv.org/abs/2602.08785}
}
```

## Thank you

Thank you to Ofek Amran, Tom Gilat, and Ron Levie for developing a framework that makes the dense-versus-sparse graph question concrete enough to audit. This reproduction is intended as a respectful, transparent record: it preserves the paper's scope, distinguishes proof-level evidence from finite experiments, exposes trust boundaries, and reports counterexamples without hiding the remaining interpretation risks.

## Attribution and scope

The repository is maintained by [MachineLearning-Nerd](https://github.com/MachineLearning-Nerd). The normalized commit identity is `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`. The original repository slug was `icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization`; it was renamed to `icml26-graphop-sparse-gnn`. The evaluator's historical [DineshAI/tRsnpaRO0m Space](https://huggingface.co/spaces/DineshAI/tRsnpaRO0m) remains referenced by protected release metadata and is intentionally not renamed by this GitHub cleanup.
