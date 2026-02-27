import pandas as pd

Border = "-"*40
 
###################################################################################
# Step 4 : FinalResult Distribution
###################################################################################
print(Border)
print("Step 4 : Distribution of Pass/Fail")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

counts = df["FinalResult"].value_counts()

print("Distribution :")
print(counts)

total = len(df)

pass_percent = (counts[1] / total) * 100
fail_percent = (counts[0] / total) * 100

print("Pass Percentage :", pass_percent)
print("Fail Percentage :", fail_percent)

if abs(pass_percent - fail_percent) < 10:
    print("Dataset is Balanced")
else:
    print("Dataset is Imbalanced")