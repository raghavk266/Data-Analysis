import numpy as np 
arr1 = np.array([ [1,2,3],
                [4,5,6],
                [7,8,9]])

arr2 = np.array( [[1,2,3],
                 [4,5,6],
                 [6,7,8]])
# vector operations
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1%arr2)
print(arr1/arr2)
print(arr1//arr2)
print(arr1 @ arr2)
#scalar operations
print(arr1 + 2)
print(arr1 *4)
print(arr1%1)
print(arr1**6)
print(arr1**arr2)
#relational operations
print(arr1==arr2)
print(arr1>arr2)
print(arr1<arr2)
print(arr1!=arr2)