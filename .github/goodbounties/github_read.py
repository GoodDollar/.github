"""GitHub read-only plumbing; the reviewer rules live in inventory.py.

This file converts GitHub responses into the small evidence records used by those
rules. Nothing here assigns reviewers, follows redirects, or runs PR code.
"""
from datetime import datetime
import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

LOGIN = r"[A-Za-z0-9-]+"


class InventoryError(Exception):
    """An operator-facing error written by us, safe to include in reports."""


def parse_time(value):
    date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if date.tzinfo is None:
        raise ValueError("Timestamp needs a timezone")
    return date


def matches(pattern, value):
    return isinstance(value, str) and re.fullmatch(pattern, value, re.IGNORECASE)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # A renamed repository needs a config update. Never forward its credential.
        return None


class GitHub:
    """One GET-only client shared by all repository reads in this run."""
    def __init__(self, token):
        if not token:
            raise InventoryError("Set GOODBOUNTIES_READ_TOKEN to a token with access to the listed repositories.")
        self.token = token
        self.opener = build_opener(NoRedirect())

    def get(self, path, **params):
        if not path.startswith("/repos/") or any(part in (".", "..") for part in path.split("/")):
            raise InventoryError("Unexpected repository API path.")
        url = "https://api.github.com" + path
        if params:
            url += "?" + urlencode(params)
        headers = {
            "Authorization": "Bearer " + self.token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "GoodBounties-read-only-inventory",
        }
        request = Request(url, method="GET", headers=headers)
        try:
            with self.opener.open(request, timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            # Explain the problem without printing response bodies or credentials.
            advice = {
                401: "Token is invalid or expired.",
                403: "Check token permissions, organization approval and GitHub rate limits.",
                404: "Repository is missing or is not shared with this token.",
                429: "GitHub rate limit reached; rerun later.",
            }.get(error.code, "Check repository naming and GitHub availability; rerun after recovery.")
            raise InventoryError(f"HTTP {error.code}: {advice}") from None
        except (URLError, OSError):
            raise InventoryError("Cannot reach GitHub; rerun after the connection recovers.") from None

    def pages(self, path, **params):
        # GitHub returns at most 100 records per page. Stopping after page one
        # would make the roster or workload look smaller than it really is.
        # The cap bounds runaway scans: hitting it is an error, never a partial success.
        for page in range(1, 101):
            rows = self.get(path, per_page=100, page=page, **params)
            if not isinstance(rows, list):
                raise InventoryError("GitHub returned an unexpected list response.")
            yield from rows
            if len(rows) < 100:
                return
        raise InventoryError("Pagination limit reached (10,000 records); report is incomplete.")


def read_login(user):
    login = user["login"]
    if not matches(LOGIN + r"(?:\[bot\])?", login):
        raise InventoryError("GitHub returned an invalid username.")
    return login.lower()  # GitHub usernames are case-insensitive. Normalize once.


def is_human(user):
    return user is not None and user["type"] == "User"


def read_pull(api, repository, pull):
    """Keep only review evidence. Never copy PR text or execute contributor code."""
    reviews = []
    path = f"/repos/{repository}/pulls/{pull['number']}/reviews"
    for review in api.pages(path):
        if is_human(review["user"]) and review["submitted_at"]:
            # Validate here so malformed dates fail this repository, not report rendering.
            submitted_at = parse_time(review["submitted_at"]).isoformat()
            reviews.append({
                "login": read_login(review["user"]),
                "state": review["state"],
                "submitted_at": submitted_at,
                "commit_id": review["commit_id"],
            })
    # Missing readiness/request fields are errors, not evidence of an unassigned PR.
    for field in ("requested_reviewers", "requested_teams"):
        if not isinstance(pull[field], list):
            raise InventoryError("GitHub returned an invalid requested-reviewer list.")
    if type(pull["draft"]) is not bool or pull["state"] not in ("open", "closed"):
        raise InventoryError("GitHub returned an unknown PR readiness/state.")
    return {
        "key": f"{repository}#{pull['number']}",
        "author": read_login(pull["user"]),
        "state": pull["state"],
        "draft": pull["draft"],
        "head_sha": pull["head"]["sha"],
        "requested_users": [read_login(u) for u in pull["requested_reviewers"] if is_human(u)],
        "requested_teams": [team["slug"] for team in pull["requested_teams"]],
        "reviews": reviews,
    }


def collect_repository(api, repository, cutoff):
    """Fetch outside collaborators, open PRs and recently updated closed PRs."""
    path = "/repos/" + repository
    metadata = api.get(path)
    if metadata["owner"]["type"] != "Organization":
        raise InventoryError("Outside collaborator discovery needs an organization repository.")
    if metadata["full_name"].lower() != repository.lower() or metadata["archived"]:
        raise InventoryError("Repository renamed or archived; update config.json.")
    collaborators = []
    for user in api.pages(path + "/collaborators", affiliation="outside"):
        if not isinstance(user["role_name"], str) or not user["role_name"]:
            raise InventoryError("GitHub did not return an effective collaborator role.")
        collaborators.append({
            "login": read_login(user),
            "type": user["type"],
            "role_name": user["role_name"],
        })
    # Read open PRs regardless of age. The cutoff applies only to closed history:
    # an old open PR can still be occupying a reviewer today.
    pulls = list(api.pages(path + "/pulls", state="open", sort="created", direction="asc"))
    for pull in api.pages(path + "/pulls", state="closed", sort="updated", direction="desc"):
        if parse_time(pull["updated_at"]) < cutoff:
            break  # Older closed PRs cannot contain reviews submitted in this window.
        pulls.append(pull)
    # These reads are not one transaction. A PR can close between the open and
    # closed queries, appearing twice. Keep the later closed snapshot so it does
    # not continue to count as open work. Any future writer must recheck live state.
    unique_pulls = {pull["number"]: pull for pull in pulls}
    return {
        "repository": repository,
        "private": metadata["private"],
        "outside_collaborators": sorted(collaborators, key=lambda user: user["login"]),
        "pulls": [read_pull(api, repository, pull) for pull in unique_pulls.values()],
    }
