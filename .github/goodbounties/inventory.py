"""Prepare a reviewer report. This script never assigns or contacts anyone.

For a policy review, read decide_review() below. For the full process, read
build_report(). GitHub requests and response checking are in github_read.py.
"""
import argparse
from collections import defaultdict
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import sys

from github_read import GitHub, InventoryError, collect_repository, matches, parse_time

HERE = Path(__file__).resolve().parent
REPOSITORY_NAME = r"GoodDollar/[A-Za-z0-9_.-]+"
LOGIN = r"[A-Za-z0-9-]+"


def decide_review(pull, owner, triage_reviewers, candidates, complete):
    """Apply four rules in order. Candidates are options, never assignments."""
    recheck = False
    options = []

    # 1. Once Alice is confirmed, her submitted review must not replace her.
    # Even lost access needs a maintainer decision, not an automatic replacement.
    # Record confirmation in the reviewed config change; Git tracks ownership edits.
    if owner:
        status = "retain_designated_reviewer"
        recheck = owner not in triage_reviewers or owner == pull["author"]
        message = f"Keep {owner}"
        if recheck:
            message += "; maintainer must recheck eligibility"

    # 2. A draft without an owner is not ready for a new review assignment.
    elif pull["draft"]:
        status = "draft"
        message = "Wait: draft PR"

    # 3. Existing activity may be a real assignment or a maintainer's first look.
    # We cannot tell which from the API, so ask instead of guessing ownership.
    # If a request was removed before any review, this snapshot cannot recover it.
    # Only a review_owners entry guarantees that original person is remembered.
    elif pull["requested_users"] or pull["requested_teams"] or any(
        review["login"] != pull["author"] for review in pull["reviews"]
    ):
        status = "reconcile_existing_reviewers"
        message = "Confirm ownership with the existing reviewers"

    # 4. Only an otherwise unassigned, ready PR gets possible reviewers.
    # A failed repository read makes everyone's workload uncertain.
    else:
        status = "needs_manager_suggestion"
        message = "Wait for a complete inventory"
        if complete:
            options = sorted(candidates - {pull["author"]})
            message = "No eligible opted-in reviewer found"
            if options:
                message = "Manager to consider: " + ", ".join(options)

    return {
        "key": pull["key"],
        "head_sha": pull["head_sha"],
        "status": status,
        "next_step": message,
        "designated_reviewer": owner,
        "eligibility_recheck_needed": recheck,
        "candidates": options,
    }


def count_workload(repositories, owners, opted_in, cutoff):
    """Keep PR links as evidence. Sets count one PR once, even after many reviews."""
    open_work = defaultdict(set)
    recent_reviews = defaultdict(set)
    for repository in repositories:
        for pull in repository["pulls"]:
            key = pull["key"]
            participants = set(pull["requested_users"])
            for review in pull["reviews"]:
                login = review["login"]
                if login == pull["author"]:
                    continue
                participants.add(login)
                if parse_time(review["submitted_at"]) >= cutoff:
                    recent_reviews[login].add(key)

            # A submitted review clears the native request. Keep that involvement
            # and the confirmed owner counted while the PR is still open.
            owner = owners.get(key.lower())
            if owner:
                participants.add(owner)
            if pull["state"] == "open":
                for login in participants:
                    open_work[login].add(key)

    metrics = {}
    for login in sorted(set(open_work) | set(recent_reviews) | opted_in):
        metrics[login] = {
            "open_involvements": sorted(open_work[login]),
            "reviewed_prs_in_window": sorted(recent_reviews[login]),
        }
    return metrics


def build_report(config, api, now):
    """Read all repositories first, then apply the same rules to every open PR."""
    validate_settings(config)
    cutoff = now - timedelta(days=config["history_days"])
    opted_in = {name.lower() for name in config["opted_in_reviewers"]}
    # This is the only ownership memory. Missing entries mean "unknown", not
    # "never assigned"; current GitHub activity is handled conservatively below.
    owners = {key.lower(): owner.lower() for key, owner in config.get("review_owners", {}).items()}

    repositories = []
    errors = []
    for name in config["repositories"]:
        try:
            repositories.append(collect_repository(api, name, cutoff))
        except InventoryError as error:
            errors.append({"repository": name, "detail": str(error)})
        except (KeyError, TypeError, AttributeError, ValueError):
            # Malformed API data is not an empty roster or an unassigned PR.
            errors.append({
                "repository": name,
                "detail": "Missing or invalid GitHub fields; rerun or check the API response.",
            })

    queue = []
    for repository in repositories:
        triage_reviewers = set()
        for user in repository["outside_collaborators"]:
            # Write/admin roles also have the triage permission BIT. We need the ROLE.
            if user["type"] == "User" and user["role_name"].lower() == "triage":
                triage_reviewers.add(user["login"])
        candidates = triage_reviewers & opted_in
        for pull in repository["pulls"]:
            if pull["state"] == "open":
                owner = owners.get(pull["key"].lower())
                queue.append(decide_review(pull, owner, triage_reviewers, candidates, not errors))

    return {
        "schema_version": 3,
        "generated_at": now.isoformat(),
        "history_since": cutoff.isoformat(),
        "complete": not errors,
        "errors": errors,
        "repositories": repositories,
        "reviewer_metrics": count_workload(repositories, owners, opted_in, cutoff),
        "queue": sorted(queue, key=lambda row: row["key"].lower()),
    }


def markdown(report):
    """Display the decision already made above; do not implement the rules twice."""
    lines = [
        "# GoodBounties review report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "Candidates need availability and conflict checks. Nobody has been assigned.",
        "",
    ]
    if report["errors"]:
        lines += ["**Incomplete: candidate lists are withheld and workload counts are partial.**", ""]
        for error in report["errors"]:
            lines.append(f"- {error['repository']}: {error['detail']}")
        lines.append("")
    lines += ["| PR | Next step |", "| --- | --- |"]
    for row in report["queue"]:
        repository, number = row["key"].split("#")
        url = f"https://github.com/{repository}/pull/{number}"
        lines.append(f"| [{row['key']}]({url}) | {row['next_step']} |")
    lines += ["", "See report.json for roles, review history and workload evidence."]
    return "\n".join(lines) + "\n"


# These checks protect the file boundary, rather than adding fallback defaults.
# A typo in ownership or scope must stop the run instead of silently changing it.
def validate_settings(config):
    """Check maintainer-edited JSON before making any GitHub requests."""
    try:
        # Scope comes from reviewed settings, never from a dispatch or PR payload.
        repositories = config["repositories"]
        if not isinstance(repositories, list) or not repositories:
            raise InventoryError("config.json needs a nonempty repositories list.")
        if not all(matches(REPOSITORY_NAME, name) for name in repositories):
            raise InventoryError("Each repository must be named GoodDollar/repository.")

        # Access is not consent: keep accepted reviewers separate from API discovery.
        reviewers = config["opted_in_reviewers"]
        if not isinstance(reviewers, list) or not all(matches(LOGIN, name) for name in reviewers):
            raise InventoryError("opted_in_reviewers must be a list of GitHub usernames.")
        for names in (repositories, reviewers):
            if len({name.lower() for name in names}) != len(names):
                raise InventoryError("Remove duplicate repository or reviewer names (case-insensitive).")
        days = config["history_days"]
        if type(days) is not int or not 1 <= days <= 365:
            raise InventoryError("history_days must be a whole number from 1 to 365.")

        # Reject ambiguous keys such as #01 so a confirmed owner cannot be overlooked.
        owners = config.get("review_owners", {})
        if not isinstance(owners, dict):
            raise InventoryError("review_owners must be an object mapping PRs to usernames.")
        if len({key.lower() for key in owners}) != len(owners):
            raise InventoryError("Remove duplicate review_owners keys (case-insensitive).")
        for key, owner in owners.items():
            if not matches(REPOSITORY_NAME + r"#[1-9][0-9]*", key) or not matches(LOGIN, owner):
                raise InventoryError("review_owners must map GoodDollar/Repository#123 to a GitHub username.")
    except (KeyError, TypeError, AttributeError, ValueError):
        raise InventoryError("Invalid config structure; see the README example.") from None


def read_settings(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        raise InventoryError(f"Cannot read valid JSON from {path.name}.") from None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=HERE / "config.json")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        config = read_settings(args.config)
        api = GitHub(os.environ.get("GOODBOUNTIES_READ_TOKEN"))
        report = build_report(config, api, datetime.now(timezone.utc))
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "report.json").write_text(json.dumps(report, indent=2) + "\n")
        (args.output / "report.md").write_text(markdown(report))
    except InventoryError as error:
        print(f"Inventory failed: {error}", file=sys.stderr)
        return 1
    except OSError:
        print("Cannot write reports; check --output and directory permissions.", file=sys.stderr)
        return 1
    print(f"Complete={report['complete']}; {len(report['queue'])} open PRs; {len(report['errors'])} repository errors")
    return 0 if report["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
