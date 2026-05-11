The Power of NumPy
range(0, 5)
range(0, 5)
list(range(0, 5))
[0, 1, 2, 3, 4]
list(range(0, 5, 2))
[0, 2, 4]
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list1 * list2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-7c0157aad319> in <module>
----> 1 list1 * list2

TypeError: can't multiply sequence by non-int of type 'list'
new_list = []

for i in range(0, len(list1)):
    x = list1[i] * list2[i]
    new_list.append(x)

print(new_list)
[2, 12, 30, 56, 90]
import numpy as np
x = np.array([1, 3, 5, 7, 9])
y = np.array([2, 4, 6, 8, 10])
print(type(x))
<class 'numpy.ndarray'>
x * y
array([ 2, 12, 30, 56, 90])