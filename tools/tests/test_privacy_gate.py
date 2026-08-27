# tools/tests/test_privacy_gate.py
import os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
from tools import privacy_gate as pg  # noqa: E402

PATTERNS = pg.load_patterns(os.path.join(ROOT, "settings", "privacy-gate.json"))
ELIGIBLE = frozenset({"technical", "contextual", "topic", "git_history", "knowledge_graph"})


class ScanText(unittest.TestCase):
    def ids(self, text, **kw):
        return sorted(f.pattern_id for f in pg.scan_text(text, PATTERNS, **kw))

    def test_clean_text_passes(self):
        self.assertEqual(self.ids("Run make test before opening a PR."), [])

    def test_aws_key_is_deny(self):
        f = pg.scan_text("key AKIAABCDEFGHIJKLMNOP here", PATTERNS)
        self.assertEqual([(x.pattern_id, x.severity, x.line) for x in f],
                         [("secret-aws-access-key", "deny", 1)])

    def test_sk_token_is_deny(self):
        f = pg.scan_text("key sk-abcdefghijklmnopqrstuvwxyz0123456789 here", PATTERNS)
        self.assertEqual([(x.pattern_id, x.severity, x.line) for x in f],
                          [("secret-sk-token", "deny", 1)])

    def test_hyphenated_project_slug_is_not_sk_token(self):
        # Regression: the pattern used to allow hyphens in the matched body,
        # so any long hyphenated "sk-..." project-name slug (e.g. a KG node id
        # under project:sk-super-model) false-positived as a secret.
        self.assertEqual(self.ids("sk-super-model-mirror-split-repo-pattern-2026-04-30"), [])

    def test_private_ip_and_home_path_are_deny(self):
        self.assertEqual(self.ids("host 192.168.1.36 and /Users/alice/x"),
                         ["net-ipv4-private", "path-home-unix"])

    def test_cgnat_range_is_deny(self):
        self.assertEqual(self.ids("100.100.5.7"), ["net-ipv4-private"])

    def test_public_ip_passes(self):
        self.assertEqual(self.ids("8.8.8.8 and 100.128.0.1"), [])

    def test_email_is_ask(self):
        f = pg.scan_text("mail me at a.b@example.org", PATTERNS)
        self.assertEqual([(x.pattern_id, x.severity) for x in f], [("pii-email", "ask")])

    def test_allowlist_by_pattern_id(self):
        self.assertEqual(self.ids("a@example.org", allowlist=["pii-email"]), [])

    def test_allowlist_by_literal(self):
        self.assertEqual(self.ids("see 192.168.1.36", allowlist=["192.168.1.36"]), [])
        self.assertEqual(self.ids("see 192.168.1.37", allowlist=["192.168.1.36"]), ["net-ipv4-private"])

    def test_private_terms_are_ask_case_insensitive(self):
        f = pg.scan_text("Ask Alice about it", PATTERNS, private_terms=["alice"])
        self.assertEqual([(x.pattern_id, x.severity) for x in f], [("private-term", "ask")])

    def test_line_numbers_are_reported(self):
        f = pg.scan_text("ok\nok\nAKIAABCDEFGHIJKLMNOP", PATTERNS)
        self.assertEqual(f[0].line, 3)

    def test_finding_never_carries_matched_text(self):
        f = pg.scan_text("AKIAABCDEFGHIJKLMNOP", PATTERNS)[0]
        self.assertNotIn("AKIA", repr(f))


class Verdict(unittest.TestCase):
    def test_codes(self):
        deny = pg.Finding("x", "deny", "p", 1); ask = pg.Finding("y", "ask", "p", 1)
        self.assertEqual(pg.verdict([]), 0)
        self.assertEqual(pg.verdict([ask]), 3)
        self.assertEqual(pg.verdict([ask, deny]), 2)


class TeamFile(unittest.TestCase):
    def test_requires_audience_team(self):
        errs = pg.check_team_file("projects/p/technical/a.md", "---\naudience: private\n---\nx", ELIGIBLE)
        self.assertEqual(errs, ["projects/p/technical/a.md: frontmatter must declare `audience: team`"])

    def test_missing_frontmatter_is_error(self):
        errs = pg.check_team_file("projects/p/technical/a.md", "no frontmatter", ELIGIBLE)
        self.assertEqual(len(errs), 1)

    def test_ineligible_category_is_error(self):
        errs = pg.check_team_file("projects/p/credentials/a.md", "---\naudience: team\n---\n", ELIGIBLE)
        self.assertEqual(errs, ["projects/p/credentials/a.md: category `credentials` is not team-eligible"])

    def test_common_category_path(self):
        self.assertEqual(pg.check_team_file("common/technical/a.md", "---\naudience: team\n---\n", ELIGIBLE), [])
        self.assertEqual(len(pg.check_team_file("common/behavioral/a.md", "---\naudience: team\n---\n", ELIGIBLE)), 1)

    def test_index_and_readme_exempt(self):
        self.assertEqual(pg.check_team_file("index.md", "# idx", ELIGIBLE), [])
        self.assertEqual(pg.check_team_file("projects/p/README.md", "# r", ELIGIBLE), [])


class Cli(unittest.TestCase):
    SCRIPT = os.path.join(ROOT, "tools", "privacy_gate.py")

    def run_cli(self, *args, stdin=""):
        import subprocess
        return subprocess.run([sys.executable, self.SCRIPT, *args], input=stdin,
                              capture_output=True, text=True)

    def test_scan_text_deny_exit_2_and_no_secret_echo(self):
        p = self.run_cli("scan", "--text", stdin="token AKIAABCDEFGHIJKLMNOP")
        self.assertEqual(p.returncode, 2)
        self.assertIn("secret-aws-access-key", p.stdout)
        self.assertNotIn("AKIAABCDEFGHIJKLMNOP", p.stdout + p.stderr)

    def test_scan_text_ask_exit_3(self):
        self.assertEqual(self.run_cli("scan", "--text", stdin="a@example.org").returncode, 3)

    def test_scan_clean_exit_0(self):
        p = self.run_cli("scan", "--text", stdin="all good")
        self.assertEqual(p.returncode, 0); self.assertIn("privacy-gate: pass", p.stdout)

    def test_json_output(self):
        import json
        p = self.run_cli("scan", "--text", "--json", stdin="AKIAABCDEFGHIJKLMNOP")
        data = json.loads(p.stdout)
        self.assertEqual(data["exit"], 2)
        self.assertEqual(data["findings"][0]["pattern_id"], "secret-aws-access-key")

    def test_staged_checks_frontmatter_in_team_repo(self):
        import subprocess, tempfile
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(["git", "init", "-q", d], check=True)
            os.makedirs(os.path.join(d, "projects", "p", "technical"))
            f = os.path.join(d, "projects", "p", "technical", "a.md")
            with open(f, "w") as h: h.write("---\naudience: private\n---\nclean\n")
            subprocess.run(["git", "-C", d, "add", "."], check=True)
            p = subprocess.run([sys.executable, self.SCRIPT, "staged"], cwd=d, capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
            self.assertIn("audience: team", p.stdout)


if __name__ == "__main__":
    unittest.main()
