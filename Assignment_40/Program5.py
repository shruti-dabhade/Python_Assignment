import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-"*40

###################################################################################
# Step 5 : Manual Accuracy Calculation
###################################################################################
print(Border)
print("Step 5 : Manual Accuracy")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

correct = (y_test == y_pred).sum()
accuracy = correct / len(y_test)

print("Manual Accuracy :", accuracy)