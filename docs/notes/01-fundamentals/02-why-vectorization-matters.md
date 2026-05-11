# Why Vectorization Matters

This note shows why NumPy is preferred for numerical operations.

## Quick Range Refresher

`range(start, stop, step)` generates numbers from `start` to `stop - 1`.

```python
print(list(range(0, 5)))      # [0, 1, 2, 3, 4]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
```

The stop value is excluded, similar to Python slicing behavior.

## Problem: Multiply Two Sequences Element-Wise

Given two lists:

```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
```

Direct multiplication does not perform element-wise math:

```python
# list1 * list2  # TypeError
```

## Pure Python Approach

You can solve it using a loop:

```python
result = []

for i in range(len(list1)):
    result.append(list1[i] * list2[i])

print(result)  # [2, 12, 30, 56, 90]
```

This works, but for larger numerical workloads it becomes verbose and less efficient.

## NumPy Approach

NumPy performs element-wise operations directly:

```python
import numpy as np

a = np.array([1, 3, 5, 7, 9])
b = np.array([2, 4, 6, 8, 10])

print(a * b)  # [ 2 12 30 56 90]
```

No manual indexing is required.

## Why This Is Better

NumPy gives:

- simpler code for vector math
- better performance on large arrays
- a standard workflow used in data science and ML

## Key Takeaway

Use plain Python loops when learning fundamentals or handling general-purpose logic.

Use NumPy arrays when working with numerical vectors and matrices, especially when operations apply to entire arrays.

## Related Artifacts

- Executable companion: `src/01-fundamentals/01-loop-vs-vectorized.py`
- Prior note in this track: `01-what-is-numpy.md`
