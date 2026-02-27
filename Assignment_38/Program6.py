import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*40
 
###################################################################################
# Step 6 : Histogram of StudyHours
###################################################################################
print(Border)
print("Step 6 : Histogram")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

plt.hist(df["StudyHours"], bins=10)

plt.title("StudyHours Distribution")
plt.xlabel("StudyHours")
plt.ylabel("Number of Students")

plt.show()