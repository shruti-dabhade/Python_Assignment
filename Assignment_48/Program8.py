"""8. Write a Python program that calculates TP, TN, FP, FN for the following arrays:
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]
Display all four values"""

#---------------------------------------------
# step 1 : create data
#---------------------------------------------

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

TP = 0
TN = 0
FP = 0
FN = 0

#---------------------------------------------
# step 2 : calculate values
#---------------------------------------------

for i in range(len(actual)):

    if actual[i] == 1 and predicted[i] == 1:
        TP = TP + 1

    elif actual[i] == 0 and predicted[i] == 0:
        TN = TN + 1

    elif actual[i] == 0 and predicted[i] == 1:
        FP = FP + 1

    elif actual[i] == 1 and predicted[i] == 0:
        FN = FN + 1

#---------------------------------------------
# step 3 : display result
#---------------------------------------------

print("True Positive : ", TP)
print("True Negative : ", TN)
print("False Positive : ", FP)
print("False Negative : ", FN)