#slicing and indexing 
import numpy as np
arr = np.array([[[1,2,3],[2,3,4]],[[1,1,2],[1,2,3]]])
print(arr[0,0,0])
print(arr[1:])
print(arr[1:, 0:1 , :2])
