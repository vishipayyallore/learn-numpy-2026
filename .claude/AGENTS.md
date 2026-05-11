# AGENTS.md — Claude Code Supplement

Claude-specific guidance for **learn-numpy-2026**. Baseline policy lives in root **`AGENTS.md`**
and **`CLAUDE.md`**.

---

## Naming and Numbering

- Two-digit prefixes starting at **`01`**: `01_arrays.ipynb`, `01_shapes.py`, `01-topic/`.
- **`00_` / `00-` prefixes are forbidden** for numbered learning artifacts.

---

## Responsibilities

1. Preserve notebook and exercise flow unless the task explicitly restructures.
2. Prefer minimal diffs; ask before large refactors.
3. Run the quality commands in root **`AGENTS.md`** before marking work complete.

---

## Source Intake

`source-material/` (when present, often gitignored) is **read-only intake**. Output must be
**transformative**: new wording, examples, and structure. Never copy transcript- or book-length
blocks into publish paths.

---

## Precedence (Claude tie-break)

When root **`AGENTS.md`** “Notes” section does not resolve a conflict:

1. Current user message.
2. Root **`CLAUDE.md`**.
3. Root **`AGENTS.md`**.
4. This file.
5. `.claude/rules/*.md`.
6. `.cursor/rules/`.
7. `.github/copilot-instructions.md`.
8. Root **`skills.md`** and **`.claude/skills.md`**.

---

## Required Checks

Match root **`AGENTS.md`** (ruff via `uvx` if `ruff` is not installed as a project dep, compileall,
markdownlint, pytest when applicable).
