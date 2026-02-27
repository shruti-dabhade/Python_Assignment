import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

Border = "-"*40
 
###################################################################################
# Complete Machine Learning Program
###################################################################################
print(Border)
print("Student Performance Prediction using Decision Tree")
print(Border)

# 1. Load Dataset
df = pd.read_csv("student_performance_ml.csv")
print("Dataset Loaded Successfully")

# 2. Basic Analysis
print("\nFirst 5 Records")
print(df.head())

# 3. Visualization
plt.hist(df["StudyHours"])
plt.title("StudyHours Distribution")
plt.show()

# 4. Train-Test Split
X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Model Training
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 6. Prediction
y_pred = model.predict(X_test)

# 7. Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy :", accuracy * 100)

# 8. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

# 9. Conclusion
print("\nConclusion :")
print("Decision Tree model can predict student performance based on input features.")