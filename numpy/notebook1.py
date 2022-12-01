import numpy as np
climate_data = [[11,12,13],
                [13,14,15],
                [15,16,17],
                [17,18,19]]
climate_data_np = np.array(climate_data)
print(climate_data_np.shape)

array3d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(array3d.shape)

weights = np.array([1,2,3])
print(weights.dtype)

weights2 = np.array([1,2,3,5.5])
print(weights2.dtype)
  
