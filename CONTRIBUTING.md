# Contributing to GoodDollar

**Agents and humans: read this before exploring code, installing dependencies, implementing or submitting work.** Then read the issue and, where present, the target repository's `AGENTS.md` and scoped instructions. If required references are unavailable or instructions conflict, stop and ask a maintainer.

The [latest merged guidelines on GitHub](https://github.com/GoodDollar/.github/blob/master/CONTRIBUTING.md) are the source of truth. GitBook and other entrypoints should link here, not maintain separate rules. Repository instructions add technical requirements; they do not waive these contribution gates.

## 1. Confirm the task, then request assignment

1. **Check ownership.** Read the issue, comments and [bounty board](https://github.com/orgs/GoodDollar/projects/5/views/1). If someone is assigned to the role, do not take it over. Ask whether another role is available.
2. **Check whether work is still needed.** Even if unassigned, search related issues, open and merged PRs, and the current code. Report an existing solution instead of duplicating it.
3. **Understand the deliverable.** Confirm the issue's intent, role, scope, acceptance criteria, design references and required evidence. Implementation, review and QA are different assignments. QA usually requires a human; an agent alone cannot complete required human judgment, exploratory feedback or live wallet testing.
4. **Apply in the issue.** Request the specific role. Include the experience, approach, handoff, ETA and other details that the issue asks for. Confirm the reward and [payment rules](https://github.com/GoodDollar/.github/blob/master/PAYMENTS.md) before accepting paid work. Agents must include the acknowledgment below.
5. **Wait for maintainer assignment and agreed scope before implementation or a PR.** Applying, an empty assignee field, silence or an automated suggestion is not permission. Normally, unassigned PRs and submissions are not considered. Maintainers may accept a useful unsolicited solution, but work that bypasses the rules mentioned here are **not eligible for rewards**, even if merged.

No issue for your idea? Use the [OS contribution proposal template](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/OS-Contribution-Proposal.md) in the affected repository. Discuss scope, acceptance and any reward with a maintainer **in the resulting issue comments**, then obtain assignment. A proposal is not authorization;. For an independent product integrating G$, see [GoodBuilders](https://ubi.gd/goodbuilders).

### Agent acknowledgment

Include this in the assignment-request comment, completed on behalf of the responsible human:

> Operator: @handle. Requested role: role. I have read the contribution guidelines and payment rules. I accept the agreed payment structure and payout through the Gardens OS Contributors Pool to the operator's verified G$ wallet. I will wait for assignment and provide all required evidence, including human testing where required.

The operator remains accountable. Disclose agent assistance, use only authorized accounts/actions, and do not infer authority to publish, merge, release, move funds or approve payments from an implementation assignment. Agents receive no separate reward.

## 2. Do the assigned work and record evidence

- Follow the approved scope, plan, repository commands and existing components. Agree material scope, design or reward changes before doing extra work.
- Reproduce the issue where practical and when picking up from pre-existing PR's, make sure to always critically validate the source.
  Add regression coverage and update relevant documentation. Follow repository commit-signing rules and use your verified contributor identity.
- Test the actual result against the issue and design reference, including relevant errors, recovery and desktop/mobile behavior. An assigned agent submission still needs the same evidence report as a human submission.
- Record exact commits/builds, commands, environment, results and evidence. Label code inspection, automated checks, agent interaction and human testing separately. Distinguish **Pass, Fail, Blocked and Not run**; never substitute mock results for required live testing.
- Keep secrets, personal data and sensitive logs out of commits and evidence. Report vulnerabilities through the repository's private security process.
- Post meaningful progress at least every three days and raise blockers promptly. An assignment may be withdrawn after three days without updates or a response.

For independent QA, follow the issue's QA guide and [QA report template](https://github.com/GoodDollar/.github/blob/master/.github/ISSUE_TEMPLATE/GoodBounties-QA-Template.md). Author self-tests are not independent QA. A human must perform required live wallet/service flows; confirm network, scope and test funds in the [support channel](https://t.me/gooddollarbounties/4115) before testing. Keep blocked and unrun cases visible and retest fixes on the new version.

## 3. Open a draft, then pass the review gate

**Open every PR as a draft** using the repository's PR template or the [default checklist](https://github.com/GoodDollar/.github/blob/master/.github/PULL_REQUEST_TEMPLATE.md). Link the assigned issue, plan/design references, acceptance criteria and evidence.

Keep it draft until all of these are complete:

- [ ] The contributor tested the change themselves and supplied proof. A short video is usually the easiest manual-flow evidence to verify.
- [ ] UI/UX matches the reference, with agreed deviations explained.
- [ ] Required automated QA, tests, lint, type checks and builds pass. Failed, blocked or unrun required checks remain gaps to resolve, not passes.
- [ ] UI/UX PRs include **reference-vs-result screenshots and a happy-path video**, covering relevant desktop/mobile behavior.
- [ ] Known limitations, untested areas and follow-ups are stated. Mark non-applicable items with a reason.
- [ ] Maintainers requested Copilot review, it completed, and findings received fixes, questions or evidence-backed counterpoints.
- [ ] The **bounty lead confirmed these checks in the PR**. The lead is assigned to the parent `[Feature]` issue. If there is no lead, ask the maintainer to identify who owns this gate; do not skip it.

Only after that confirmation should the PR become **Ready for review** and reviewers be assigned or maintainer sign-off requested. Focused intermediate review is welcome while draft: state the specific question, alternatives or checkpoint you need help with. It does not imply readiness.

Reply to each review thread with the fix or reasoning; leave resolution of maintainer and automated threads to reviewers/maintainers. Refresh evidence after relevant changes. The contributor, independent reviewer and QA tester must be different people unless review and QA are explicitly posted as one combined role. Maintainers retain merge/release authority.

## 4. Acceptance and payout

Follow the [payment rules](https://github.com/GoodDollar/.github/blob/master/PAYMENTS.md) and the issue's agreed role/reward. Assignment alone does not guarantee payment. Request payout only after the applicable merge/acceptance and approval conditions are met, through the **Gardens OS Contributors Pool**, using the accountable operator's verified G$ wallet. Review or QA participation does not authorize self-approval of a payment.

Keep decisions in the issue/PR. For help, use the [support channel](https://t.me/gooddollarbounties/4115) or ask [@l03tj3](https://github.com/l03tj3) in the related pull-request/issue. Find other task formats in the [template directory](https://github.com/GoodDollar/.github/tree/master/.github/ISSUE_TEMPLATE).
