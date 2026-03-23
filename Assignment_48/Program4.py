"""4. Write a Python program to calculate the Euclidean distance between two points before and after applying 
feature scaling, and explain the difference in results"""

import numpy as np
from sklearn.preprocessing import StandardScaler
import math

#---------------------------------------------
# step 1 : create dataset
#---------------------------------------------

data = np.array([[25,20000],
                 [30,40000]])

#---------------------------------------------
# step 2 : distance before scaling
#---------------------------------------------

p1 = data[0]
p2 = data[1]

dist_before = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))

print("Distance before scaling : ", dist_before)

#---------------------------------------------
# step 3 : apply scaling
#---------------------------------------------

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

#---------------------------------------------
# step 4 : distance after scaling
#---------------------------------------------

sp1 = scaled_data[0]
sp2 = scaled_data[1]

dist_after = math.sqrt(((sp1[0]-sp2[0])**2) + ((sp1[1]-sp2[1])**2))

print("Distance after scaling : ", dist_after)