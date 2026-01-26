"""
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
parameters as number and perform the operation. Write on python program which call all the 
functions from Arithmetic module by accepting the parameters from user. 
"""

import Arithmetic


def main():
    no1 = int(input("Enter number 1 :"))
    no2 = int(input("Enter number 2 : "))
    
    print("Addition is : ",Arithmetic.Add(no1, no2))
    print("Substraction is : ",Arithmetic.Sub(no1, no2))
    print("Multiplication is : ",Arithmetic.Mul(no1, no2))
    print("Division is : ",Arithmetic.Div(no1, no2))
    
if __name__ == "__main__":      
        main()