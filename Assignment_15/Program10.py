"""Write a lambda function using filter() which accepts a list of numbers and returns the count of even 
numbers"""


from functools import reduce
countEven = lambda x: x % 2 == 0


def main():
    Data = [1, 2, 3, 4, 5]
    print("Data  : ",Data)

    mData = list(filter(countEven, Data))
    print("count of even numbers ", mData)

if __name__ == "__main__":
    main()