"""1. Load and Explore the Dataset
◦ Handle missing or unknown values (e.g., unknown in categorical features).
◦ Display basic stats and visualize class distribution."""

import pandas as pd
import matplotlib.pyplot as plt

#---------------------------------------------
# step 1 : load dataset
#---------------------------------------------

df = pd.read_csv("bank.csv")

print("Shape of dataset : ", df.shape)

#---------------------------------------------
# step 2 : first 5 records
#---------------------------------------------

print(df.head())

#---------------------------------------------
# step 3 : info
#---------------------------------------------

print(df.info())

#---------------------------------------------
# step 4 : check missing / unknown values
#---------------------------------------------

print(df.isnull().sum())

#---------------------------------------------
# step 5 : class distribution
#---------------------------------------------

df['y'].value_counts().plot(kind='bar')
plt.title("Target Distribution")
plt.show()