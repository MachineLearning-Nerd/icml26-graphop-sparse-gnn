# Claim-to-evidence ledger

The six claim contracts under .openresearch/artifacts/claim_N freeze the exact
quantifiers, source anchors, production routes, and controls. The release
pages under release/space_upload/pages/ are the evaluator-facing exposition;
the raw artifacts below are the machine-readable evidence.

| Claim | Paper statement | How the result is produced | Evidence and control | Status |
| --- | --- | --- | --- | --- |
| C1 — graphop axioms | Definition 3.1 characterizes self-adjoint, positivity-preserving graphops. | Prove positivity and self-adjointness for arbitrary symmetric nonnegative kernels, audit the finite atomic criterion, and sweep dense and sparse families. | .openresearch/artifacts/claim_1/general_proof_certificate.json, general_checker_output.json, raw_results.json, negative_control_output.json | VERIFIED_SCOPED, MEDIUM |
| C2 — bounded fibers | Theorem 3.3 gives unique measurable fibers and identifies their essential mass with both operator norms. | Construct the joint measure, extend and disintegrate it on standard Borel spaces, prove uniqueness and norm identities, then check finite and uncountable sparse cases. | .openresearch/artifacts/claim_2/general_proof_certificate.json, general_checker_output.json, raw_results.json, negative_control_output.json | VERIFIED_SCOPED, MEDIUM |
| C3 — uniform output constant | Theorem 4.1 claims an output constant depending only on L, D, and r. | Use a singleton space, fixed input action distance at most 8, and an admissible MPNN offset M; choose M=8C+1 for any proposed C. | .openresearch/artifacts/claim_3/raw_results.json, checker_output.json, negative_control_output.json | FALSIFIED_SCOPED, MEDIUM |
| C4 — strict subset | Corollary 5.3 claims a compact proper subset for every L in N₀. | Instantiate L=0, zero operator, identity signal, and arbitrary probability measure pi; derive Gamma_0=P(H⁰). | .openresearch/artifacts/claim_4/raw_results.json, checker_output.json, negative_control_output.json | FALSIFIED_SCOPED, HIGH |
| C5 — universal approximation | Theorem M.1 claims uniform density of scalar L-layer MPNNs on the realizable quotient. | Independently prove DIDM separation, algebra closure, and Stone–Weierstrass density; corroborate with an L=2 MPNN, independent readout, continuum sweep, and controls. | .openresearch/artifacts/claim_5/general_proof_certificate.json, general_checker_output.json, raw_results.json, negative_control_output.json | VERIFIED_SCOPED, MEDIUM |
| C6 — uniform generalization | Theorem M.5 claims a vanishing uniform empirical-to-statistical risk gap over the formal MP_D class. | Use two singleton inputs and an unrestricted offset M; sample imbalance gives an infinite supremum gap, with the bad-event probability tending to one. | .openresearch/artifacts/claim_6/raw_results.json, checker_output.json, negative_control_output.json | FALSIFIED_SCOPED, MEDIUM |

## Claim 1 production path

The primary certificate starts with an arbitrary probability space and an
admissible symmetric nonnegative kernel. Integral monotonicity proves
positivity; Fubini and symmetry prove self-adjointness. The independent
finite-atomic checker proves, for every positive measure vector and real
matrix, weighted balance is equivalent to self-adjointness and entrywise
nonnegativity is equivalent to positivity preservation. The campaign covers 34
families and 448,593,904 certified operator cells, including an uncountable
two-neighbour circle graphing. Asymmetric and negative-entry controls fail as
intended.

## Claim 2 production path

The general certificate constructs a finite joint measure from the positive
bilinear form, extends it, disintegrates it on standard Borel spaces, proves
uniqueness with a countable generator, and derives both norm identities from
positivity and duality. The finite route reconstructs every atom indicator
fiber. The uncountable circle graphing has measurable singular two-point
fibers of mass one. A countable diagonal operator with unbounded fibers is
retained as a rejected bofop control.

## Claim 3 production path

The formal MP_D definition bounds Lipschitz constants but not initial offsets
or output ranges. On singleton inputs, the selected fixed-dimension model has
L=1 and D=1, while the input action metric is at most 8 and the output gap is
M. Therefore M=8C+1 defeats every finite constant C. Adding an initial-offset
bound rejects the counterexample; the prose’s hidden-state range is recorded
as an interpretation risk rather than silently added to the formal claim.

## Claim 4 production path

The source quantifies over L in N₀. At L=0, choose H⁰=[-1,1]^d, A=0,
f equal to the identity, and arbitrary pi in P(H⁰). The realized measure is
Gamma_0=pi, so the image is the whole probability space, not a strict subset.
The compactness clause is left untouched. Mutating the critical depth to L=1
correctly rejects the same construction.

## Claim 5 production path

The independent route proves recursive DIDM point separation, closure under
algebra operations, and Stone–Weierstrass density without treating Theorem
E.12 or M.1 as premises. It then checks an independently implemented
piecewise-linear readout on 800 rows, a weighted-cycle continuum on 8,193
points, and an actual L=2 MPNN on held-out sparse graph families. The first
independent readout knot count meeting the 0.04 threshold is 17; the
continuum route meets the 0.01 threshold. Removing message passing, shifting
labels, or using a discontinuous target fails.

## Claim 6 production path

Two fixed singleton inputs have equal probability and the same label target.
The formal MPNN family produces outputs 0 and M, so sample imbalance gives an
infinite supremum loss gap for odd sample sizes and at least a half-probability
bad event for even sizes. The bad probability tends to one. Adding a uniform
offset envelope restores a finite loss envelope and is the required control.

## Evidence boundary

Claims 1, 2, and 5 rely on standard measure-theory and functional-analysis
lemmas that are made explicit as trust boundaries, not claimed to be
foundationally formalized. Finite sweeps and learned MPNN measurements
corroborate the proof routes but do not replace their quantified statements.
Claims 3, 4, and 6 are formal counterexamples subject to the stated
formal-versus-prose interpretation boundary.

