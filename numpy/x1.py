import numpy as np 
arr = np.array([[25.,76.,99.],
                [67.,87.,78.],
                [76.,67.,89.],
                [54.,67.,23.],
                [24.,43.,63.]])
multiplier = np.array([12.,45.,46.,])
print(arr.shape,multiplier.shape)
result = np.matmul(arr,multiplier)
print(result)
print(result.shape)
concatenated_result = np.concatenate((arr,result.reshape(5,1)),axis = 1)
print(concatenated_result)
 