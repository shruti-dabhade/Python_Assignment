import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*40
 
###################################################################################
# Step 8 : Boxplot of Attendance
###################################################################################
print(Border)
print("Step 8 : Boxplot")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

plt.boxplot(df["Attendance"])

plt.title("Attendance Boxplot")

plt.show()