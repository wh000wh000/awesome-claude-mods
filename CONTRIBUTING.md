# Contributing

Corrections are the fastest way to improve this list, and they are genuinely
welcome. Open an issue; that is the whole process.

## Suggesting a mod

Open an issue with the repository URL and a sentence on what it changes. A
suggestion bypasses the relevance filter.

It does **not** bypass evidence grading. Somebody saying "include this" is not
the same as verifying what a project does, so a suggested entry still lands at
`inferred` unless its own text names part of the mod surface.

## What belongs here, and what does not

The subject is the layer Claude Code gained in **2.1.287**, when plugins became
able to modify deeper behaviour and draw their own interface.

**In scope:** mods, the plugin and hook surface they build on, the panes, bands,
cards and status lines drawn through it, and the DSH and Cordis equivalents.

**Out of scope:** the wider Claude Code ecosystem. A prompt pack is not a mod, a
skills collection is not a mod, and an agent framework is not a mod. Those are
well covered elsewhere; this list is deliberately narrower.

## Reporting a misfiled or wrongly excluded entry

Two cases are worth reporting.

**A mod was wrongly excluded.** This is the most likely failure of an automated
filter and the most valuable report. The word "mod" is one of the most overloaded
tokens in software, so the rules exclude game modding, moderation tooling,
modular arithmetic and Apache's `mod_*` namespace by pattern. If a genuine mod
was caught by one of those, say so — it is the failure mode that matters most.

**An entry is mis-graded.** The grades mean something specific:

| Grade | Claim |
| --- | --- |
| `official` | published by Anthropic, or read from the official changelog |
| `observed` | its own text names part of the mod surface — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, a pane, band or card |
| `inferred` | it calls itself a mod, plugin or hook, but nothing names that surface |
| `unverified` | matched on vocabulary alone |

If an entry deserves a better grade, the most useful thing you can send is a
link to the file or the line that proves it.

## Reporting a broken asset

Cards show a screenshot and, where one exists, a recording taken from the
project's own README. Two rules apply:

- Assets are bundled only when the project declares a redistribution-friendly
  licence. Otherwise the upstream URL is linked and the card says so.
- Every bundled asset is capped by size and format; a recording that exceeds the
  cap is linked rather than copied.

If an asset of yours appears here and you would rather it did not, open an issue
and it will be removed. If a card shows the wrong image, that is almost always
because the project's README has several candidates and the heuristic picked a
less useful one — say which file it should be and that becomes an override.

## Translations

Corrections from native speakers are especially welcome. Say which edition and
which string. Identifiers such as `ui.render`, `agent.spawn`, `Client`, `Cordis`
and `DSH` are kept verbatim on purpose and should not be translated.