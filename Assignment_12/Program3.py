"""Write a program which accepts two numbers and prints addition, subtraction, 
multiplication and division
"""

def Add(No1 , No2):
    ans = No1 + No2
    print("Addition is : ", ans)

def Sub(No1 , No2):
    ans = No1 - No2
    print("substraction is : ", ans)

def Mul(No1 , No2):
    ans = No1 * No2
    print("Multiplication is : ", ans)


def Div(No1 , No2):
    ans = No1 // No2
    print("Division is : ", ans)

def main():
    
    No1 = int(input("Enter number 1 : "))
    No2 = int(input("Enter number 2 : "))

    Add(No1,No2)
    Sub(No1,No2)
    Mul(No1,No2)
    Div(No1,No2)


if __name__ == "__main__":
    main()
