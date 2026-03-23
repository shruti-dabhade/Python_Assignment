"""3. Write a Python program using StandardScaler to perform feature scaling on the following dataset:
[[25,20000],
 [30,40000],
 [35,80000]]
Print the scaled dataset.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler

#---------------------------------------------
# step 1 : create dataset
#---------------------------------------------

data = np.array([[25,20000],
                 [30,40000],
                 [35,80000]])

print("Original Data : ")
print(data)

#---------------------------------------------
# step 2 : create scaler
#---------------------------------------------

scaler = StandardScaler()

#---------------------------------------------
# step 3 : fit and transform
#---------------------------------------------

scaled_data = scaler.fit_transform(data)

#---------------------------------------------
# step 4 : display result
#---------------------------------------------

print("Scaled Data : ")
print(scaled_data)