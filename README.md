# GoodDollar contribution policies

**Start with [CONTRIBUTING.md](CONTRIBUTING.md), whether you are an agent or a human.**

This repository is the source for GoodDollar contribution rules, [payments](PAYMENTS.md), [issue templates](.github/ISSUE_TEMPLATE) and the [PR checklist](.github/PULL_REQUEST_TEMPLATE.md). Use the latest merged `master` versions when linking from other repositories or GitBook. Repository-specific instructions cover setup and technical requirements, not separate copies of these policies.

## Rollout

This change prepares the central policy and entrypoints. It does **not** update other repositories or GitBook.

GitHub displays supported default community files for repositories without local overrides, but [does not include them in clones](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file). `AGENTS.md`, `CLAUDE.md` and `GEMINI.md` are not inherited community files. Adding them here only helps agents in this repository; each participating repository needs a local entrypoint.

After reviewing this change:

1. Recheck [PAYMENTS.md](PAYMENTS.md) against the live policy with the payment owner. Merge the approved canonical files before directing contributors to new `master` paths.
2. Put the following block **at the top** of each participating repository's root `AGENTS.md`, preserving its technical instructions:

   ```md
   ## Read before project work

   Before exploring code, installing dependencies or making changes, read the
   [latest GoodDollar contribution guidelines](https://github.com/GoodDollar/.github/blob/master/CONTRIBUTING.md)
   and follow their assignment, payment, evidence and draft/review gates.
   Then read this repository's instructions and the assigned issue.
   If you cannot retrieve required instructions, stop and ask for the missing input.
   ```

3. Add a prominent README link for humans. Where present, link local `CONTRIBUTING.md`, `CLAUDE.md`, `GEMINI.md` and `.github/copilot-instructions.md` to the root `AGENTS.md` and canonical guidelines. Do not duplicate the policy. Use `../AGENTS.md` from `.github/copilot-instructions.md`.
4. Reconcile local PR/issue templates with the central gates. A repository's own issue templates/config override the entire default issue-template directory. Include the OS proposal template locally when needed; central storage alone will not make it appear in that repository's chooser.
5. Replace duplicated contribution/payment/checklist rules in GitBook with links to the corresponding `master` files. Keep explanatory material only where it does not create competing rules. Suggested contribution-page replacement:

   > The current [GoodDollar contribution guidelines](https://github.com/GoodDollar/.github/blob/master/CONTRIBUTING.md), [payment rules](https://github.com/GoodDollar/.github/blob/master/PAYMENTS.md) and [PR checklist](https://github.com/GoodDollar/.github/blob/master/.github/PULL_REQUEST_TEMPLATE.md) are maintained on GitHub. Agents and humans must read them before starting work.

6. Verify a fresh clone's agent entrypoints, the issue chooser and PR template in each repository. Confirm GitBook links resolve after merge. Keep rollout changes in their own repository reviews.

Local entrypoints make the rules discoverable; they cannot guarantee that every agent harness will read or obey them.
