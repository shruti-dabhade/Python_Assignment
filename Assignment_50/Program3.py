"""3. Split the Data
◦ Use 80% data for training and 20% for testing.
◦ Apply train_test_split()."""

from sklearn.model_selection import train_test_split
import pandas as pd

#---------------------------------------------
# step 1 : load dataset
#---------------------------------------------

df = pd.read_csv("bank.csv")

#---------------------------------------------
# step 2 : encoding
#---------------------------------------------

df = pd.get_dummies(df)

#---------------------------------------------
# step 3 : split data
#---------------------------------------------

X = df.drop("y_yes", axis=1)
Y = df["y_yes"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Training size : ", X_train.shape)
print("Testing size : ", X_test.shape)