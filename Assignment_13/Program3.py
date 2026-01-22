""" Write a program which accepts one number and checks whether it is perfect number or 
not.
Input: 6 
Output: Perfect Number
"""

num = int (input("Enter number : "))
sum = 0
for iCnt in range( 1, num):
    if(num % iCnt == 0 ):
        sum = sum + iCnt

if(num == sum):
    print("The number is perfect")
else:
    print("Number is not perfect")