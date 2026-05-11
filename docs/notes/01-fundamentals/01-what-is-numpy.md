# What Is NumPy?

NumPy is the core numerical computing library in Python.

If Python gives us general-purpose programming tools, NumPy gives us fast tools for working with numbers and arrays at scale.

## What Is A Python Library?

A library is a collection of reusable code.

In practice, this means you can import tested modules instead of writing every utility from scratch.

## Why NumPy Matters

NumPy is short for **Numerical Python**. It is widely used in:

- data analysis
- machine learning
- scientific computing
- numerical simulations

NumPy is essential because it combines two important ideas:

- compact storage for numerical data
- fast vectorized operations

## NumPy Arrays Vs Python Lists

Python lists are flexible and can store mixed types.

NumPy arrays are usually **homogeneous** (same data type in an array), which allows lower overhead and faster computation.

Example:

```python
import numpy as np

py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5], dtype=np.int64)

print(type(py_list))   # <class 'list'>
print(type(np_array))  # <class 'numpy.ndarray'>
```

## Performance Mindset

With NumPy, we try to think in terms of whole-array operations instead of element-by-element loops.

That approach gives us:

- cleaner code
- fewer manual loops
- better performance for large datasets

## Key Takeaway

NumPy is not just another package.

It is the foundation for numerical work in Python, and learning it early makes later topics like pandas, machine learning, and linear algebra much easier.

## Related Artifacts

- Executable companion: `src/01-fundamentals/01-loop-vs-vectorized.py`
- Next note in this track: `02-why-vectorization-matters.md`
