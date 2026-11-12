# Reviewer setup status

The owner requested JoshKozy as a fully AI reviewer with eligible merge authority,
matching the role in the public
[Operations Tracking reference](https://github.com/JoshuaKosakowsky/Operations-Tracking-Application/blob/main/docs/HERMES_REVIEWER.md).
The [policy for this repository](ai-reviewer.md) governs the new role.

## Account and enforcement

JoshKozy requires accepted collaborator Write access for eligible reviews/merges
in the reference arrangement. Write access is not a technical prohibition on
editing branches; the separately restricted reviewer broker must expose only
review/read/merge tools. Main protections provide an additional server-side gate.
See `repository-setup.md` for observed invitation and protection state.

## Windows operator setup remains to be verified

The referenced `operations-reviewer` profile and its broker are configured for
the other repository. This setup task does not modify Joshua's Windows machine,
reuse its repository allowlist blindly, or claim that its runtime now supports
this project. Cloning this repo does not install or launch an AI agent.

On the Windows PC, an authorized operator must:

1. Accept the collaborator invitation while signed in as JoshKozy.
2. Configure a dedicated or explicitly scoped reviewer connection for
   `JoshuaKosakowsky/rental-maintenance-optimization`, using this repo's policy.
3. Verify only the six equivalent read/review/merge capabilities are exposed and
   that file edits, terminal execution, credential fallback, and pushes are denied.
4. Verify identity/repository access and read-only inspection of current main/PRs.
5. Exercise an eligible review through a real ready PR, without self-approval or
   bypassing main protections; record the actual evidence and any limitations.

Do not copy broker credentials, OS-keyring state, provider sessions, or private
Windows files into this public repository. The coding identity remains
JoshuaKosakowsky; no coding session may impersonate the reviewer.
