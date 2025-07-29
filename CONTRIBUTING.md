# Contributing to GoodDollar

Thank you for your interest in contributing to the [GoodDollar initiative](https://www.gooddollar.org). Everyone is welcome: Developers, designers and entrepreneurs with a passion for decentralised technologies and a vision to build a new world that has equality, security, inclusivity and innovation as its cornerstones.

When contributing to this project, please do first discuss the change you wish to make via [issues](./.github/ISSUE_TEMPLATE), [community forum](https://forum.gooddollar.org/), or any other communication channel with the [community](https://community.gooddollar.org/).

**Notes:** 
1. The GoodDollar project is distributed across [multiple repositories](https://github.com/GoodDollar). Try to file the issue against the correct repository.

1. Please note we have [issues](./.github/ISSUE_TEMPLATE) and [pull requests](./.github/PULL_REQUEST_TEMPLATE) templates, make sure you follow them to ease the contribution process.

## Issues
Issues are always welcome. Feature requests, bug reports, documentation improvements and any other kid of contribution will be triaged and worked on according to the [GoodDollar](https://github.com/GoodDollar) community and maintainers prioritization and best effort.

## Pull Requests
In general, [GoodDollar](https://github.com/GoodDollar) project [follows the GitHub flow](https://guides.github.com/introduction/flow/).

1. Fork and clone the project locally.
1. Create an upstream remote and sync local copy before branching.
1. Use individual feature branches for each separate piece of work.
1. Code changes and tests accordingly. Writing good commit messages, making sure tests pass, maintaining coverage level and following existing [documentation](https://app.gitbook.com/@gooddollar/s/gooddapp/).
1. Push to origin (fork) repository.
1. Create a new PR following the [pull request template](./.github/PULL_REQUEST_TEMPLATE).
1. Work with maintainers on code review feedback.

## Scoutgame Developers
For the most part, you can follow the contribution guidelines written below.
 
Full description about the scoutgame and participation can be found here: [GoodDollar Partner Rewards](https://scoutgame.xyz/info/partner-rewards/good-dollar)

Any support needed during your time building?

- For high-level questions the comment section of the issue you are working on is a good place to ask them.
- More in-depth questions or support required. Please join [the scoutgame support channel.](https://t.me/gooddollarbounties/4115)
- It's suggested to join the [scoutgame channel](https://t.me/gooddollarbounties/4115) anyway once you start contributing. Updates around new tickets and other opportunities will be shared in this channel first.

### Some general rules
- We expect that after being assigned, we will see progress happening. Show some progress at least once a week. This can be done through draft pr's.
- We will try to reach out and follow up if we don't see progress. But if, after seeing no progress and no response to feedback, we will unassign someone after 5 days of no response.

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

## A big Thank You!
Your contributions to this project, regardless being large or smaller ones, take this initiative a step closer to the ultimate purpose of reducing wealth inequality through blockchain technology. Thank you for taking the time to contribute.

## Building something on GoodDollar?
Share your ideas, or ask for development support.

Be sure to check out the [GoodBuilders Program!](https://gooddollar.notion.site/GoodBuilders-Program-1a6f258232f080fea8a6e3760bb8f53d)
For discussion on Discord or various program events: [GoodDollar Discord Development](https://discord.com/invite/B4bj9eXuWU)
We are also on Telegram: [GoodDollar Builders](https://discord.com/invite/B4bj9eXuWU)
