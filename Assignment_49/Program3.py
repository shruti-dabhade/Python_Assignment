"""3. Model Building:
Train at least 2 different algorithms on the dataset:
• Logistic Regression
• K-Nearest Neighbors (KNN)
• Decision Tree 
• Use train_test_split to divide the data."""

import numpy as np
from sklearn.preprocessing import StandardScaler

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#---------------------------------------------
# step 1 : load dataset
#---------------------------------------------

df = pd.read_csv("diabetes.csv")

X = df.drop("Outcome", axis=1)
Y = df["Outcome"]

#---------------------------------------------
# step 2 : split dataset
#---------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#---------------------------------------------
# step 3 : create model
#---------------------------------------------

model = DecisionTreeClassifier()

#---------------------------------------------
# step 4 : train model
#---------------------------------------------

model.fit(X_train,Y_train)

print("Model Trained Successfully")