import numpy as np
a = np.random.randint(0,3,6)
print("1st array:")
print(a)
b = np.random.randint(0,3,6)
print("2nd array:")
print(b)
print("arrays are equal or not")
array_equal = np.allclose(a, b)
print(array_equal)