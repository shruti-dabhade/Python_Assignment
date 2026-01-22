 # Write a program which accepts one number and prints multiplication table of that 
# number.
# input: 4 
# # output: 4 , 8, 12,16, 20,24,28,32,36,40


def Multiplication(no):

    for  iCnt in range( 1,11):   # iCnt use for counter #
        print( no ,"x", iCnt, "=", no * iCnt)

def main():
    Multiplication(4)


if __name__ == "__main__":
    main()



"""num = int(input("Enter the number: "))

for i in range(1,11):
    print(num, "x", i, "=", num * i)"""


