"""Write a lambda function using filter() which accepts a list of strings and returns a list of strings 
having length greater than 5"""



length   = lambda str :  len(str) > 5


def main():
    Data = ["Hi", "Hello", "a", "marvellous"]
    print("Data  : ",Data)

    mData = list(filter(length, Data))
    print("list of strings having length greater than 5: ", mData)

if __name__ == "__main__":
    main()