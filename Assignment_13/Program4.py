""" Write a program which accepts one number and prints binary equivalent.
"""

num = int (input("Enter number : "))

while(num != 0):
    rem = num % 2
    print(rem)
    num = num // 2