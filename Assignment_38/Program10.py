import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*40
 
###################################################################################
# Step 10 : SleepHours vs FinalResult
###################################################################################
print(Border)
print("Step 10 : Sleep vs Result")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

plt.scatter(df["SleepHours"], df["FinalResult"])

plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")

plt.show()