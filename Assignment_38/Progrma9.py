import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*40
 
###################################################################################
# Step 9 : AssignmentsCompleted vs FinalResult
###################################################################################
print(Border)
print("Step 9 : Assignments vs Result")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])

plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")

plt.show()