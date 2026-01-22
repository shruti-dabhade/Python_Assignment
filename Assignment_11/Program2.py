"""Write a program which accepts one number and prints count of digits in that number.
Input: 7521 
Output: 4"""

num = int(input("Enter the number"))
count = 0
iDigit = 0

while(num != 0):
    iDigit = num % 10
    count = count + 1
    num = num //  10

print("Number of Digits are: ", count)