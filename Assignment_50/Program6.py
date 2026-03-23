"""6. Visualize Results
◦ Plot confusion matrix and ROC curves"""

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

#---------------------------------------------
# step 1 : probability prediction
#---------------------------------------------

y_prob = log_model.predict_proba(X_test)[:,1]

#---------------------------------------------
# step 2 : ROC values
#---------------------------------------------

fpr, tpr, thresholds = roc_curve(Y_test, y_prob)

#---------------------------------------------
# step 3 : plot ROC curve
#---------------------------------------------

plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

#---------------------------------------------
# step 4 : AUC score
#---------------------------------------------

auc = roc_auc_score(Y_test, y_prob)
print("ROC-AUC Score : ", auc)