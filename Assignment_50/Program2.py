"""2. Preprocess the Data
◦ Convert categorical variables using Label Encoding or One-Hot Encoding.
◦ Scale numeric features (e.g., using StandardScaler)."""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

#---------------------------------------------
# step 1 : load dataset
#---------------------------------------------

df = pd.read_csv("bank.csv")

#---------------------------------------------
# step 2 : handle categorical data
#---------------------------------------------

le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

#---------------------------------------------
# step 3 : separate features and target
#---------------------------------------------

X = df.drop("y", axis=1)
Y = df["y"]

#---------------------------------------------
# step 4 : scaling
#---------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Preprocessing done")