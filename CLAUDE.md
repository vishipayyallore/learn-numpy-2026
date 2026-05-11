# Claude Code Instructions — Learn NumPy (2026)

**Project:** learn-numpy-2026  
**Purpose:** Structured hands-on learning for NumPy — notebooks, exercises, small libraries in
`src/`, tests, and notes.

Read this file together with root **`AGENTS.md`** (checks, intake policy, precedence). For
Claude-specific supplements, see **`.claude/AGENTS.md`**, **`.claude/skills.md`**, and
**`.claude/rules/`**.

---

## Critical Rules

1. **Original learning content** — Do not copy long verbatim passages from third-party tutorials or
   intake notes. Teach with fresh examples; see `.cursor/rules/01_numpy-learning-rules.mdc`.
2. **Preserve structure** — Read the full file before editing. Make minimal, targeted changes.
3. **Ask before risky edits** — Large notebook rewrites or mass renames need explicit scope.
4. **Numbering** — Learning artifacts start at **`01_`** / **`01-`**; never **`00_`**.

---

## Internal Intake (`source-material/`)

If present (often gitignored), use it only as **inspiration**. Rewrite completely for notebooks,
`notes/`, and README. Do not link `source-material/` from learner-facing files.

---

## Repository Layout (quick reference)

Authoritative detail: root **`README.md`**. Typical areas:

- `notebooks/` — concept walkthroughs
- `src/` — reusable helpers
- `exercises/` — practice scripts
- `tests/` — automated checks
- `datasets/` — small data for examples

---

## Python and NumPy

- Prefer clear **shapes**, **dtypes**, and **vectorized** code in examples.
- Keep dependencies aligned with **`pyproject.toml`**; add `numpy` (and dev tools) explicitly when
  you introduce imports or CI.

---

## Quality Commands

See root **`AGENTS.md`**. Prefer `uvx ruff` / `uvx pytest` when tools are not yet project
dependencies.

---

## Related Files

- **Cursor rules:** `.cursor/rules/`
- **Claude supplements:** `.claude/AGENTS.md`, `.claude/skills.md`, `.claude/rules/`
- **Copilot:** `.github/copilot-instructions.md`
- **Skill index:** `skills.md`
