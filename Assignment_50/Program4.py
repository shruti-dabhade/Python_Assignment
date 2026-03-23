"""4. Train Classification Models
◦ Train the following models:
▪ Logistic Regression
▪ K-Nearest Neighbors
▪ Random Forest Classifier"""

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

#---------------------------------------------
# step 1 : create models
#---------------------------------------------

log_model = LogisticRegression()
knn_model = KNeighborsClassifier()
rf_model = RandomForestClassifier()

#---------------------------------------------
# step 2 : train models
#---------------------------------------------

log_model.fit(X_train,Y_train)
knn_model.fit(X_train,Y_train)
rf_model.fit(X_train,Y_train)

print("Models trained successfully")