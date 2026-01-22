"""  Write a program which accepts one number and prints that many numbers in reverse 
order.
Input: 5 
Output: 5 4 3 2 1

"""

num = int(input("Enter number : "))
print(" Number in numbers in reverse order")
for iCnt in range(num  , 0, -1):
    print(iCnt)