# GitHub Copilot Instructions — Learn NumPy (2026)

**Project:** learn-numpy-2026  
**Purpose:** Hands-on NumPy learning through notebooks, exercises, `src/` utilities, tests, and notes.

---

## Repository Overview

This repo is a **personal / cohort learning** space for NumPy in 2026. Typical layout (see root
`README.md` for the authoritative tree):

- `notebooks/` — concept walkthroughs (`01-…`, `02-…`, numbering starts at **01**).
- `src/<topic>/` — runnable learning scripts (topic folders; optional `journal/` for dated progress).
- `exercises/` — practice scripts.
- `tests/` — checks for non-trivial library code in `src/`.
- `notes/` or `docs/` — markdown explanations (create as needed).

There is **no** `src/Working/` or L1/S1 curriculum layout unless you add it explicitly.

---

## Content Rules

### Core Principles

- Make minimal, targeted changes. Read the full file before editing.
- If a change feels broad or risky, pause and ask.
- Preserve learner progression in numbered notebooks and exercises unless the task says otherwise.

### Zero-Copy and Originality

Explain concepts in **your own structure and examples**. Do not paste long verbatim excerpts from
books, paid courses, or third-party tutorials. Short attributed quotes are rare exceptions.

### Placement

Add new topics as the next numbered artifact (`05-…`) or an agreed folder name. Do not silently
overwrite completed milestone notebooks without maintainer approval in the task.

---

## Source Material Intake (`source-material/`)

If `source-material/` exists (often **gitignored**), it is **internal intake only**:

- Rewrite ideas; never ship intake text verbatim into README, `docs/`, `notes/`, or notebooks.
- Do not link or reference `source-material/` paths in learner-facing files.

There is **no** separate Copilot agent scoped only to `source-material/`. These rules apply to
**every** edit in this repository.

---

## NumPy Guidance

- Prefer **vectorized** operations and clear **shape** / **dtype** commentary when it helps.
- Use `np.random.default_rng(seed)` for reproducible random examples.
- Keep examples small enough to run quickly on a laptop.

---

## Quality Checklist

Before completing a task that touches Python or markdown:

- `uvx ruff check src exercises tests` (narrow paths if folders do not exist yet)
- `python -m compileall -q src exercises tests` (same caveat)
- `pytest` when `tests/` contains tests
- `npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md" "notes/**/*.md"`
  (omit globs for missing folders)

---

## Precedence

If guidance conflicts: root **`README.md`** (structure) → this file → root **`CLAUDE.md`** →
root **`AGENTS.md`** → `.cursor/rules/` → `.claude/` supplements.
