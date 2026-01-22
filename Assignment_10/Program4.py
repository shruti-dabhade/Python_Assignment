"""Write a program which accepts one number and prints all even numbers till that 
number.
Input: 10 
Output: 2 4 6 8 10"""

num = int(input("Enter the number"))
print("Even numbers are")
for i in range(1,11):
    if (i % 2 == 0):
        print(i)