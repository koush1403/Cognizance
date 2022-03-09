import numpy as np
nums = np.array([10,11,12,13,14])
print("original :")
print(nums)
p = 4
new_array = np.zeros(len(nums) + (len(nums)-1)*(p))
new_array[::p+1] = nums
print("\4 zeros array:")
print(new_array)