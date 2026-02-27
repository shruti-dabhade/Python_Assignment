import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-"*40
 
###################################################################################
# Step 1 : Train Decision Tree Model
###################################################################################
print(Border)
print("Step 1 : Training Decision Tree Model")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

print("Model trained successfully")