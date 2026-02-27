import pandas as pd

Border = "-"*40
 
###################################################################################
# Step 2 : Student Count
###################################################################################
print(Border)
print("Step 2 : Total Students, Pass & Fail Count")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Total number of students :", len(df))

passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()

print("Students Passed :", passed)
print("Students Failed :", failed)