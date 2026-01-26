""". Write a program which accept number from user and return addition of digits in that number. 
    Input : 1234
    Output : 10
"""


def SumDigit(no):  
    iDigit = 0
    sum = 0
    while(no != 0):
         iDigit = no % 10
         sum = sum + iDigit
         no = no // 10
    return sum
         
def main():
    no = int(input("Enter number : "))

    iRet = SumDigit(no)

    print("sum of digits is : ", iRet)
    
if __name__ == "__main__":      
        main()

