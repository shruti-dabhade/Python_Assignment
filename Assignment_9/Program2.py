# Write a program which contains one function ChkGreater() that accepts two numbers 
# and prints the greater number
# Input : 10 , 20
# Output : 20 is greater number


def ChkGreater(No1,No2):
    if(No1 > No2):
    #    print(f"{No1} is greater number")
        print(No1, "is greater number")
    else:
    #    print(f"{No2} is greater number")
        print(No2, "is greater number")



def main():
    ChkGreater(10,20)


if __name__ == "__main__":
    main()