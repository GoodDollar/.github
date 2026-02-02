# Contributing to GoodDollar

Thank you for your interest in contributing to the GoodDollar initiative.

GoodDollar is a nonprofit protocol building Universal Basic Income (UBI) via the G$ token.
We ship open-source dApps, SDKs, and contracts with the goal of making it easier for anyone to access and use G$.

Everyone is welcome: developers, designers, product builders, and entrepreneurs who want to build practical tools for financial access and inclusion.
We have different paths available to any type of builder to contribute.

# Choose your path

If you’re here, you’re probably fit into one of these modes:

1. **Building or planning a project that integrates G$**
   Check out the ongoing GoodBuilders program (mentorship + funding): [https://ubi.gd/goodbuilders](https://ubi.gd/goodbuilders)
   Questions? Join the GoodBuilders Telegram: [https://ubi.gd/GoodBuildersTG](https://ubi.gd/GoodBuildersTG)

2. **Contributing to GoodDollar repos through bounties**
   That’s the [GoodDollar Bounties program](#gooddollar-bounties-in-90-seconds).

3. **You have your own idea for improvements and want autonomy?**
   Propose your own work via our Gardens Pool for Open Source Contributors:
   [Welcome to GoodDollar development - Discourse Forum](https://discourse.gooddollar.org/t/welcome-to-the-gooddollar-development-category/8241)



## GoodDollar Bounties

GoodDollar Bounties are a lightweight way to contribute to our open-source repos and earn rewards in G$. Pick a task, ship a PR, get it merged, and request payout.

### GoodDollar Bounties in 90 seconds

1. Find a bounty 'Ready-for-assignment' on our [GitHub Bounties Board](https://github.com/orgs/GoodDollar/projects/5/views/1)
2. Get assigned a bounty by commenting on the issue (see [“Claiming & assignment”](#claiming--assignment))
3. Ship work via a PR and link the issue in the description besides your explanation of things fixed/changed/added. (`#123`)
4. Request a review by one of the maintainers using github's 'Request Review' button.
5. Follow up on any of the suggestions/feedback a reviewer gives. This includes going over AI automated reviews.
   
   -- Note: **resolving comments is done by reviewers/maintainers**.
   a contributor only comments on responding to questions, or sharing what has been fixed or why a reviewer might be wrong.
7. Request payout in our [Gardens OS-Contributors Pool](https://app.gardens.fund/gardens/42220/0x62b8b11039fcfe5ab0c56e502b1c372a3d2a9c7a/0xf42c9ca2b10010142e2bac34ebdddb0b82177684/94) (link PR + issue). A more in-depth explanation can be found: <here>.
8. Once approved, payout is processed in G$'s based on the [tier of your bounty](#reward-tiers).

If you get stuck at any point: ask in the bounty support channel (link below). We’d rather answer questions early than review a PR that went sideways.

### Where bounties live

Our bounties are GitHub issues tracked via a GitHub Projects board.

- [Bounties board](https://github.com/orgs/GoodDollar/projects/5/views/1)
- Some Eligible repositories:
  - [https://github.com/GoodDollar/GoodProtocolUI](https://github.com/GoodDollar/GoodProtocolUI)
  - [https://github.com/GoodDollar/GoodSdks](https://github.com/GoodDollar/GoodSdks)
  - [https://github.com/GoodDollar/GoodCollective](https://github.com/GoodDollar/GoodCollective)
  - [https://github.com/GoodDollar/GoodWeb3-Mono](https://github.com/GoodDollar/GoodWeb3-Mono)

- Find issues labeled: `gd-bounty`, and a tier label (Basic/Common/…).

Tip: the board is the source of truth for what’s available. Look in the column “Ready-For-Assignment”.

### Reward tiers

Each bounty issue has a tier. Payouts are in G$.

| Tier      | Reward (USD) |  Reward (G$) |
| --------- | -----------: | -----------: |
| Basic     |          $25 |   250,000 G$ |
| Common    |          $50 |   500,000 G$ |
| Rare      |         $150 | 1,500,000 G$ |
| Epic      |         $250 | 2,500,000 G$ |
| Mythic    |         $350 | 3,500,000 G$ |
| Legendary |         $450 | 4,500,000 G$ |

Note: G$ amounts are calculated using a base price of $0.0001. Market value can fluctuate, and we can’t guarantee the value at the time of distribution.
Tier assignments are mainly based on our estimated 'time to completion', which can be longer depending on your skill-set.
Taking longer to resolve a task does not mean you will be eligible for a higher-tier payment.

### Claiming & assignment

To claim a bounty:

1. Comment on the issue you want (e.g., “I’d like to take this. ETA: 2–3 days.”)
2. A maintainer will assign you (or ask a quick clarifying question)

To keep things fair and moving:

- We usually only allow 1 bounty / 1 contributor at a time. Resolve your pending bounty before requesting to work on a new one.
- Show progress at least every 3 days (draft PRs are perfect).
  Its okay to have a Draft PR and things are maybe still broken, or not 100% resolved. this stage is just so reviewers can verify if things are still moving forward
- If we see no progress and no response for 5 days, we may unassign the issue so others can pick it up.
- If you’re blocked, say so. We’ll help. Silence looks identical to abandonment. Early asks for assistance increases the quality and PR-Review time significantly.

### What “done” means (how to get merged fast)

We review faster when your PR makes verification easy.

During building:

- is it your first time contributing, please read up on the [general rules](#some-general-rules). Does not hurt to revisit this sometimes, we do expect returning contributors to know them.
- Ask questions and raise blockers early on, using the builders-channel on telegram, or issue/PR comment section on github.
- If you notice your PR changeset becomes bigger, ask for a 'in-the-middle' review.
  Large PR's are very difficult to review and adequately find potential bugs/things to refactor or change.
  asking a review while you are still building will reduce overal time for a reviewer to accept your submission.
  During creating a bounty we try to accomodate towards this and might setup 'milestone' deliverables.

In your PR description:

- Link the issue you solved (use `#issue-number`)
- Explain what you changed and why
- Include screenshots/video for UX changes (desktop + mobile responsiveness)
- Include testing notes (how you verified, steps to reproduce, etc.)
- Keep scope tight: one PR should solve one issue

During review:

- Respond promptly to feedback
- Don’t resolve maintainer comments yourself (reply with what you changed, or why you disagree)
- Ensure builds pass and formatting/linting matches the repo defaults

### How payout works (Scout Game replacement flow)

Scout Game (the external platform) has been sunset. We now process bounty payouts through our Gardens Pool.

After your PR is merged:

1. Create a payout request in our Gardens Pool: <need a notion page with explanation>
2. Include:
   - PR link
   - Issue link
   - Tier (Basic/Common/…)
   - Your payout address
   - Any notes needed for verification

3. A maintainer/committee member verifies the merge + tier and approves the payout.

We strongly recommend you join the bounty channel so you can see current payout cadence and any updates to the process.

### Support & updates

- [Bounty support channel (bounty updates, questions, blockers, review help)](https://t.me/gooddollarbounties/4115)
- GoodBuilders general builders channel: [https://ubi.gd/GoodBuildersTG](https://ubi.gd/GoodBuildersTG)
- Docs: [https://docs.gooddollar.org](https://docs.gooddollar.org)

## General contribution guidelines (applies to all contributors)

Notes:

1. GoodDollar is split across multiple repositories: [https://github.com/GoodDollar](https://github.com/GoodDollar)
2. Please use our issue and PR templates:

- Issues: `./.github/ISSUE_TEMPLATE`
- PRs: `./.github/PULL_REQUEST_TEMPLATE`

### Getting started

1. Fork and clone the repository
2. Create a feature branch
3. Make changes following existing patterns
4. Test thoroughly using demo apps
5. Submit a PR with a clear description

### Issues

Feature requests, bug reports, docs improvements, and other contributions are welcome. Issues are triaged based on maintainer prioritization and best effort.

### Pull requests

We follow the GitHub flow: [https://guides.github.com/introduction/flow/](https://guides.github.com/introduction/flow/)

### Some general rules

- We expect that after being assigned, we will see progress happening. Show some progress at least once a week. This can be done through draft pr's.
- We will try to reach out and follow up if we don't see progress. But if, after seeing no progress and no response to feedback, we will unassign someone after 5 days of no response.
- Don't resolve comments generated by either AI or one of the maintainers. Just comment you have done the requested change, or explain why the maintainer or AI might be wrong.

1. Understand the Repositories:
   - Familiarize yourself with the architecture and functionality of the repository from which you take an issue.
   - Read existing code to understand structure and best practices. Always try to follow similar patterns / re-use existing helper methods.
   - If UI, verify if there are existing components you can utilize, and make sure your addition fits into existing design.

2. Select and Understand the Issue:
   - Review the reported issue carefully to ensure clear understanding.
   - Clarify any uncertainties by asking detailed questions—don't hesitate to seek guidance.
   - Ask, Ask, And Ask again

3. Fork and Clone:
   - Fork the repository.

4. Reproduce the Issue:
   - Run the existing codebase and reproduce the behavior or issue reported.

5. Prepare and Learn:
   - If the coding language or technology is new, complete a brief introductory course to familiarize yourself.

6. Implement Your Solution:
   - Develop your solution based on the issue's requirements.
   - While we don't enforce strict rules, we kindly expect adherence to the default principles of the frameworks and languages in use.
   - Seamlessly integrate your solution into the larger codebase—if existing code can be utilized, please do so!
   - For UI components: If no UI is provided, feel free to craft your own design, keeping in mind essential UI/UX principles.
   - If you're unsure about any part of the process, implementation, or a decision to make, we're here and more than happy to guide you.

7. Documentation and Examples:
   - Provide clear documentation and, if applicable, relevant examples or demonstrations of your solution.

8. Submit Your Pull Request (PR):
   - Clearly mention the issue in your PR and describe your solution thoroughly to facilitate quicker reviews.
   - Make sure to add the '#' reference to exact issue.
   - If a new feature involving UX/UI is added, show a demo video, or screens. Most of our apps are usable on both desktop/mobile, so make sure they are responsive.
   - Respond promptly to feedback from maintainers and incorporate requested changes.
   - Make sure there are no build errors and typings are applied correctly (most of our projects use TypeScript). Utilize existing linting configuration like prettier and eslint.
     - If using VSCode, you can for example use the [esbenp.prettier extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
     - in the root of the project
     - add a folder .vscode
     - in .vscode, add a file settings.json
     - add the following settings:

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnPaste": false, // required
  "editor.formatOnType": false, // required
  "editor.formatOnSave": true, // optional
  "editor.formatOnSaveMode": "file", // required to format on save
  "files.autoSave": "onFocusChange", // optional but recommended
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit"
  },
"[typescriptreact]": {
  "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[jsonc]": {
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
}
```

## A big thank you

Your contributions—large or small—help push GoodDollar toward its mission of reducing wealth inequality through open, decentralized tools. Thank you for building with us.

