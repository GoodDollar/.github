# GoodBounties reviewer inventory

This reads GitHub and produces evidence for the GoodBounties manager. It does not assign reviewers, send messages or run the manager. Those connections are still to be made.

## One config file

Edit [config.json](config.json):

| Field | Purpose |
| --- | --- |
| `repositories` | Add/remove participating repositories. The current six are proposals. |
| `opted_in_reviewers` | Accepted GitHub usernames. Empty means no candidates. |
| `history_days` | How far back to count submitted reviews (currently 90 days). |
| `review_owners` | Optional map of PR to confirmed reviewer, e.g. `"GoodDollar/GoodWidget#123": "alice"`. |

There is no separate designation ledger. Record confirmation or reassignment in the Git review of the config change; Git history supplies the audit trail. Keep closed entries so reopening preserves the same owner. The script never writes this map.

**Recording an owner is required to guarantee that exact person's continuity.** Without an entry, existing requests or submitted reviews cause a reconciliation prompt. A request removed before anyone submits a review cannot be recovered from the snapshot. Removing this map entirely would lose that guarantee; this small manual step remains until the manager has an integrated, durable ownership store.

## Four rules to review

Start at `decide_review()` at the top of [inventory.py](inventory.py):

1. **Recorded owner:** keep them through new commits, reviews and draft transitions. Flag lost eligibility; do not replace them.
2. **Draft without an owner:** wait.
3. **Existing requested/submitted review activity:** ask the maintainer who owns it.
4. **Otherwise ready:** show opted-in outside collaborators with effective Triage role, excluding the author. The manager must still check availability, co-authorship, QA separation and conflicts.

If any repository cannot be read, all candidate lists are withheld. Partial workload could make a busy reviewer look free. Workload counts distinct PRs; it can include maintainer first impressions and excludes unattributed team work and work outside the listed repositories.

`github_read.py` contains GET requests, pagination and response checking. The two Python files use only the standard library. JSON report version 3 stores a `designated_reviewer` username, candidate usernames and shared workload evidence; Markdown displays the same decisions.

## Tests and live runs are separate

[Check GoodBounties changes](../workflows/goodbounties-check.yml) runs offline tests and validates the actual config on relevant PRs and pushes to `master`. It has no inventory credential. Local equivalent:

```sh
python3 -m unittest discover -s .github/goodbounties/tests -v
```

[The inventory workflow](../workflows/goodbounties-review-inventory.yml) does only checkout → live collection → upload. Runtime checks still validate configuration, access, response fields and pagination. It accepts a manual run or `goodbounties-review-refresh` dispatch; its schedule is commented out.

Before enabling, review the code, confirm the roster/owners and report destination, and provide `GOODBOUNTIES_READ_TOKEN` with **Metadata read + Pull requests read** on the listed repositories. User-based tokens also need appropriate organization/repository access. Set the single variable `GOODBOUNTIES_INVENTORY_ENABLED=true` after merge to the default branch. No credential or remote setting has been created here.

Reports are `report.md` and `report.json`, uploaded as `goodbounties-review-inventory-<run_id>-<run_attempt>` in the workflow run's Artifacts, retained for **7 days**. They are not sent to the manager. Check repository/artifact visibility before including private data. Failed collection saves an incomplete report; failures before collection may produce none. Exit 1 means failure.

For a local run with the token supplied securely in the environment:

```sh
python3 .github/goodbounties/inventory.py --output /tmp/goodbounties-report
```

## What remains to connect

`.github` does not automatically receive other repositories' PR events. The inactive [relay example](templates/review-refresh.yml.example) can send a constant refresh event after separate installation; it needs its own credential with **Contents write on GoodDollar/.github only**. It never runs PR code. Remove relay access when offboarding. A trusted App receiver could replace it later; none is implemented.

Every refresh rescans the configured list; duplicate events are harmless. The relay covers ready/open/reopen/commit/close/draft events, not submitted reviews. An optional hourly scan could cover missed changes. Add manager report retrieval/execution separately using [these instructions](manager-instructions.md).

The collector never requests reviews or changes permissions. It preserves evidence, not GitHub's reviewer sidebar. It rejects redirects and malformed data; scans have limits/timeouts. Reads are not atomic, so any future assignment writer must recheck live state. Actual hosted execution and token access still need a pilot check.

References: [GitHub roles/access](https://docs.github.com/en/rest/collaborators/collaborators#list-repository-collaborators), [review requests](https://docs.github.com/en/rest/pulls/review-requests#get-all-requested-reviewers-for-a-pull-request), [dispatch permissions](https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event).
