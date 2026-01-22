""" Write a program which accepts one character and checks whether it is vowel or 
consonant.
Input: a 
Output: Vowel
"""


ch = input("Enter character : ")

if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print("Entered character is vowel")
else:
    print("Entered chracter is constant or special symbol or digit ")