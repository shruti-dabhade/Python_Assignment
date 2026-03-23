"""4. Model Evaluation:
• Print accuracy score, confusion matrix, precision, recall, and F1 score.
• Use matplotlib or seaborn to visualize confusion matrix"""

import numpy as np
from sklearn.preprocessing import StandardScaler
import math

#---------------------------------------------
# step 1 : create dataset
#---------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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
# step 3 : train model
#---------------------------------------------

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

#---------------------------------------------
# step 4 : prediction
#---------------------------------------------

Y_pred = model.predict(X_test)

#---------------------------------------------
# step 5 : evaluation
#---------------------------------------------

print("Accuracy : ", accuracy_score(Y_test,Y_pred))
print("Confusion Matrix : ")
print(confusion_matrix(Y_test,Y_pred))
print("Classification Report : ")
print(classification_report(Y_test,Y_pred))