import numpy as np
#temperature, rainfall , humidity
climate_data = np.array([[73,67,43],
                         [91,88,64],
                         [87,134,58],
                         [102,43,37],
                         [69,96,70]])
weights = np.array([0.3,0.2,0.5])
result = np.matmul(climate_data,weights)
result2 = climate_data @ weights
print(result,result2)