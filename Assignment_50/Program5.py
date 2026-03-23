"""5. Evaluate the Models
◦ Compare using:
▪ Accuracy
▪ Confusion Matrix
▪ Classification Report
▪ ROC-AUC score"""

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#---------------------------------------------
# step 1 : predictions
#---------------------------------------------

log_pred = log_model.predict(X_test)
knn_pred = knn_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

#---------------------------------------------
# step 2 : evaluate
#---------------------------------------------

print("Logistic Regression")
print(accuracy_score(Y_test,log_pred))
print(confusion_matrix(Y_test,log_pred))
print(classification_report(Y_test,log_pred))

print("KNN")
print(accuracy_score(Y_test,knn_pred))
print(confusion_matrix(Y_test,knn_pred))
print(classification_report(Y_test,knn_pred))

print("Random Forest")
print(accuracy_score(Y_test,rf_pred))
print(confusion_matrix(Y_test,rf_pred))
print(classification_report(Y_test,rf_pred))