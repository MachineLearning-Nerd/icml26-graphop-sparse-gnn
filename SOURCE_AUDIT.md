# Source audit entry point

## Primary source

- Paper: *A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation*
- Authors: Ofek Amran, Tom Gilat, and Ron Levie
- arXiv: [2602.08785](https://arxiv.org/abs/2602.08785)
- HTML source: https://ar5iv.labs.arxiv.org/html/2602.08785
- Retrieved: 2026-07-28 17:44:40 UTC
- Version: arXiv:2602.08785v1, 9 February 2026
- HTML SHA-256: ae8d8f620023d94024494817d799bbd52617d2dd0eca282e29a8cab00e2dc3ca

The full source audit is preserved in
.openresearch/artifacts/source/paper_source_audit.md and mirrored under the
release evidence package.

## Claim anchors and quantifiers

- C1: HTML anchor #S3.Thmtheorem1, Definition 3.1. A graphop is
  self-adjoint and positivity-preserving as an operator from L-infinity to
  L1 over a Borel probability space.
- C2: HTML anchor #S3.Thmtheorem3, Theorem 3.3. A bofop has a unique
  measurable fiber family; its essential fiber mass equals both operator norms.
  The converse additionally assumes symmetry.
- C3: HTML anchor #S4.Thmtheorem1, Theorem 4.1. The output constant is claimed
  to depend only on L, D, and r for inputs in BF_d^r and models in MP_D.
- C4: HTML anchor #S5.Thmtheorem3, Corollary 5.3. Compactness and properness
  are quantified for every L in N₀ and r>0.
- C5: HTML anchor #A13.Thmtheorem1, Theorem M.1. Scalar L-layer MPNNs are
  claimed uniformly dense on the order-L bofop-DIDM quotient.
- C6: HTML anchor #A13.Thmtheorem5, Theorem M.5. A simultaneous
  empirical-to-statistical bound is claimed for every confidence parameter
  and arbitrary data probability measure.

The imported judge summary labels the C2 fiber statement as Definition 3.1;
the paper source places it in Theorem 3.3. This audit uses the source anchor.

## Fidelity boundary

The current release improves Claims 1, 2, and 5 beyond the finite-only
historical evidence that earned toy credit. It still exposes the
Fubini/disintegration/Riesz/Stone–Weierstrass trust boundaries. The 9/12
revision, the earlier 8/12 revision, and the rejected baseline remain
archived under release/space_upload/historical.

