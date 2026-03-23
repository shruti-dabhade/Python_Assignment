"""1. Exploratory Data Analysis (EDA):
• Load the dataset using pandas.
• Display the first 5 rows.
• Show column info and check for null values.
• Display basic statistics using .describe().
• Plot the distribution of the target variable (Outcome).
• Use graphs like hist, boxplot, or pairplot to identify patterns or outliers"""

import pandas as pd
import matplotlib.pyplot as plt

#---------------------------------------------
# step 1 : load dataset
#---------------------------------------------

df = pd.read_csv("diabetes.csv")

print("Shape of dataset : ", df.shape)

#---------------------------------------------
# step 2 : display first 5 records
#---------------------------------------------

print("First 5 records : ")
print(df.head())

#---------------------------------------------
# step 3 : dataset info
#---------------------------------------------

print("Dataset Info : ")
print(df.info())

#---------------------------------------------
# step 4 : null values
#---------------------------------------------

print("Null values : ")
print(df.isnull().sum())

#---------------------------------------------
# step 5 : statistics
#---------------------------------------------

print("Statistics : ")
print(df.describe())

#---------------------------------------------
# step 6 : plot target variable
#---------------------------------------------

df['Outcome'].value_counts().plot(kind='bar')
plt.title("Outcome Distribution")
plt.show()