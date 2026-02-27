import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-"*40
 
###################################################################################
# Step 7 : Predict New Student
###################################################################################
print(Border)
print("Step 7 : New Student Prediction")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

new_student = [[6, 85, 66, 7, 7]]

result = model.predict(new_student)

if result[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")