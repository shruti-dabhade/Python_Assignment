"""2. Data Preprocessing:
• Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
• Apply feature scaling using StandardScaler or MinMaxScaler.
• Split the dataset into features (X) and target (y)."""

import pandas as pd
from sklearn.preprocessing import StandardScaler

#---------------------------------------------
# step 1 : load dataset
#---------------------------------------------

df = pd.read_csv("diabetes.csv")

#---------------------------------------------
# step 2 : handle zero values
#---------------------------------------------

df.replace(0, df.mean(), inplace=True)

#---------------------------------------------
# step 3 : separate features and target
#---------------------------------------------

X = df.drop("Outcome", axis=1)
Y = df["Outcome"]

#---------------------------------------------
# step 4 : feature scaling
#---------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Scaled Data : ")
print(X_scaled)