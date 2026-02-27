import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

Border = "-"*40
 
###################################################################################
# Step 4 : Confusion Matrix
###################################################################################
print(Border)
print("Step 4 : Confusion Matrix")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

plt.show()

print("True Positive  : Correctly predicted Pass")
print("True Negative  : Correctly predicted Fail")
print("False Positive : Predicted Pass but actually Fail")
print("False Negative : Predicted Fail but actually Pass")