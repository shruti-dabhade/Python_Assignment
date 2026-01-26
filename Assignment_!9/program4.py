"""
.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which are even. Map function will calculate its square. 
Reduce will return addition of all that numbers. 
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10] 
List after map = [4, 16, 16, 4, 64, 100] 
Output of reduce = 204 
"""

from functools import reduce

numbers = []
n = int(input("Enter number of elements: "))

print("Enter elements:")
for i in range(n):
    numbers.append(int(input()))

filtered = list(filter(lambda x: x % 2 == 0, numbers))


mapped = list(map(lambda x: x * x, filtered))


result = reduce(lambda x, y: x + y, mapped)

print("Input List =", numbers)
print("List after filter =", filtered)
print("List after map =", mapped)
print("Output of reduce =", result)
