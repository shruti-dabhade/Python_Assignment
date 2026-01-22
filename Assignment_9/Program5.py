# Write a program which accepts one number and checks whether it is divisible by 3 and 5
#  Input: 15 
# Output: Divisible by 3 and 


def Is_Divisible(No):

    if((No % 3 == 0 ) and (No % 5 == 0)):
        print("It is divisible by 3 and 5")
    else:
        print("It is not divisible by 3 and 5")

def main():
    Is_Divisible(15)

if __name__ == "__main__":
    main()