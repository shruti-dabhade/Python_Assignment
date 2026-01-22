
"""5. Write a program which accepts one number and checks whether it is palindrome or not.
 Input: 121 
Output: Palindrome
"""

num = int(input("Enter the number"))
Rev = 0
iDigit = 0
temp = num

while(temp != 0):
    iDigit = temp % 10
    Rev = Rev * 10 +iDigit
    temp = temp //  10

if(num == Rev):
    print("number is palindrome")
else:
    print("Number is not palindrome")