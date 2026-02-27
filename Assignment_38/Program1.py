import pandas as pd

Border = "-"*40
 
###################################################################################
# Step 1 : Load the data set
###################################################################################
print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully")

print("\nFirst 5 records")
print(df.head())

print("\nLast 5 records")
print(df.tail())

print("\nTotal rows and columns")
print(df.shape)

print("\nList of column names")
print(df.columns)

print("\nData types of each column")
print(df.dtypes)

