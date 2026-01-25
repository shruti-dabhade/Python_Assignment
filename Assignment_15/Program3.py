"""Write a lambda function using filter() which accepts a list of numbers and returns a list of odd 
numbers."""


CheckOdd   = lambda no : (no % 2 == 1)


def main():
    Data = [1, 2, 3, 4, 5,6, 7, 8, 9 ,10]
    print("Data  : ",Data)

    mData = list(filter(CheckOdd,Data))
    print("Data after odd check : ", mData)

if __name__ == "__main__":
    main()