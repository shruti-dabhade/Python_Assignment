import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-"*40
 
###################################################################################
# Step 5 : Training vs Testing Accuracy
###################################################################################
print(Border)
print("Step 5 : Overfitting / Underfitting Check")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_acc = accuracy_score(y_train, train_pred)
test_acc = accuracy_score(y_test, test_pred)

print("Training Accuracy :", train_acc * 100)
print("Testing Accuracy :", test_acc * 100)

if train_acc > test_acc:
    print("Model may be Overfitting")
else:
    print("Model is Generalizing well")