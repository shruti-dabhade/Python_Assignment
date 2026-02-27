import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-"*40
 
###################################################################################
# Step 6 : Compare max_depth
###################################################################################
print(Border)
print("Step 6 : Decision Tree Depth Comparison")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

depths = [1, 3, None]

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("max_depth =", depth, "Testing Accuracy =", acc * 100)