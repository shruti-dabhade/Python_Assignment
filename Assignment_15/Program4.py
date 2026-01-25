"""Write a lambda function using reduce() which accepts a list of numbers and returns the addition of 
all elements"""

from functools import reduce
Add   = lambda no1, no2 : no1 + no2


def main():
    Data = [1, 2, 3, 4, 5,6, 7, 8, 9 ,10]
    print("Data  : ",Data)

    mData = reduce(Add, Data)
    print("Data after Add : ", mData)

if __name__ == "__main__":
    main()