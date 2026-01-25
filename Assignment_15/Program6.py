"""Write a lambda function using reduce() which accepts a list of numbers and returns the minimum 
element"""

from functools import reduce
Min   = lambda no1, no2 :  no1 if no1 < no2 else no2


def main():
    Data = [11, 80, 3, 22]
    print("Data  : ",Data)

    mData = reduce(Min, Data)
    print("Min: ", mData)

if __name__ == "__main__":
    main()