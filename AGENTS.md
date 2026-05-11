# AGENTS.md

Repository agent guidance for automation and AI assistants — **Learn NumPy (2026)**.

## Naming and Numbering Conventions

- Sequential learning files use a two-digit prefix: `01_name.py`, `01-arrays.ipynb`, `01-topic/`.
- **Numbers must start at `01`, never `00`.** Files and folders prefixed `00_` or `00-` are forbidden.
- Support folders with no natural sequence (`datasets/`, `references/`) may omit a numeric prefix.

## Default Agent Responsibilities

1. Preserve existing learning structure and notebook progression unless the task says otherwise.
2. Make minimal, targeted edits unless broader refactors are explicitly approved.
3. Validate code and docs quality before finishing work.

## Required Checks Before Completion

When your change touches Python under `src/`, `exercises/`, or `tests/`:

- `uvx ruff check src exercises tests` (use only paths that exist)
- `python -m compileall -q src exercises tests`

When your change touches markdown:

- `npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md" "notes/**/*.md"`
  (omit globs for folders that do not exist yet)

When `tests/` contains tests:

- `pytest` (or `uv run pytest` if pytest is a project dependency)

**Optional:** If you add `tools/psscripts/docs-links.ps1` (Docker-based link checker), run it on
`README.md` and `docs/` before large doc releases.

## Source Intake Policy

- `source-material/` is an optional **internal, read-only** intake folder (list in `.gitignore` if you
  use it). Do not assume it exists in every clone.
- Publish-facing content must be **original and transformative** — no verbatim copying from intake
  notes, books, or course transcripts.

Intake rules apply to **every** assistant surface: root `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`,
`.github/copilot-instructions.md`, `.claude/`.

## Precedence (when instructions conflict)

1. Explicit instruction in the current user message.
2. Root **`README.md`** for intended repository layout (authoritative for this repo).
3. `.github/copilot-instructions.md`
4. Root `CLAUDE.md`
5. This file (`AGENTS.md`)
6. `.cursor/rules/` and `.claude/` supplements
7. Root `skills.md` / `.claude/skills.md`
8. Model defaults

There is **no** `docs/RepositoryStructure.md`, `src/Working/`, or meetup session table in this
repository unless you add them.

## Notes

This file complements `.github/copilot-instructions.md`, `CLAUDE.md`, and `.claude/` (including
`.claude/AGENTS.md`, `.claude/skills.md`, `.claude/rules/`).
