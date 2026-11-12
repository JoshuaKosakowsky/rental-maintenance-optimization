# Data ownership and documentation

Dora leads the project data. The approved scope is eight repair jobs across six
rental houses and three contractors for one week, using justified synthetic data.
No project dataset has been created yet.

Store the agreed base tables in `base/` and explicit scenario changes in
`scenarios/`. Document each table's identifier columns, units, relationships,
missing-value rules, parameter sources, and synthetic-value rationale here.

The model needs repair requirements, contractor qualifications and available
hours, and assignment costs/hours. Agree on the schema with Josh and Izzy before
creating it. Do not invent costs, hours, qualifications, or identifiers merely
to make the model feasible. Keep all public data synthetic; never use tenant
names, addresses, contact details, or credentials.

Required alternatives: one specified contractor unavailable; two additional
required repairs. Identify the selected contractor and added repairs explicitly.
