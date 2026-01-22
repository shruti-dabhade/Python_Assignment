"""Write a program which accepts one number and prints reverse of that number.
Input: 123 
Output: 321
"""



num = int(input("Enter the number"))
Rev = 0
iDigit = 0

while(num != 0):
    iDigit = num % 10
    Rev = Rev * 10 +iDigit
    num = num //  10

print(" Reverse number is : ", Rev)