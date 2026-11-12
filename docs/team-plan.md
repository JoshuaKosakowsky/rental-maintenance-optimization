# Team plan

This preserves the proposal's roles and dates. The team readiness target is
December 3, 2026; the course deadline is December 10, 2026. Live task status belongs
in [GitHub Issues](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues)
and the [Project](https://github.com/users/JoshuaKosakowsky/projects/3).

## Responsibilities

| Member | Responsibility and deliverables |
| --- | --- |
| Dora | Explain the problem; create and justify repairs/contractors/costs/hours/skills/availability data; write problem/data/assumptions; organize recording |
| Josh | Define decisions/objective/constraints; hand-check a small example; help Izzy debug; independently verify outputs; write model/verification |
| Izzy | Implement Python/Gurobi model; run benchmark/base/scenarios; provide assignment/cost tables; write numerical results and README |
| Anete | Write recommendations/limitations; format results; combine completed report sections; assemble submission and everyone's AI notes |

Everyone supplies polished writing, their own AI-use notes and recording segment,
and reviews the final report/results/files. Josh and Izzy collaborate on coding
and verification. Anete combines completed sections rather than writing them all.

## Milestones from the proposal

| Due date in 2026 | Milestone | Lead |
| --- | --- | --- |
| [November 13](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/1) | Agree on scope, assumptions and roles; confirm Track A recording | Everyone |
| [November 17](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/2) | Complete data tables and first mathematical model | Dora and Josh |
| [November 22](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/3) | Working Python model and independent verification | Izzy and Josh |
| [November 25](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/4) | Benchmark, optimized base case and both scenarios; share results | Izzy with team |
| [November 28](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/5) | Deliver completed written sections to Anete | Everyone |
| [November 30](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/6) | Combined report; review results and recommendations | Anete with team |
| [December 2](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/7) | Finish recording; test README; review full package | Dora coordinates; everyone contributes |
| [December 3](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/milestone/8) | Final edits complete; files ready for submission | Anete with everyone |

December 10 is separately tracked as the course submission deadline. No deadline
time is supplied by the documents. Josh's November 28 Thanksgiving comment remains
open for team review; no milestone has been shifted automatically.

## Experiments

1. Greedy benchmark: fixed job order, cheapest qualified contractor with enough
   remaining hours; report if it cannot complete every job.
2. Optimized base case: same inputs and restrictions; compare costs only for
   equivalent completed workloads.
3. Contractor unavailable: explain reassignments, cost changes, or infeasibility.
4. Two repairs added: explain cost changes, capacity pressure, or infeasibility.
