"""Write a program which accepts one number and checks whether it is prime or not.
Input: 11 
Output: Prime Number"""

num = int(input("Enter the number"))
bFlag = True
for i in range(2,num):
    if(num % i == 0):
        bFlag = False
if(bFlag):
    print("number is prime")
else:
    print("number is not prime")
