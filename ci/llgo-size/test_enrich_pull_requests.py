import importlib.util
import io
import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).with_name("enrich_pull_requests.py")
SPEC = importlib.util.spec_from_file_location("enrich_pull_requests", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PullRequestSelectionTest(unittest.TestCase):
    def test_prefers_exact_merged_commit(self):
        pulls = [
            {
                "number": 11,
                "html_url": "https://github.com/xgo-dev/llgo/pull/11",
                "merged_at": "2026-08-01T00:00:00Z",
                "merge_commit_sha": "b" * 40,
            },
            {
                "number": 12,
                "html_url": "https://github.com/xgo-dev/llgo/pull/12",
                "merged_at": "2026-08-02T00:00:00Z",
                "merge_commit_sha": "a" * 40,
            },
        ]
        selected = MODULE.select_merged_pull_request(pulls, "a" * 40)
        self.assertEqual(selected["number"], 12)

    def test_uses_first_merged_containing_pull_request(self):
        pulls = [
            {
                "number": 22,
                "html_url": "https://github.com/xgo-dev/llgo/pull/22",
                "merged_at": "2026-08-03T00:00:00Z",
                "merge_commit_sha": "c" * 40,
            },
            {
                "number": 21,
                "html_url": "https://github.com/xgo-dev/llgo/pull/21",
                "merged_at": "2026-08-02T00:00:00Z",
                "merge_commit_sha": "b" * 40,
            },
        ]
        selected = MODULE.select_merged_pull_request(pulls, "a" * 40)
        self.assertEqual(selected["number"], 21)

    def test_retries_public_lookup_when_repository_token_is_scoped(self):
        pull = {
            "number": 23,
            "html_url": "https://github.com/xgo-dev/llgo/pull/23",
            "merged_at": "2026-08-04T00:00:00Z",
            "merge_commit_sha": "a" * 40,
        }
        denied = urllib.error.HTTPError(
            "https://api.github.com/test",
            403,
            "forbidden",
            {},
            io.BytesIO(b"token cannot access repository"),
        )
        with mock.patch.object(
            MODULE.urllib.request,
            "urlopen",
            side_effect=[denied, io.BytesIO(json.dumps([pull]).encode())],
        ) as urlopen:
            selected = MODULE.github_pull_request_lookup(
                "xgo-dev/llgo", "a" * 40, "https://api.github.com", "scoped-token"
            )
        self.assertEqual(selected["number"], 23)
        self.assertIn("Authorization", urlopen.call_args_list[0].args[0].headers)
        self.assertNotIn("Authorization", urlopen.call_args_list[1].args[0].headers)


class IndexEnrichmentTest(unittest.TestCase):
    def test_orders_runs_by_llgo_main_history_instead_of_build_completion(self):
        first = "a" * 40
        second = "b" * 40
        index = {
            "runs": [
                {
                    "key": second,
                    "llgoCommit": second,
                    "llgoMainIndex": 1,
                    "createdAt": "2026-08-21T01:00:00Z",
                },
                {
                    "key": first,
                    "llgoCommit": first,
                    "llgoMainIndex": 1,
                    "createdAt": "2026-08-21T02:00:00Z",
                },
            ]
        }

        MODULE.order_runs(index, [first, second])

        self.assertEqual([run["key"] for run in index["runs"]], [second, first])
        self.assertEqual([run["llgoMainIndex"] for run in index["runs"]], [2, 1])

    def test_places_non_main_runs_after_topological_history(self):
        main = "a" * 40
        manual = "c" * 40
        index = {
            "runs": [
                {"key": manual, "llgoCommit": manual, "createdAt": "2026-01-01T00:00:00Z"},
                {"key": main, "llgoCommit": main, "createdAt": "2026-08-01T00:00:00Z"},
            ]
        }

        MODULE.order_runs(index, [main])

        self.assertEqual([run["key"] for run in index["runs"]], [main, manual])

    def test_builds_compact_trends_and_historical_benchmark_union(self):
        with tempfile.TemporaryDirectory() as temporary:
            data_dir = Path(temporary)
            index = {"runs": []}
            for key, names in (("a", ["Zeta", "alpha"]), ("b", ["Historical", "alpha"])):
                result_dir = data_dir / "runs" / key
                result_dir.mkdir(parents=True)
                benchmarks = [
                    {
                        "name": name,
                        "values": {"Go": len(name)},
                        "sizes": {"withDwarf": {"Go": 42}, "withoutDwarf": {"Go": 21}} if key == "a" else None,
                        "buildTimes": {"Go": {"wallNs": len(name) * 10}} if key == "a" else {},
                    }
                    for name in names
                ]
                (result_dir / "results.json").write_text(
                    json.dumps({
                        "benchmarks": benchmarks,
                        "native": {"buildTimes": "build-times.tsv"},
                    }),
                    encoding="utf-8",
                )
                (result_dir / "build-times.tsv").write_text(
                    "benchmark\tconfiguration\treal-ns\tuser-ns\tsys-ns\n"
                    + "\n".join("{}\tGo\t{}\t1\t1".format(name, len(name) * 100) for name in names)
                    + "\n",
                    encoding="utf-8",
                )
                index["runs"].append({"path": "runs/{}/results.json".format(key)})

            trends = MODULE.build_trends(index, data_dir)

            self.assertEqual(trends["runs"][0]["benchmarks"][0]["sizes"]["withoutDwarf"]["Go"], 21)
            self.assertIsNone(trends["runs"][1]["benchmarks"][0]["sizes"])
            self.assertEqual(index["benchmarkNames"], ["alpha", "Historical", "Zeta"])
            self.assertEqual(trends["runs"][0]["benchmarks"][0]["values"]["Go"], 4)
            self.assertEqual(trends["runs"][0]["benchmarks"][0]["buildTimes"]["Go"]["wallNs"], 40)
            self.assertEqual(trends["runs"][1]["benchmarks"][0]["buildTimes"]["Go"]["wallNs"], 1000)

    def test_reads_legacy_repository_and_caches_resolution(self):
        with tempfile.TemporaryDirectory() as temporary:
            data_dir = Path(temporary)
            result_dir = data_dir / "runs" / ("a" * 40)
            result_dir.mkdir(parents=True)
            (result_dir / "results.json").write_text(
                json.dumps({"run": {"llgoRepository": "xgo-dev/llgo"}}),
                encoding="utf-8",
            )
            index = {
                "runs": [
                    {
                        "key": "a" * 40,
                        "llgoCommit": "A" * 40,
                        "path": "runs/{}/results.json".format("a" * 40),
                    }
                ]
            }
            calls = []

            def lookup(repository, commit):
                calls.append((repository, commit))
                return {
                    "number": 2346,
                    "html_url": "https://github.com/xgo-dev/llgo/pull/2346",
                    "title": "go1.25",
                }

            queries, linked = MODULE.enrich_runs(index, data_dir, lookup, "fallback/llgo")
            self.assertEqual((queries, linked), (1, 1))
            self.assertEqual(calls, [("xgo-dev/llgo", "a" * 40)])
            run = index["runs"][0]
            self.assertEqual(run["pullRequestNumber"], 2346)
            self.assertEqual(run["pullRequestUrl"], "https://github.com/xgo-dev/llgo/pull/2346")
            self.assertEqual(run["commitUrl"], "https://github.com/xgo-dev/llgo/commit/" + "a" * 40)

            queries, linked = MODULE.enrich_runs(
                index,
                data_dir,
                lambda *_: self.fail("cached metadata should not be queried"),
                "fallback/llgo",
            )
            self.assertEqual((queries, linked), (0, 1))


if __name__ == "__main__":
    unittest.main()
