# Data ownership and documentation

Dora (GitHub: `chinchillad-ux`) prepared the synthetic data and draft section.
The proposal records eight repairs across six houses, three contractors, and
one week. Dora's draft uses
40 base repairs across 20 houses and introduces overtime and priority-based
deferral. Confirm scope and schema with the team before using these inputs in
the model. [Scope](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues/7)
· [Overtime](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues/8)
· [Priority](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues/9)
· [Schema](https://github.com/JoshuaKosakowsky/rental-maintenance-optimization/issues/13)

## Draft files

- [40-job base workbook](base/rental_maintenance_data_40_jobs.xlsx) contains 40 base jobs and two urgent additions.
- [Contractor C unavailable workbook](scenarios/rental_maintenance_contractor_C_unavailable.xlsx) changes C's regular and overtime hours to zero.
- Dora's [problem, data, and assumptions draft](../reports/sections/Rental_Maintenance_Problem_and_Data_draft.docx) explains the assumptions and their rationale.

## Workbook schema

| Worksheet | Keys and units |
| --- | --- |
| Jobs | `Job` identifies a repair and `House` groups repairs by synthetic property. `Hours` is labor hours per job. `BaseJob` and `CanDefer` are 1 for yes and 0 for no. `DeferralPenalty` is dollars per deferred job. |
| Contractors | `Contractor` identifies a company. `RegularHours` and `MaxOvertime` are company labor hours per week. `OvertimeSurcharge` is additional dollars per overtime hour. |
| Quotes | `Job` and `Contractor` reference their respective sheets and jointly identify an eligible assignment. `Cost` is dollars per completed job, including normal labor and materials. An absent pair means the assignment is ineligible. |
| Notes | Scenario instructions, units, and rationale for the synthetic durations, prices, capacity, and penalties. |

The structured sheets have headers in row 1 and one record per subsequent row.
The supplied rows contain values for every field. `CanDefer = 0` requires
completion even when the penalty is zero. Use `BaseJob = 1` to select the 40 jobs
for the base and C-unavailable comparisons. The added-repair scenario uses the
base workbook with J41 and J42 included.

Keep all public data synthetic and omit tenant names, addresses, contact
details, and credentials.
