"""Predict whether a news article is Fake or Real using text classification techniques. This assignment 
demonstrates the power of ensemble learning using a Voting Classifier with models like Logistic Regression, 
Decision Tree."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#=========================================================
# Part 1 : Data Preprocessing
#=========================================================

#---------------------------------------------
# step 1 : load datasets
#---------------------------------------------

fake = pd.read_csv("fake.csv")
true = pd.read_csv("true.csv")

#---------------------------------------------
# step 2 : add label column
#---------------------------------------------

fake["label"] = 0
true["label"] = 1

#---------------------------------------------
# step 3 : combine datasets
#---------------------------------------------

df = pd.concat([fake, true])

print("Shape of dataset : ", df.shape)

#---------------------------------------------
# step 4 : drop null values
#---------------------------------------------

df = df.dropna()

#---------------------------------------------
# step 5 : select useful column (text)
#---------------------------------------------

X = df["text"]
Y = df["label"]

#=========================================================
# Part 2 : Feature Extraction
#=========================================================

#---------------------------------------------
# step 1 : TF-IDF vectorization
#---------------------------------------------

vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

#=========================================================
# Part 3 : Train Test Split
#=========================================================

X_train,X_test,Y_train,Y_test = train_test_split(X_vector,Y,test_size=0.2,random_state=42)

#=========================================================
# Part 4 : Model Training
#=========================================================

#---------------------------------------------
# step 1 : create models
#---------------------------------------------

log_model = LogisticRegression()
dt_model = DecisionTreeClassifier()

#---------------------------------------------
# step 2 : train models
#---------------------------------------------

log_model.fit(X_train,Y_train)
dt_model.fit(X_train,Y_train)

#---------------------------------------------
# step 3 : Voting Classifier (Hard)
#---------------------------------------------

hard_model = VotingClassifier(
    estimators=[('lr',log_model), ('dt',dt_model)],
    voting='hard'
)

hard_model.fit(X_train,Y_train)

#---------------------------------------------
# step 4 : Voting Classifier (Soft)
#---------------------------------------------

soft_model = VotingClassifier(
    estimators=[('lr',log_model), ('dt',dt_model)],
    voting='soft'
)

soft_model.fit(X_train,Y_train)

#=========================================================
# Part 5 : Evaluation
#=========================================================

#---------------------------------------------
# step 1 : predictions
#---------------------------------------------

log_pred = log_model.predict(X_test)
dt_pred = dt_model.predict(X_test)
hard_pred = hard_model.predict(X_test)
soft_pred = soft_model.predict(X_test)

#---------------------------------------------
# step 2 : accuracy
#---------------------------------------------

print("Logistic Accuracy : ", accuracy_score(Y_test,log_pred))
print("Decision Tree Accuracy : ", accuracy_score(Y_test,dt_pred))
print("Hard Voting Accuracy : ", accuracy_score(Y_test,hard_pred))
print("Soft Voting Accuracy : ", accuracy_score(Y_test,soft_pred))

#---------------------------------------------
# step 3 : confusion matrix
#---------------------------------------------

print("Logistic Confusion Matrix : ")
print(confusion_matrix(Y_test,log_pred))

print("Decision Tree Confusion Matrix : ")
print(confusion_matrix(Y_test,dt_pred))

print("Hard Voting Confusion Matrix : ")
print(confusion_matrix(Y_test,hard_pred))

print("Soft Voting Confusion Matrix : ")
print(confusion_matrix(Y_test,soft_pred))