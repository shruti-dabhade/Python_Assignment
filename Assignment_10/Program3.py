"""Write a program which accepts one number and prints factorial of that number.
Input: 5 
Output: 120"""

num = int(input("Enter the number: "))
fact = 1 

while(num > 0):
    fact = fact * num
    num = num - 1 
print("factorial is",fact)
