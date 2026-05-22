# Contributing to GoodDollar

## Welcome to the GoodDollar Ecosystem!

Thank you for your interest in contributing to GoodDollar, we’re excited you’re here. GoodDollar is a nonprofit, open-source protocol focused on building **Universal Basic Income (UBI) on-chain** through the **G$ token**. Our mission is to make financial access more inclusive by giving people around the world a basic economic safety net, while enabling builders to create real-world applications on top of that foundation. We design and maintain open-source smart contracts, SDKs, and decentralized applications (dApps) that make it easy for anyone to integrate G$ into products, services, and communities. If you care about:

* Financial inclusion
* Web3 for social impact
* Open-source collaboration
* Building tools people actually use\
  You’re in the right place.

### Who Can Contribute?

Everyone is welcome. Whether you’re a:

* Developer (frontend, backend, smart contracts, full-stack)
* Designer or UX researcher
* Product builder or founder
* Technical writer or documentation contributor
* Student, hobbyist, or experienced professional
* Entrepreneur, etc.

There are multiple paths to participate depending on your interests, skills, and availability.

### Want to Learn More First?

* Protocol overview & documentation: [https://docs.gooddollar.org](https://docs.gooddollar.org/)
* Whitepaper: <https://docs.gooddollar.org/gooddollar-whitepaper>
* Website: [https://gooddollar.org](https://gooddollar.org/)

These explain how G$ works, the token mechanics, the UBI model, and the broader vision.

***

### Wondering How You Can Contribute? Here Are a Few Paths 👇

If you’re excited about building technology that expands access, dignity, and opportunity, we’d love to have you contribute.

#### 1) Build or Plan a Project That Integrates G$

If you’re working on (or exploring) a product that uses G$, check out the **GoodBuilders Program** — a mentorship and funding initiative that supports teams building with GoodDollar.

**Apply / Learn more:**\
👉 <https://ubi.gd/goodbuilders>

**Questions or community chat on Telegram:**\
👉[ https://ubi.gd/GoodBuildersTG](https://ubi.gd/GoodBuildersTG)

**Great fit for founders, indie hackers, and product teams**

***

#### 2) Contribute to Open Source via GoodDollar Bounties

GoodDollar Bounties are small- to medium-scope tasks across our open-source repos. You pick an issue, ship a fix or feature, and earn G$. Check out [GoodDollar Bounties](#gooddollar-bounties-overview) for more information.&#x20;

Perfect if you want:

* Clear tasks
* Fast feedback
* A way to get familiar with the codebase
* To earn while contributing

***

#### 3) Have Your Own Idea?

If you have an idea for improvements, tooling, or experiments, and want more autonomy, you can propose your own work through our **Gardens Pool for Open Source Contributors**:

👉 Welcome to GoodDollar development – [Discourse Forum](https://discourse.gooddollar.org/t/welcome-to-the-gooddollar-development-category/8241)

This path is ideal for proactive contributors who want to shape what gets built.

***

### General Contribution Guidelines

These guidelines apply to all contributors across the GoodDollar repositories.\

Read our docs [Code-Review and QA](https://docs.gooddollar.org/for-developers/open-source-contributors-code-review-and-qa)\
for more specific instructions around Code-review and QA bounty and contributions, 

#### 1) Quick Context

GoodDollar code lives across multiple repositories:\
<https://github.com/GoodDollar>

Please use the provided templates when opening:

* Issues: `./.github/ISSUE_TEMPLATE`
* Pull Requests: `./.github/PULL_REQUEST_TEMPLATE`

#### 2) Before You Start

* Get familiar with the repository and it's architecture
* Skim existing code to learn patterns and best practices
* Reuse existing helpers and components where possible
* For UI work, check if similar components already exist

#### 3) Getting Started

1. Fork and clone the repository
2. Create a feature branch
3. Make your changes following existing patterns
4. Test your changes
5. Open a Pull Request (PR) with a clear description

#### 4) What You Can Contribute.

**GoodDollar Bounty contributors** can find available tasks directly here on GitHub. See [GoodDollar Bounties](#gooddollar-bounties-overview) for more information.&#x20;

If you’re interested in contributing through the **Open Contributors Pool?** Please start by applying **first** on [The GoodDollar Discourse Forum](https://discourse.gooddollar.org/t/welcome-to-the-gooddollar-development-category/8241). <br>

Below are some issues you can look out for:

* Feature ideas
* Bug fixes
* Documentation improvements
* Small enhancements and refactors

All contributions are welcome and triaged based on maintainer priority and capacity.

#### 5) While Building

* Reproduce the issue locally if applicable
* Follow the repo’s framework and language conventions
* Keep changes focused and scoped
* Always ask questions early if anything is unclear
* We ask that you follow the framework's default principles and best practices, as well as the language's conventions and existing design patterns. If you’re designing something new, aim for simple, usable, and consistent experiences. Make sure your change fits naturally within the part of the product where it will live.

#### 6) Opening a Pull Request

We follow the GitHub flow: <https://guides.github.com/introduction/flow/>

To make the review faster:

* One PR should solve one issue
* Reference the related issue using `#issue-number`
* Clearly explain what you changed and why
* Add screenshots or a demo video for UI/UX changes (desktop + mobile)
* Make sure builds pass and typings are correct (most repos use TypeScript)
* Use existing linting and formatting rules (prettier, eslint, etc.)

**VSCode formatting tip:**

* Install [esbenp.prettier extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
* In the root of the project:
  * Create a `.vscode` folder
  * Inside it, create `settings.json`
  * Add:

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

> **Tip:** If you’re unsure about anything, ask in the bounty support channel. We’re happy to help early rather than after a PR goes off-track.

#### 7) During Review

* Share progress at least every 3 days (draft PRs are great). If any issue arises, please communicate as needed.
* We request that you not resolve comments from the maintainer or AI (automated) yourself; only reply with what you changed or why. When you’ve made the requested changes, reply to the comment to let us know; reviewers and maintainers will handle resolving it.
* Respond to feedback as promptly as possible.
* A maintainer will assign you or ask a quick clarifying question. We strongly encourage you to ask follow-up questions if anything about the scope or implementation isn’t fully clear. This helps avoid rework and speeds up reviews.

#### 8) Staying Active

* If there are no updates and no response for 3 days, the issue may be unassigned. Always be on the look out of the status of the task.
* If you’re stuck or blocked, let us know — we’re happy to help
* Ask questions and share blockers as soon as they come up — in the Builders Telegram channel or directly on the GitHub issue/PR
* If your PR starts to grow bigger than expected, please ask for an **in-progress review**
* For some bounties, we may suggest small milestones along the way

#### 9) Documentation Guidelines

* Add or update documentation when relevant and let us know when you do
* Include examples or demos when helpful
* Again, always reach out to us in any relevant channel for any questions/concerns/asks— we’re happy to assist

***

### GoodDollar Bounties Overview

**Bounties are posted as GitHub issues and tracked in a Projects board.**\
See [GitHub Bounties Board](https://github.com/orgs/GoodDollar/projects/5/views/1)

#### How it Works

1. Browse the Bounties Board and find an issue in [**Ready-For-Assignment**](https://github.com/orgs/GoodDollar/projects/5/views/1). Bounties are labeled gd-bounty- (for example: gd-bounty-basic, gd-bounty-common, etc.), so you can quickly see the tier and scope.
2. To claim a bounty, comment on the issue to request assignment - Example: `I’d like to take this. ETA: 2–3 days.`
3. Once assigned and want to start working, implement the task and open a Pull Request (PR)
4. In the PR description, link to the issue and explain what you fixed/changed/added
5. Request a review using GitHub’s *Request Review* button
6. Address feedback (including automated review comments).
7. After the merge, request a payout in the [**Gardens OS Contributors Pool**](https://app.gardens.fund/gardens/42220/0x62b8b11039fcfe5ab0c56e502b1c372a3d2a9c7a/0xf42c9ca2b10010142e2bac34ebdddb0b82177684/94)

Submit a payout request with:

* PR link
* Issue link
* Bounty tier
* Your payout address

A maintainer or committee member will review and approve the payout.&#x20;

Please note: To submit a payout request through the Gardens Pool, you must be a verified community member with a whitelisted G$ wallet or address. You'll also need to stake 105,000 G$ in the pool. Once your stake is active, you can start creating proposals. This requirement helps keep the process running smoothly and ensures a trusted contributor system.

8\. Once approved, you’ll receive G$ based on the bounty tier

### Bounty Tiers Explained

Each bounty is assigned a tier that reflects it's scope, difficulty, and expected time commitment. Higher tiers come with higher G$ rewards.

* **Basic** – Small fixes or straightforward tasks (e.g., UI tweaks, minor bug fixes, documentation updates)
* **Common** – Medium-sized features or improvements that require some familiarity with the codebase
* **Rare** – Larger features or greater improvements that touch multiple areas or require a solid understanding of the system
* **Mythic** – Complex work involving architecture, performance, or important product flows
* **Legendary** – High-impact initiatives such as major features, protocol-level changes, or long-running improvements

The tier is shown on each bounty issue so you know upfront what level of effort (and reward) to expect and payouts are in G$. \
For Code-review and QA bounty payouts, [see this table](https://docs.gooddollar.org/for-developers/open-source-contributors-code-review-and-qa/payments-for-reviews-and-qa). \
For Bounty-Contributors see the table below:&#x20;

| Tier      | Reward (USD) |  Reward (G$) |
| --------- | -----------: | -----------: |
| Basic     |          $25 |   250,000 G$ |
| Common    |          $50 |   500,000 G$ |
| Rare      |         $150 | 1,500,000 G$ |
| Epic      |         $250 | 2,500,000 G$ |
| Mythic    |         $350 | 3,500,000 G$ |
| Legendary |         $450 | 4,500,000 G$ |

#### Important to Note

* G$ rewards are calculated using a base price of **$0.0001 per `G$`**
* Because token prices can move, we can’t guarantee the exact value at the time of distribution
* Each bounty’s tier is set upfront based on scope (taking longer to finish doesn’t change the payout amount)

### Where Bounties Live

**Bounties Board (source of truth):**\
<https://github.com/orgs/GoodDollar/projects>

**Some eligible repositories:**

* <https://github.com/GoodDollar/GoodProtocolUI>
* <https://github.com/GoodDollar/GoodSdks>
* <https://github.com/GoodDollar/GoodCollective>
* <https://github.com/GoodDollar/GoodWeb3-Mono>

Look for issues labeled `GoodBounties-<tier>` and a tier label (Basic / Common / Advanced / etc.).

***

#### GPG-Signing
_Before doing the next steps make sure your email address is verified.
You can do this in your profile > settings > emails section._


In most of our repositories, commits are only accepted if they are signed.
If you are on a system with GPG keyrings already installed, you can use the following command:
`gpg --full-generate-key`

Follow the prompts (choose RSA, 4096 bits, and use your verified Git email).

After which you can run:
`gpg --list-secret-keys --keyid-format LONG`
and take the key-id that is associated with your VERIFIED git email address

You can read more about commit signatures and how to set it up on your specific system here: https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification

***

#### Need Help?

Bounty support channel (questions, blockers, reviews):&#x20;

* [GoodDollar Bounties Telegram](https://t.me/gooddollarbounties/4115)
* [Builders Telegram](https://ubi.gd/GoodBuildersTG)
* [GoodDollar Docs](https://docs.gooddollar.org)
* [GoodDollar Organization on GitHub](https://github.com/GoodDollar)

***

**Your contributions, large or small, help advance GoodDollar's mission to reduce wealth inequality through open, decentralized tools.**

Thank you for building with us, and welcome to **GoodDollar**!
