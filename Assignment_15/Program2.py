"""Write a lambda function using filter() which accepts a list of numbers and returns a list of even 
numbers."""


CheckEven   = lambda no : (no % 2 == 0)


def main():
    Data = [1, 2, 3, 4, 5,6, 7, 8, 9 ,10]
    print("Data  : ",Data)

    mData = list(filter(CheckEven,Data))
    print("Data after even check : ", mData)

if __name__ == "__main__":
    main()