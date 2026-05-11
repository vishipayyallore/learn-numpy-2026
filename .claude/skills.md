# skills.md — Claude Code Skill Index

Extends root **`skills.md`** with Claude-oriented notes for **learn-numpy-2026**.

See **`.claude/rules/README.md`** for rule supplements (including `source-material/` intake).

---

## Core Skills

1. **NumPy pedagogy** — short objectives, minimal runnable cells, then optional depth (broadcasting,
   linalg, dtypes, memory layout).
2. **Notebook hygiene** — clear section headings, deterministic seeds, shape annotations in text.
3. **Exercise design** — small `exercises/01_*.py` scripts that reinforce one idea each.
4. **Test-backed helpers** — when `src/` grows non-trivial functions, add focused `tests/`.
5. **Markdown quality** — `markdownlint-cli2` on README and any `docs/` / `notes/` paths that exist.
6. **Zero-copy intake** — transform any private notes in `source-material/`; never paste verbatim.

---

## Guardrails

- Do not reference **`source-material/`** in learner-facing markdown or notebook prose.
- Do not add long policy blocks about internal intake into README; keep that in agent instruction files.
- Match the repo’s **01-first** numbering; never introduce `00_` numbered learning files.

## Runnable skills vs repository instructions

There is no separate installable “source-material agent.” Intake expectations live in
**`AGENTS.md`**, **`.github/copilot-instructions.md`**, **`.cursor/rules/`**, and
**`.claude/rules/source-material-intake.md`**.
