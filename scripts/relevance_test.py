#!/usr/bin/env python3
"""
awesome-claude-mods :: relevance_test.py

Tests for the one rule this project lives or dies by.

"mod" is one of the most overloaded tokens in software. A search for it returns,
in rough order of volume: game mods, moderation bots, modulo, and Apache's
mod_* namespace. All four appeared in the real candidate set during the first
collection run. If the filter is loose the list fills with Minecraft; if it is
tight the list is empty.

So the rule is a two-signal rule with three disjoint word sets, and every case
below is either a family that actually polluted the candidate set or a shape the
rule is supposed to admit.

Run: python3 scripts/relevance_test.py
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import curate  # noqa: E402


def admitted(full_name: str, description: str = "",
             topics: tuple[str, ...] = ()) -> bool:
    """
    The admission decision from build_repo_entries, without the star floor.

    Kept in step with that function deliberately: a test that exercises a
    reimplementation proves nothing about the code that runs.
    """
    owner = full_name.split("/")[0].lower()
    repo_name = full_name.split("/")[-1]
    topic_text = " ".join(topics)
    haystack = f"{repo_name} {description} {topic_text}"
    full_haystack = f"{full_name} {description} {topic_text}"

    if curate.is_collision(full_name, full_haystack):
        return False
    if full_name in curate.SELF_REPOS:
        return False
    if full_name in curate.OFFICIAL_ALLOWLIST or owner in curate.OFFICIAL_OWNERS:
        return True
    if curate.any_match(curate.STRONG_PATTERNS, haystack):
        return True
    # A name no longer admits on its own, and neither does being a plugin.
    return curate.medium_signal(haystack)


class TestAdmits(unittest.TestCase):
    """Projects that belong in the list."""

    def test_official(self):
        self.assertTrue(admitted("anthropics/claude-code",
                                 "Claude Code, the CLI agent"))

    def test_builtin_mod_name(self):
        self.assertTrue(admitted("someone/cc-plugin-you-should-know",
                                 "A side agent watches your back"))

    def test_phrase_strong(self):
        self.assertTrue(admitted("someone/toolkit",
                                 "Adds Claude Mods support to your session"))

    def test_mod_plus_platform(self):
        self.assertTrue(admitted("someone/statusbar",
                                 "A mod for Claude Code that customises the status line"))

    def test_statusline_is_mod_surface(self):
        self.assertTrue(admitted("someone/line",
                                 "A statusline for Claude Code with token counts"))

    def test_pane_is_mod_surface(self):
        self.assertTrue(admitted("someone/xyz",
                                 "Draws a band above the prompt in Claude Code"))

    def test_teammates_are_mod_surface(self):
        self.assertTrue(admitted("someone/team",
                                 "Spawns Claude Code teammates for parallel work"))

    def test_plain_plugin_is_out_of_scope(self):
        # The plugin ecosystem predates mods and is far larger. Admitting it
        # put 783 repositories in a list about the layer that came after, and
        # measured again after narrowing, 406 of the 409 entries in the plugin
        # category named no part of the mod surface.
        self.assertFalse(admitted("someone/market",
                                  "A Claude Code plugin marketplace"))
        self.assertFalse(admitted("someone/hooks",
                                  "Hooks and slash commands for Claude Code"))
        self.assertFalse(admitted("someone/skills",
                                  "380 Claude Code skills and agents"))
        self.assertFalse(admitted("someone/agents",
                                  "A multi-agent framework for Claude Code"))

    def test_cordis_plugin(self):
        self.assertTrue(admitted("someone/cordis-mods",
                                 "A Cordis plugin that adds a mod pane"))

    def test_dsh(self):
        self.assertTrue(admitted("someone/dsh-tools",
                                 "A dsh plugin adding teammate panes"))

    def test_mod_api_token(self):
        self.assertTrue(admitted("someone/debugger",
                                 "Overlays ui.render output for every mod"))

    def test_agent_spawn_token(self):
        self.assertTrue(admitted("someone/teams", "Wraps agent.spawn"))

    def test_name_alone_is_never_enough(self):
        # Naming the host is not evidence of using the mod capability. Naming
        # the mod surface is: "the repository says it is a mod" is evidence the
        # reader of this list accepts, so `claude-mods` qualifies and
        # `claude-toolkit` does not.
        self.assertFalse(admitted("someone/claude-toolkit",
                                  "Utilities for working with Claude Code"))
        self.assertFalse(admitted("someone/cc-plugin-toolkit",
                                  "A toolkit for Claude Code"))
        self.assertFalse(admitted("someone/claude-config",
                                  "My Claude Code configuration"))

    def test_generic_claude_name_alone_is_not_enough(self):
        # A name is not a claim: hundreds of repositories are called
        # claude-something without extending the client's mod layer.
        self.assertFalse(admitted("someone/claude-notes",
                                  "Notes about using Claude Code"))

    def test_hook_plus_platform(self):
        self.assertTrue(admitted("someone/guard",
                                 "A Claude Code mod that blocks risky shell commands"))

    def test_skill_plus_platform_is_out_of_scope(self):
        self.assertFalse(admitted("someone/skills", "Claude Code skills collection"))

    def test_topic_corroboration(self):
        # A topic alone does not admit; the description has to carry the signal.
        self.assertTrue(admitted("someone/thing", "A mod for Claude Code",
                                 ("claude-code-mod",)))


class TestRejects(unittest.TestCase):
    """Every family that actually polluted the candidate set."""

    def test_minecraft(self):
        for desc in ("A Minecraft mod loader",
                     "Forge mod for Minecraft 1.20",
                     "Modrinth client for browsing modpacks",
                     "CurseForge mod manager"):
            with self.subTest(desc=desc):
                self.assertFalse(admitted("someone/mc-tool", desc))

    def test_game_modding_other(self):
        for desc in ("Skyrim mod manager", "Factorio mod portal",
                     "RimWorld modding framework", "Terraria mod loader",
                     "GarrysMod server tools", "Steam Workshop downloader"):
            with self.subTest(desc=desc):
                self.assertFalse(admitted("someone/gamemod", desc))

    def test_moderation(self):
        for desc in ("Discord moderation bot with automod",
                     "Reddit moderator toolkit",
                     "Twitch chat mod commands",
                     "A moderation queue for forums"):
            with self.subTest(desc=desc):
                self.assertFalse(admitted("someone/modbot", desc))

    def test_arithmetic(self):
        for desc in ("Modular arithmetic library in Rust",
                     "Fast modulo calculator",
                     "modpow and modinv primitives"):
            with self.subTest(desc=desc):
                self.assertFalse(admitted("someone/mathlib", desc))

    def test_apache_namespace(self):
        for name, desc in (("someone/mod_python", "Python in Apache"),
                           ("someone/mod_wsgi", "WSGI adapter"),
                           ("someone/mod_rewrite", "Rewrite rules"),
                           ("someone/mod_security", "WAF rules")):
            with self.subTest(name=name):
                self.assertFalse(admitted(name, desc))

    def test_substring_traps_are_not_matches(self):
        # `\bmods?\b` cannot match these, and they must not be dragged in by a
        # looser pattern.
        for desc in ("A Node modules manager",
                     "Modern CSS framework",
                     "Model Context Protocol server",
                     "Modify JSON in place",
                     "Commodity price tracker"):
            with self.subTest(desc=desc):
                self.assertFalse(admitted("someone/thing", desc))

    def test_platform_word_alone_is_not_enough(self):
        # The self-pairing bug: "claude" was in both the medium set and the
        # pairing set, so it justified itself and this was admitted.
        self.assertFalse(admitted("someone/paintings",
                                  "Classifies Claude Monet paintings"))
        self.assertFalse(admitted("someone/name", "A dataset of French names"))

    def test_unrelated_plugin_hosts(self):
        for desc in ("A WordPress plugin for SEO",
                     "Vim plugin for fuzzy finding",
                     "Figma plugin that exports tokens",
                     "A webpack plugin"):
            with self.subTest(desc=desc):
                self.assertFalse(admitted("someone/plugin", desc))

    def test_unrelated_hooks(self):
        for desc in ("React hooks for forms", "Git hook manager",
                     "Webhook relay service"):
            with self.subTest(desc=desc):
                self.assertFalse(admitted("someone/hooks", desc))

    def test_topic_stuffing_alone_is_not_enough(self):
        # A high-star link list carrying a Claude topic it has no use for.
        self.assertFalse(admitted("someone/anything-about-game",
                                  "A curated list about game development",
                                  ("claude", "claude-code")))

    def test_self(self):
        self.assertFalse(admitted("wh000wh000/awesome-claude-mods",
                                  "This list"))


class TestRuleShape(unittest.TestCase):
    """Properties of the sets, not individual cases."""

    def test_sets_are_disjoint(self):
        """
        A term must not justify itself.

        This is the regression that admitted "Claude Monet": `claude` sat in
        both the evidence set and the platform set, so it justified itself and
        any sentence containing the word passed. The two sets must stay
        disjoint for the rule to mean anything.
        """
        surface = set(curate.MOD_SURFACE_PATTERNS)
        platform = set(curate.PLATFORM_PATTERNS)
        self.assertFalse(surface & platform,
                         "an evidence pattern must not also be a platform pattern")

    def test_bare_mod_is_never_strong(self):
        for text in ("mod", "mods", "a mod for something"):
            with self.subTest(text=text):
                self.assertFalse(curate.any_match(curate.STRONG_PATTERNS, text))

    def test_bare_mod_without_platform_is_not_medium(self):
        for text in ("mod loader", "plugin for wordpress", "hooks for react"):
            with self.subTest(text=text):
                self.assertFalse(curate.medium_signal(text))

    def test_mod_with_platform_is_medium(self):
        for text in ("mod for claude", "cordis mod", "dsh plugin",
                     "claude code mods"):
            with self.subTest(text=text):
                self.assertTrue(curate.medium_signal(text))


class TestCurateIsDeterministic(unittest.TestCase):
    """The pipeline rule: no model in the curation loop."""

    def test_no_network_or_model_imports(self):
        src = (SCRIPTS / "curate.py").read_text()
        # Checked as code, not as vocabulary: "anthropic" is a domain word this
        # list is about, and banning the string would ban the subject.
        for banned in ("import openai", "import anthropic", "import requests",
                       "urllib.request", "http_json(", "guildos"):
            with self.subTest(banned=banned):
                self.assertNotIn(banned, src,
                                 f"curate.py must stay offline and model-free")

    def test_double_run_is_identical(self):
        """
        Two runs over the same input must produce byte-identical output.

        This is the property that makes every diff reviewable. If it fails, a
        model or a random source has crept into the loop.
        """
        path = SCRIPTS.parent / "data" / "entries.json"
        if not path.exists():
            self.skipTest("no entries.json yet; run curate once first")
        # Run it twice here rather than comparing against whatever happened to
        # be on disk: after a rule change the stored file is from the old rules,
        # and the first run legitimately differs.
        import json as _json

        def stable() -> str:
            """The decision, with the clock removed.

            `generated_at` is a timestamp and legitimately differs between runs;
            what must not differ is which entries were chosen, how they were
            graded and the order they appear in.
            """
            doc = _json.loads(path.read_text())
            return _json.dumps(
                [{k: v for k, v in e.items() if k not in
                  # Fields that describe the transition from the previous
                  # snapshot rather than the entry itself. stars_delta is the
                  # clearest: on the first run it measures against the published
                  # state, on the second against the first run's own output, so
                  # it is 1 then 0 without anything having changed. seen_count,
                  # last_seen and is_new are the same shape.
                  ("last_seen", "generated_at", "updated_at", "seen_count",
                   "stars_delta", "is_new", "history")}
                 for e in doc["entries"]], sort_keys=True, ensure_ascii=False)

        first_run = subprocess.run([sys.executable, str(SCRIPTS / "curate.py")],
                                   capture_output=True, text=True)
        self.assertEqual(first_run.returncode, 0, first_run.stderr[-600:])
        snapshot = stable()
        second_run = subprocess.run([sys.executable, str(SCRIPTS / "curate.py")],
                                    capture_output=True, text=True)
        self.assertEqual(second_run.returncode, 0, second_run.stderr[-600:])
        self.assertEqual(snapshot, stable(),
                         "curate.py is not deterministic: two runs over the "
                         "same input chose different entries")


if __name__ == "__main__":
    unittest.main(verbosity=2)