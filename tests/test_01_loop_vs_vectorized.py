from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_loop_vs_vectorized_script_output() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "src/01-fundamentals/01-loop-vs-vectorized.py"

    result = subprocess.run(
        [sys.executable, str(script_path)],
        check=True,
        capture_output=True,
        text=True,
    )

    output = result.stdout
    assert "The Power of NumPy" in output
    assert "Element-wise with loop -> [2, 12, 30, 56, 90]" in output
    assert "NumPy vectorized multiply -> [ 2 12 30 56 90]" in output
