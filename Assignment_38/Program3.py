import pandas as pd

Border = "-"*40
 
###################################################################################
# Step 3 : Statistical Analysis
###################################################################################
print(Border)
print("Step 3 : Statistical Measures")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Average StudyHours :", df["StudyHours"].mean())
print("Average Attendance :", df["Attendance"].mean())
print("Maximum PreviousScore :", df["PreviousScore"].max())
print("Minimum SleepHours :", df["SleepHours"].min())