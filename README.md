# Learn Numpy in 2026

> A structured hands-on journey to learn NumPy through notebooks, exercises, topic-organized `src/` scripts, and real-world numerical computing examples.

---

# Overview

This repository documents my 2026 learning journey into
NumPy — the foundational numerical computing library used across:

* Data Science
* Machine Learning
* Artificial Intelligence
* Scientific Computing
* Deep Learning
* High-performance numerical processing

The goal of this repository is not only to learn NumPy APIs, but also to develop a strong understanding of:

* vectorized computation,
* multidimensional arrays,
* numerical transformations,
* broadcasting,
* linear algebra,
* performance-oriented programming,
* and scientific Python workflows.

---

# Repository Structure

Content is organized in layers so you can answer “where is the idea?” and “where do I run it?” without `day1/` / `day2/` folders. **`docs/notes/`, `notebooks/`, and `src/` share the same numbered topic folders** (`01-fundamentals` … `05-linear-algebra`) so progression and navigation stay aligned. Inside each topic, scripts use `01-`, `02-`, … for a clear reading order. **Day-to-day progress** belongs in `journal/YYYY-MM-DD.md` (not in `.py` filenames unless you deliberately want that style).

| Layer | Role |
| --- | --- |
| Conceptual | `docs/notes/` — theory, comparisons, summaries (topic folders, co-located `images/` per topic when needed) |
| Interactive | `notebooks/` — runnable walkthroughs, same topic numbering as notes |
| Executable | `src/NN-topic/` — runnable scripts (e.g. `01-…py`); run with `python path/to/script.py` (leading digits are for humans, not import paths) |
| Chronology | `journal/` — dated log of programs run, notes read, and takeaways |
| Practice | `exercises/` — short drills (`01_` naming when you add scripts) |
| Reference | `docs/diagrams/`, `docs/cheatsheets/`, repo `README` and external docs |
| Data | `datasets/` — tiny files for examples |
| Quality | `tests/` — checks for non-trivial `src/` helpers |

Suggested flow for a new topic: read the matching note under `docs/notes/NN-topic/`, try `notebooks/NN-topic/`, run or extend code under `src/NN-topic/`, optionally append `journal/`, then reinforce in `exercises/`.

```text
learn-numpy-2026/
│
├── journal/
│
├── docs/
│   ├── notes/
│   │   ├── 01-fundamentals/
│   │   ├── 02-array-operations/
│   │   ├── 03-broadcasting/
│   │   ├── 04-reshape/
│   │   └── 05-linear-algebra/
│   ├── diagrams/
│   ├── cheatsheets/
│   └── images/
│
├── notebooks/
│   ├── 01-fundamentals/
│   ├── 02-array-operations/
│   ├── 03-broadcasting/
│   ├── 04-reshape/
│   └── 05-linear-algebra/
│
├── src/
│   ├── 01-fundamentals/
│   ├── 02-array-operations/
│   ├── 03-broadcasting/
│   ├── 04-reshape/
│   └── 05-linear-algebra/
│
├── exercises/
├── datasets/
├── tests/
└── README.md
```

Add `06-…`, `07-…`, … under all three roots when you introduce statistics, random, performance, or larger projects.

Optional local intake notes stay out of version control; see `.gitignore` if you use that workflow.

---

# Topics Covered

## NumPy Fundamentals

* ndarray
* array creation
* indexing and slicing
* reshaping
* flattening
* iteration

## Mathematical Operations

* vectorized computation
* aggregation
* statistics
* universal functions (ufuncs)
* broadcasting

## Linear Algebra

* matrices
* dot products
* matrix multiplication
* determinants
* eigenvalues
* decompositions

## Advanced Concepts

* memory layout
* views vs copies
* performance optimization
* structured arrays
* random module
* numerical stability

---

# Learning Approach

This repository follows a hybrid learning model:

* `.ipynb` notebooks for interactive exploration
* `.py` scripts under `src/NN-topic/` for disciplined coding practice (`01-`, `02-`, … inside each topic; dates only in `journal/` unless you choose otherwise)
* `journal/` entries when you want a dated trail across topics
* exercises for reinforcement
* mini-projects for applied learning (as larger scripts or notebook sequences when you add them)

The emphasis is on:

* conceptual clarity,
* implementation detail,
* and practical engineering usage.

---

# Setup

## Clone Repository

```bash id="6t0j7p"
git clone https://github.com/vishipayyallore/learn-numpy-2026.git
cd learn-numpy-2026
```

## Create Virtual Environment

```bash id="w8d0lo"
python -m venv .venv
```

## Activate Environment

### Windows

```bash id="85f6v7"
.venv\Scripts\activate
```

### Linux / macOS

```bash id="h4eqi2"
source .venv/bin/activate
```

## Install Dependencies

```bash id="r7q64m"
pip install numpy jupyter matplotlib pandas
```

---

# Running Jupyter Notebook

```bash id="1nzhf9"
jupyter lab
```

or

```bash id="ijw2b1"
jupyter notebook
```

---

# Example

```python id="x3mwmt"
import numpy as np

arr = np.arange(12)

matrix = arr.reshape(3, 4)

print(matrix)
```

Output:

```text id="b7n7ku"
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

---

# Why NumPy?

NumPy is the computational foundation behind much of the modern Python AI/ML ecosystem, including:

* Pandas
* SciPy
* scikit-learn
* TensorFlow
* PyTorch

Understanding NumPy deeply improves:

* data manipulation skills,
* ML intuition,
* numerical reasoning,
* and performance engineering.

---

# Goals

* Build strong numerical computing foundations
* Master vectorized thinking
* Understand multidimensional data manipulation
* Prepare for advanced ML and AI workflows
* Develop performance-conscious Python programming habits

---

# References

* [NumPy Documentation](https://numpy.org/doc/?utm_source=chatgpt.com)
* [JupyterLab](https://jupyter.org/?utm_source=chatgpt.com)
* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)

---

# License

This repository is intended for educational and learning purposes.
