# Contributing to GoodDollar

GoodDollar builds open-source tools for universal basic income and the G$ ecosystem. Developers, reviewers, testers, designers and documentation contributors are welcome, including those using coding agents.

These rules apply to humans and agents. Read them alongside the target repository's instructions.

## Before implementation

1. Read the issue, specification, design references and discussion. Read the repository's `AGENTS.md` where present, linked development instructions and instructions scoped to the files you will change. Check agent-specific files explicitly; tools may not load them automatically.
2. Search existing issues and pull requests for related work.
3. For an existing issue, request assignment. For a new idea or bug, open an issue describing the problem, evidence and proposed outcome. Include reproduction steps for bugs and links to related work.
4. Wait for a maintainer to confirm the scope and either assign the work or explicitly authorize you to proceed in the linked issue or discussion. Obtain this confirmation before implementation or opening a pull request.

Creating an issue, requesting assignment or receiving no objection is not approval. Neither an available issue nor an automated recommendation grants an assignment. This gate also applies to work found through repository scans or agent suggestions.
For eligibility for any rewards out of our Contributors program its required to follow these rules.

Not following these instructions and automated pull-requests might still be accepted but will not be part of the rewards program.

For maintainer decisions, use the assigned contact or ask **[@l03tj3](https://github.com/l03tj3), [@sirpy](https://github.com/sirpy) or [@blueogin](https://github.com/blueogin)**.

## Contribution paths

- **Existing GoodBounty:** Browse the [GoodBounties board](https://github.com/orgs/GoodDollar/projects/5/views/1). Check the issue's status, available role, requirements and reward. Apply in the issue with relevant experience, your understanding of the task and an estimated completion time. Wait for assignment before starting paid work.
- **Proposed improvement or bug fix:** Follow the issue proposal step above. A maintainer determines priority, scope and contribution route. A proposal does not automatically become a funded bounty; confirm any paid role and reward before undertaking paid work.
- **Maintainer-led work or follow-up:** A maintainer may prepare a fix, request review of internal work or commission QA without a full bounty-lead sequence. Record the required deliverables, accountable people, acceptance criteria and any agreed payment in the issue.
- **Independent project:** For a product integrating G$, see [GoodBuilders](https://ubi.gd/goodbuilders). For an independent open-source proposal, use the [Open Contributors discussion](https://discourse.gooddollar.org/t/welcome-to-the-gooddollar-development-category/8241) and [proposal template](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/OS-Contribution-Proposal.md).

Follow the task's agreed roles, deliverables and acceptance conditions. Deliverables may include implementation, independent review, QA or another defined outcome. An AI-generated implementation, a separate external bounty lead and every possible bounty role are not required for every task.

## Scope and planning

- Use the repository's documented setup, package manager, build and test commands, and contribution conventions.
- If instructions conflict, a required link is unavailable or expected behavior is unclear, ask a maintainer before continuing the affected work.
- Prepare and agree a plan before implementation when the task requires investigation, design choices or cross-repository coordination. Include the approach, affected components, risks and verification. Otherwise, follow the scoped issue unless the issue or repository requires a separate plan.
- Keep unrelated refactoring and newly discovered features in separate proposals. Confirm material changes to scope, approach or reward before doing the extra work.

## Roles and accountability

Record the roles needed for the task in the issue:

- **Lead:** Clarifies scope and acceptance criteria, coordinates work and records acceptance or gaps. A maintainer may fill this role.
- **Contributor:** Implements the change, supplies self-test evidence and documentation, and responds to review.
- **Reviewer:** Independently checks the implementation, risks and evidence; records actionable findings and a review decision.
- **QA tester:** Independently executes requested user flows and exploratory checks, records observations and retests fixes.
- **Maintainer:** Confirms scope and assignments, resolves outstanding decisions and retains final merge and release authority.

Within a bounty workstream, different people must perform the contributor, reviewer and QA roles when those roles are required. Author self-tests are required evidence, but do not count as independent review or QA.

## Implementation and verification

- Reproduce the problem where practical and understand the affected user flow. Check intended behavior against the request and design references, not only existing code.
- Reuse existing components, connectors, helpers and the design system. Explain justified departures.
- Match supplied designs in layout, structure, emphasis and behavior. For UI changes, verify desktop and mobile layouts and usable contrast. Record missing design input or agreed deviations.
- Add or update behavior and regression tests. Run the repository's linting, type checking and build checks.
- Report failed checks and their relationship to the change. To claim a failure also occurs on the base branch, provide evidence from that branch or link an existing report.
- Update documentation, examples or stories when behavior or configuration changes.
- Follow repository commit-signing requirements and use your own verified contributor identity. See [GitHub's commit signature guidance](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).
- Keep credentials, private keys, personal data and sensitive logs out of commits and public evidence. Use the repository's private security-reporting process for vulnerabilities.

## Pull requests and review

Use the repository's PR template. Include:

- The approved issue or discussion, scope, specification and design links.
- A concise change summary and important implementation decisions.
- Acceptance criteria and evidence for each completed item.
- Exact test commands, outcomes and CI links. List failures, blocked checks and unrun checks separately.
- Screenshots or a short recording of relevant desktop and mobile behavior for UI changes.
- Documentation or configuration changes, limitations and follow-ups.
- Agent assistance and the responsible human operator, where applicable.

Report only actions performed and results observed. Distinguish code inspection, automated checks, agent-operated interactions and human testing. Include enough context for reviewers without relying on a private agent conversation.

Keep the PR focused on the approved scope. Request the assigned reviewer through GitHub where permitted; otherwise ask in the issue or support channel. For automated findings, reproduce or explain the finding, then fix it or provide evidence for leaving it unchanged.

Reply to review threads with the change made or the reason for not changing it. Leave resolution of maintainer and automated review threads to reviewers or maintainers. Update evidence when changes affect earlier test or review results. Request an in-progress review if the change grows beyond the expected scope.

## Additional rules for agents

The human operator remains accountable for the work, its accuracy and compliance with the assignment.

- Identify the operator and assigned role in the issue or PR, and disclose agent assistance.
- Use only accounts, access and actions authorized by the operator and task. Publish on the operator's behalf only when the operator has authorized publication.
- Do not infer merge, release, payment-approval or production-administration authority from an implementation assignment.
- Report blockers and uncertainty. Do not describe blocked or unrun checks as successful.
- Include actual human work when the task requires independent human judgment, exploratory feedback or live human QA. Automated reports and simulated interactions do not replace it.

## Independent QA and live testing

For assigned QA, read the task's QA request and repository QA guide. The request should identify the change, environments, user flows, design references, evidence and acceptance conditions. Follow these task instructions as well as the report template.

When the task requires live testing:

1. A human must connect the requested wallet or service and execute the real flow in the agreed environment.
2. At the start, contact the [GoodBounties Telegram channel](https://t.me/gooddollarbounties/4115) to confirm network and scope and request test funds where needed.
3. Record funding or access blockers. Do not substitute mock results for live testing.

For QA execution and reporting:

- Explore realistic navigation, errors, recovery and the wallet or device combinations in the request. Compare against design references and provide evidence of UI regressions.
- Use fixtures, scripts and automated tests for diagnosis and regression checks. Keep those results separate from live and exploratory human observations.
- Use the [reusable QA report](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/GoodBounties-QA-Template.md). Record exact commits and package or build versions, the executor of each check, environment and evidence.
- Use **Pass**, **Fail**, **Blocked** and **Not run** accurately. Keep required gaps visible. Record any exception as an explicit decision with a follow-up owner, not as a Pass.
- Separate author self-tests from independent QA. Record fixes and retests against their new versions.
- Ensure the accountable lead and maintainer record the required decisions before treating a QA recommendation as acceptance.

## Rewards and payment requests

Read the current [payments policy](https://docs.gooddollar.org/for-developers/contributing/open-source-contributors/payments-for-reviews-contributors-and-qa) before accepting a paid role. Follow its tiers, applicable role shares, accepted-bug bonuses, payment conditions and request process.

- Record the agreed role, scope, tier or standalone reward in the issue. Resolve unclear or conflicting terms with a maintainer before starting paid work.
- Do not infer a standalone review or QA reward from an unrelated full bounty. Extra time, unsolicited PRs and unapproved scope increases do not change the agreed reward by themselves. Work without agreed scope or assignment does not establish payment eligibility.
- The human operator is the accountable payment recipient and requester. Agent-prepared or agent-submitted requests remain on that person's behalf, using their verified identity and G$ wallet. Agents do not receive separate rewards.
- After the applicable acceptance and approval conditions are met, follow the linked payment process. Include the issue, PR or report, agreed role and reward, and verified payout address. Check current community membership and proposal requirements before submitting.
- Review or QA participation does not authorize approval of one's own payment.

## Progress and coordination

Post a meaningful progress update at least every three days while assigned. Raise blockers promptly and state the help needed. An assignment may be withdrawn after three days without updates or a response.

Use the relevant issue or PR and the [GoodBounties Telegram channel](https://t.me/gooddollarbounties/4115) for questions, blockers, assignment and review coordination. Keep agreed decisions linked from the issue.

## Templates and further guidance

Use the current template for the deliverable and any applicable repository-specific template:

- [Central issue templates](https://github.com/GoodDollar/.github/tree/master/.github/ISSUE_TEMPLATE)
- [Contributor bounty request](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/contributor-bounty-template.md)
- [Feature request](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/FEATURE_REQUEST.yml)
- [Bug report](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/BUG_REPORT.md)
- [Agent bug report](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/AGENT_BUG_TEMPLATE.yml)
- [QA report](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/GoodBounties-QA-Template.md)
- [Open-source contribution proposal](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/OS-Contribution-Proposal.md)
- [Reviewer role](https://docs.gooddollar.org/for-developers/contributing/open-source-contributors/human-reviewer-role)
- [QA role](https://docs.gooddollar.org/for-developers/contributing/open-source-contributors/qa-role)
- [Contributor growth path](https://docs.gooddollar.org/for-developers/contributing/open-source-contributors/contributor-growth-path)
