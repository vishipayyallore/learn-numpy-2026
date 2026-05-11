# Source material intake (`source-material/`)

## What this folder is

`source-material/` holds **internal, read-only** intake: rough notes, transcripts, or references.
It is **not** learner-facing and must not be copied into publish paths as-is.

The repository may list `source-material/` in **`.gitignore`**; clones may omit it. When present
locally, treat it as **author-only** input, not part of the shipped tutorial surface.

## Required behavior

1. **Transform, do not transcribe** — Rebuild explanations with new structure, voice, and examples.
2. **No verbatim blocks** — Do not paste from intake into `README`, `docs/`, `notes/`, or notebooks.
3. **No public citations of intake paths** — Do not link to `source-material/…` in learner-facing files.
4. **Placement** — Ideas inspired by intake go into the next appropriate **numbered** notebook,
   exercise, or note; do not silently replace completed milestones without approval.

## Where the full policy lives

- Root **`AGENTS.md`**
- **`.github/copilot-instructions.md`**
- **`.cursor/rules/01_numpy-learning-rules.mdc`** (NumPy + educational rules)
- Root **`CLAUDE.md`** and **`.claude/AGENTS.md`**
