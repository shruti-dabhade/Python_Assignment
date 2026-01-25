"""Write a lambda function using reduce() which accepts a list of numbers and returns the product of all 
elements"""


from functools import reduce
product = lambda x, y : x * y


def main():
    Data = [1, 2, 3, 4, 5]
    print("Data  : ",Data)

    mData = reduce(product, Data)
    print("product of all elements ", mData)

if __name__ == "__main__":
    main()