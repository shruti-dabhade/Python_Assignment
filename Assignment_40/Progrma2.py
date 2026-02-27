import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-"*40

###################################################################################
# Step 2 : Remove SleepHours Feature
###################################################################################
print(Border)
print("Step 2 : Remove SleepHours Feature")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

df = df.drop("SleepHours", axis=1)

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, y_pred))