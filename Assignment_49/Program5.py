"""5. Final Output:
• Predict whether a patient is diabetic based on test data.
• Display predictions on screen and save them in a CSV file"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#---------------------------------------------
# step 1 : load dataset
#---------------------------------------------

df = pd.read_csv("diabetes.csv")

X = df.drop("Outcome", axis=1)
Y = df["Outcome"]

#---------------------------------------------
# step 2 : split dataset
#---------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#---------------------------------------------
# step 3 : train model
#---------------------------------------------

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

#---------------------------------------------
# step 4 : predict
#---------------------------------------------

Y_pred = model.predict(X_test)

print("Predictions : ")
print(Y_pred)

#---------------------------------------------
# step 5 : save output
#---------------------------------------------

output = pd.DataFrame({"Actual":Y_test, "Predicted":Y_pred})

output.to_csv("output.csv", index=False)

print("Output saved in output.csv")