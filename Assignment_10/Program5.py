"""Write a program which accepts one number and prints all odd numbers till that 
number.
Input: 10 
Output: 1 3 5 7 9  """

num = int(input("Enter the number"))
print("odd numbers are")
for i in range(1,11):
    if (i % 2 != 0):
        print(i)