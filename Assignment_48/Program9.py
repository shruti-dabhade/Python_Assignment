"""9. Write a Python program using scikit-learn to generate a classification report for the following data:
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]
Display the complete classification report including precision, recall, F1-score, and support."""

from sklearn.metrics import classification_report

#---------------------------------------------
# step 1 : create data
#---------------------------------------------

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

#---------------------------------------------
# step 2 : generate report
#---------------------------------------------

report = classification_report(actual, predicted)

#---------------------------------------------
# step 3 : display report
#---------------------------------------------

print("Classification Report : ")
print(report)