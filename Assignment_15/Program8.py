"""Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers 
divisible by both 3 and 5"""



isDivisble   = lambda no : ( no % 3 == 0) and (no % 5 == 0)


def main():
    Data = [2, 3,  12, 15, 10]
    print("Data  : ",Data)

    mData = list(filter(isDivisble, Data))
    print("list of numbers divisible by both 3 and 5 ", mData)

if __name__ == "__main__":
    main()