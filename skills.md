# skills.md

Repository-level skill index for contributors and AI assistants — **Learn NumPy (2026)**.

## Core Skills

1. **NumPy fundamentals** — ndarray creation, indexing, slicing, reshaping, views vs copies.
2. **Broadcasting and vectorization** — teach loop-free patterns with small, inspectable arrays.
3. **Notebook-first learning** — one main idea per section; reproducible `default_rng(seed)`.
4. **Exercise scripts** — `exercises/01_*.py` style; runnable from repo root with `uv run`.
5. **Tests for helpers** — when `src/` grows logic, mirror with `tests/test_*.py`.
6. **Markdown quality** — headings, links, and `markdownlint-cli2` on paths listed in `AGENTS.md`.
7. **Zero-copy intake** — transform private `source-material/`; never ship verbatim source text.

## Guardrails

- Treat optional **`source-material/`** as internal; do not reference it in public-facing docs.
- **No `00_` numbered** learning files; start at **`01`**.
- Do not paste internal agent policy blocks into README or notebooks; keep policy in
  `AGENTS.md`, `.cursor/rules/`, `.github/`, `.claude/`.

## Policy vs runnable skills

Intake and originality expectations live in **repository instruction files** (`AGENTS.md`,
`CLAUDE.md`, `.github/copilot-instructions.md`, `.cursor/rules/`, `.claude/`) — not in a separate
installable skill binary.

Root **`skills.md`** is the canonical index; **`.claude/skills.md`** extends it for Claude Code.
