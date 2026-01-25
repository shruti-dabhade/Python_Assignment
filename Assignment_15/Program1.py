""" Write a lambda function using map() which accepts a list of numbers and returns a list of squares of 
each number."""

Square = lambda no : no * no


def main():
    Data = [2, 3, 4, 5]
    print("Data before square : ",Data)

    mData = list(map(Square, Data))
    print("Data after map is : ", mData)

if __name__ == "__main__":
    main()