"""  
2. Write a program which accepts one number and prints sum of first N natural numbers.
Input: 5 
Output: 15 
"""

num = int(input("Enter the number: "))
sum =0 

while(num > 0):
    sum = sum + num
    num = num - 1 
print(f"sum of first natural num",sum)




