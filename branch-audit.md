# Branch audit

This repository was migrated from opaque OpenResearch-generated branch names to descriptive branches. Each clean branch preserves the corresponding proof, counterexample, or release snapshot.

## Mapping

| Former branch | Clean branch | Purpose |
| --- | --- | --- |
| `orx/frozen-baseline-exact-graphop-definition` | `historical/judged-baseline` | Preserve the original exact graphop baseline and judged release lineage. |
| `orx/general-finite-graphop-and-bofop-certificates` | `audit/claims1-2-finite-certificates` | Generalize finite graphop and bofop certificates across dense and sparse families. |
| `orx/general-probability-space-proof-certificates` | `audit/claims1-2-general-proof` | Add arbitrary probability-space and standard-Borel proof certificates. |
| `orx/exact-bounded-fiber-characterization` | `audit/claim2-bounded-fibers` | Characterize unique bounded fibers and exact norms. |
| `orx/theorem-4-1-uniform-constant-counterexample` | `audit/claim3-uniform-constant` | Construct the unbounded-offset Theorem 4.1 counterexample. |
| `orx/corollary-5-3-l-zero-counterexample` | `audit/claim4-depth-zero` | Falsify the strict-subset clause at depth zero. |
| `orx/universal-approximation-proof-reconstruction` | `audit/claim5-proof-reconstruction` | Reconstruct the universal-approximation proof route. |
| `orx/constructive-mpnn-universal-approximation-eviden` | `audit/claim5-mpnn-approximation` | Add the actual sparse-graph MPNN, independent readout, continuum, and controls. |
| `orx/formal-mpnn-uniform-generalization-counterexampl` | `audit/claim6-generalization-counterexample` | Falsify uniform generalization with the exact infinite-gap event. |
| `orx/evaluator-visible-strengthened-evidence-candidat` | `release/strengthened-evidence` | Preserve the 9/12 judged revision with strengthened evidence. |
| `orx/evaluator-visible-release-candidate` | `release/evaluator-candidate` | Preserve the earlier evaluator-visible six-claim release. |
| `orx/evaluator-visible-general-proof-release` | `release/general-proof-candidate` | Package the arbitrary-space proof release and blind-review materials. |
| `orx/final-general-proof-publication` | `release/final-publication` | Freeze final publication metadata before the current cumulative main. |
| `main` | `main` | Cumulative publication surface. |

## Migration guarantees

- All former `orx/*` remote branches were deleted after their clean replacements were pushed.
- Every live branch contains this file and the claim-focused README.
- Branch tips and historical commits are normalized to `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`.
- The renamed repository is [`MachineLearning-Nerd/icml26-graphop-sparse-gnn`](https://github.com/MachineLearning-Nerd/icml26-graphop-sparse-gnn).
- The historical Hugging Face Space identifier `DineshAI/tRsnpaRO0m` is intentionally retained in evaluator metadata; it is not a GitHub username or branch name.

## Verification checklist

For each clean branch, verify:

```bash
git show-ref --verify "refs/heads/<branch>"
git show "<branch>:README.md" >/dev/null
git show "<branch>:branch-audit.md" >/dev/null
git log "<branch>" --format='%an <%ae>' | sort -u
```

The expected identity is `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`. Scientific status comes from the claim contracts and evidence pages, not from branch names alone.
