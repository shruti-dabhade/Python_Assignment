""". Write a program which accepts one number and prints its factors.
Input: 12 
Output: 1 2 3 4 6 12
"""

num = int(input ("Enter number : "))

print("Factors are : ")
for iCnt in range(1, (num + 1)):
    if(num % iCnt == 0):
        print(iCnt)