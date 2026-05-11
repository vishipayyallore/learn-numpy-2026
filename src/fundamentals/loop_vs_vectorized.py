"""Fundamentals: range basics and NumPy vectorized multiplication."""

import numpy as np


def main() -> None:
    print("The Power of NumPy")

    print("range(0, 5) ->", list(range(0, 5)))
    print("range(0, 5, 2) ->", list(range(0, 5, 2)))

    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]

    # Python lists need an explicit loop for element-wise multiplication.
    new_list: list[int] = []
    for i in range(len(list1)):
        new_list.append(list1[i] * list2[i])
    print("Element-wise with loop ->", new_list)

    x = np.array([1, 3, 5, 7, 9])
    y = np.array([2, 4, 6, 8, 10])

    print("type(x) ->", type(x))
    print("NumPy vectorized multiply ->", x * y)


if __name__ == "__main__":
    main()
