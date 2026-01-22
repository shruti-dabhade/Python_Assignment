"""Write a program which accepts one number and prints sum of digits.
Input: 123 
Output: 6
"""

num = int(input("Enter the number"))
sum = 0
iDigit = 0

while(num != 0):
    iDigit = num % 10
    sum = sum + iDigit
    num = num //  10

print("sum of Digits are: ", sum)