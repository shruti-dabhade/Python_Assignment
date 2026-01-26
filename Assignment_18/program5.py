""".Write a program which accept N numbers from user and store it into List. Return addition of all 
prime numbers from that List. Main python file accepts N numbers from user and pass each 
number to ChkPrime() function which is part of our user defined module named as 
MarvellousNum. Name of the function from main python file should be ListPrime(). 

    Input : Number of elements : 11 
    Input Elment : 13 5  45 7 4  56 10 34 2 5 8 
    Output : 54 (13 + 5 + 7 +2 + 5) 
""" 


import Marvellous

def ListPrime(numbers):
    total = 0
    for num in numbers:
        if Marvellous.ChkPrime(num):
            total += num
    return total

def main():
    n = int(input("Enter number of elements: "))

    numbers = []
    print("Enter elements:")
    for i in range(n):
        value = int(input())
        numbers.append(value)

    result = ListPrime(numbers)
    print("Addition of all prime numbers:", result)

if __name__ == "__main__":
    main()
