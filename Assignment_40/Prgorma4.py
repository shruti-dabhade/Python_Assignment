import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-"*40

###################################################################################
# Step 4 : Predict New Students
###################################################################################
print(Border)
print("Step 4 : Prediction for New Students")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

new_students = pd.DataFrame({
    "StudyHours":[2,5,7,1,6],
    "Attendance":[60,85,90,50,88],
    "PreviousScore":[55,78,88,40,80],
    "AssignmentsCompleted":[3,8,9,2,7],
    "SleepHours":[6,7,6,5,7]
})

pred = model.predict(new_students)

print("Predictions :", pred)