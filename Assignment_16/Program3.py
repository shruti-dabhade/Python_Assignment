"""
 Write a program which contains one function named as Add() which accepts two numbers 
from user and return addition of that two numbers. 
    Input : 11    5   
    Output : 16 
"""

def Add(no1, no2):
    ans = no1 + no2
    return ans

def main():
    no1 = int(input("Enter number 1 : "))
    no2 = int(input("Enter number 2 : "))

    Ret = Add(no1, no2)

    print("Addition is : ", Ret)


if __name__ == "__main__":      
        main()