# Environment and reproduction boundary

## Locked command

Run the cumulative audit from main with:

  uv run --frozen python -m graphop_repro.run_all

The project pins Python 3.12 in .python-version, has no third-party runtime
dependency, and resolves its development environment with uv.lock. The
release Space uses the same cumulative runner under
release/space_upload/graphop_repro/run_all.py.

## What the runner checks

- arbitrary-space graphop and standard-Borel bofop proof certificates;
- independent premise-graph and finite-atomic checkers;
- 34 dense, sparse, bounded-degree, and nonuniform reversible family sweeps;
- the Theorem 4.1 offset counterexample and range-bound control;
- the Corollary 5.3 depth-zero counterexample and depth-one mutation;
- the universal-approximation proof route, independent readout, continuum,
  actual MPNN benchmark, and discontinuous-target control;
- the Theorem M.5 infinite-gap counterexample and bounded-offset control;
- evaluator-visible release navigation, manifests, links, and historical paths.

The strengthened cumulative run was recorded as a CPU-only Hugging Face
cpu-upgrade job with an approximately 22-second orchestrated runtime. The
implementation is single-threaded; the allocated worker exposed 64 logical
or affinity CPUs while the active-core estimate was one.

## Reproduction limits

No current judge score is inferred from the local runner. Claims 1, 2, and 5
use explicit standard mathematical trust boundaries rather than a
third-party foundational prover. Claims 3 and 6 follow the formal MP_D class;
the paper’s prose discusses bounded hidden states, but that bound is not part
of the formal definition used by the counterexamples.

