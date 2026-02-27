import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*40
 
###################################################################################
# Step 7 : Scatter Plot StudyHours vs PreviousScore
###################################################################################
print(Border)
print("Step 7 : Scatter Plot")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

pass_data = df[df["FinalResult"] == 1]
fail_data = df[df["FinalResult"] == 0]

plt.scatter(pass_data["StudyHours"], pass_data["PreviousScore"], label="Pass")
plt.scatter(fail_data["StudyHours"], fail_data["PreviousScore"], label="Fail")

plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.legend()

plt.show()